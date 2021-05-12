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
        configure_drawing_server(self.simulation)
        threading.Thread(target=start_motion_sensor,
                         args=(self.simulation, )).start()

        avaliable_colors = self.simulation.config["avaliableToDraw"]
        self.selected_color = tk.StringVar()
        self.selected_type = tk.StringVar()
        first_color = avaliable_colors[0][next(iter(avaliable_colors[0]))]
        first_type = next(iter(avaliable_colors[0]))
        self.selected_color.set(first_color)
        self.selected_type.set(first_type)
        set_color(first_color)

        number_of_addition_buttons = 5

        for number in range(0, len(avaliable_colors) + number_of_addition_buttons - 1):
            self.grid_rowconfigure(number, weight=1, minsize=4)

        for number in range(0, 3):
            self.grid_columnconfigure(number, weight=1, minsize=4)

        tk.Label(self, text="Select colors and draw starting position on panels",
                 font='Helvetica 14 bold').grid(row=0, column=0, columnspan=3, sticky='nesw')

        tk.Label(self, text="Selected:").grid(row=1, column=0, sticky='nesw')
        tk.Label(self, textvariable=self.selected_type).grid(
            row=1, column=1, sticky='nesw')
        self.color_frame = tk.Frame(self, background=self.selected_color.get())
        self.color_frame.grid(row=1, column=2, columnspan=3, sticky='nesw')
        tk.Label(self, text="").grid(
            row=2, column=0, columnspan=3, sticky='nesw')

        actual_row = 3
        for color in avaliable_colors:
            for key, value in color.items():
                tk.Radiobutton(self, text=key, variable=self.selected_color, value=value, command=lambda value=value,
                               key=key: self.change_color(key, value)).grid(row=actual_row, column=0, sticky='nesw')
                tk.Frame(self, bg=value).grid(row=actual_row,
                                              column=1, columnspan=3, sticky='nesw')
                actual_row = actual_row + 1

        tk.Button(self, text="Return", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.controller.frames["ParametersPage"].tkraise()).grid(row=actual_row, column=0, columnspan=3, sticky='nesw')
        tk.Button(self, text="Cancel", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.controller.frames["StartPage"].tkraise()).grid(row=actual_row + 1, column=0, columnspan=3, sticky='nesw')
        tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green,
                  command=lambda: self.go_to_in_progress_page()).grid(row=actual_row + 2, column=0, columnspan=3, sticky='nesw')

    def change_color(self, value, color):
        self.selected_color.set(color)
        self.selected_type.set(value)
        self.color_frame.config(background=self.selected_color.get())
        threading.Thread(target=set_color, args=(color, )).start()

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