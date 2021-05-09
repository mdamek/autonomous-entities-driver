import threading
from colors import Colors
from requestMaker import configure_drawing_server, set_color, start_motion_sensor, stop_motion_sensor
import scripts_runner as sr
import tkinter as tk


class DrawPage(tk.Frame):
    def __init__(self, parent, controller, hosts):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.hosts = hosts

    def set_simulation(self, simulation):
        self.simulation = simulation

    def render_page(self):
        self.clear_page()
        configure_drawing_server(self.simulation)
        threading.Thread(target=start_motion_sensor,
                         args=(self.simulation.shape, )).start()

        avaliable_colors = self.simulation.config["avaliableToDraw"]
        self.selected_color = tk.StringVar()
        first_color = avaliable_colors[0][next(iter(avaliable_colors[0]))]
        self.selected_color.set(first_color)
        set_color(first_color)

        tk.Label(self, text="Select colors and draw starting position on panels",
                 font='Helvetica 14 bold').pack(side="top", fill="x")

        tk.Label(self, text="Selected color:",
                 font='Helvetica 14 bold').pack(side="top", fill="x")
        self.color_frame = tk.Frame(self, background=self.selected_color.get(
        ), height=30)
        self.color_frame.pack(side="top", fill=tk.BOTH, expand=True)

        tk.Frame(self, bg="light grey", height=20).pack(
            side="top", fill=tk.BOTH, expand=True)

        for color in avaliable_colors:
            for key, value in color.items():
                tk.Button(self, text=key.capitalize(), bg=value, activebackground=value,
                          command=lambda value=value: self.change_color(value)).pack(side="top", fill=tk.BOTH, expand=True)
        tk.Frame(self, bg="light grey", height=20).pack(
            side="top", fill=tk.BOTH, expand=True)

        tk.Button(self, text="Return", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.controller.frames["ParametersPage"].tkraise()).pack(side="top", fill=tk.BOTH, expand=True)
        tk.Button(self, text="Cancel", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.controller.frames["StartPage"].tkraise()).pack(side="top", fill=tk.BOTH, expand=True)
        tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green,
                  command=lambda: self.go_to_in_progress_page()).pack(side="top", fill=tk.BOTH, expand=True)

    def change_color(self, color):
        self.selected_color.set(color)
        self.color_frame.configure(bg=color)
        set_color(color)

    def go_to_in_progress_page(self):
        threading.Thread(target=stop_motion_sensor).start()
        if self.stepped:
            self.controller.frames["InProgressSteppedPage"].set_simulation(
                self.simulation)
            self.controller.frames["InProgressSteppedPage"].tkraise()
        else:
            self.controller.frames["InProgressPage"].set_simulation(
                self.simulation)
            self.controller.frames["InProgressPage"].tkraise()
        sr.run_xinuk(self.simulation)

    def clear_page(self):
        for widget in self.winfo_children():
            widget.destroy()
