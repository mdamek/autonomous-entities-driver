from colors import Colors
from requestMaker import set_simulation_delay, start_stepped_simulation
import scripts_runner as sr
import platform
import threading
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import Radiobutton, Label
else:
    import Tkinter as tk
    from Tkinter import Radiobutton, Label


class InProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def render_page(self):
        self.delay = tk.IntVar()

        self.grid_rowconfigure(0, weight=1, minsize=4)
        self.grid_rowconfigure(1, weight=1, minsize=4)
        self.grid_rowconfigure(4, weight=2, minsize=4)
        self.grid_rowconfigure(5, weight=2, minsize=4)

        for number in range(0, 10):
            self.grid_columnconfigure(number, weight=1, minsize=4)

        tk.Label(self, text=self.simulation.config["name"].capitalize(), font=("Courier", 13)).grid(
            row=0, column=0, columnspan=10, sticky='nesw')
        tk.Label(self, text="Iteration space time", font=("Courier", 10)).grid(
            row=1, column=0, columnspan=10, sticky='nesw')

        Radiobutton(self, variable=self.delay, value=0,
                    command=self.set_new_delay).grid(row=2, column=0)
        Radiobutton(self, variable=self.delay, value=100,
                    command=self.set_new_delay).grid(row=2, column=1)
        Radiobutton(self, variable=self.delay, value=300,
                    command=self.set_new_delay).grid(row=2, column=2)
        Radiobutton(self, variable=self.delay, value=500,
                    command=self.set_new_delay).grid(row=2, column=3)
        Radiobutton(self, variable=self.delay, value=1000,
                    command=self.set_new_delay).grid(row=2, column=4)
        Radiobutton(self, variable=self.delay, value=1500,
                    command=self.set_new_delay).grid(row=2, column=5)
        Radiobutton(self, variable=self.delay, value=2000,
                    command=self.set_new_delay).grid(row=2, column=6)
        Radiobutton(self, variable=self.delay, value=2500,
                    command=self.set_new_delay).grid(row=2, column=7)
        Radiobutton(self, variable=self.delay, value=3000,
                    command=self.set_new_delay).grid(row=2, column=8)
        Radiobutton(self, variable=self.delay, value=5000,
                    command=self.set_new_delay).grid(row=2, column=9)

        Label(self, text="Without").grid(row=3, column=0)
        Label(self, text="100ms").grid(row=3, column=1)
        Label(self, text="300ms").grid(row=3, column=2)
        Label(self, text="500ms").grid(row=3, column=3)
        Label(self, text="1s").grid(row=3, column=4)
        Label(self, text="1.5s").grid(row=3, column=5)
        Label(self, text="2s").grid(row=3, column=6)
        Label(self, text="2.5s").grid(row=3, column=7)
        Label(self, text="3s").grid(row=3, column=8)
        Label(self, text="5s").grid(row=3, column=9)

        tk.Button(self, text="Step simulation", bg=Colors.Blue, activebackground=Colors.Blue,
                  command=lambda: self.show_stepped_simulation(), font=("Courier", 13)).grid(row=4, column=0, columnspan=10, sticky='nesw')

        tk.Button(self, text="Stop", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.stop_simulation(), font=("Courier", 13)).grid(row=5, column=0, columnspan=10, sticky='nesw')

    def set_simulation(self, simulation):
        self.simulation = simulation

    def set_new_delay(self):
        threading.Thread(target=set_simulation_delay,
                         args=(self.delay.get(),)).start()

    def show_stepped_simulation(self):
        start_stepped_simulation()
        self.controller.frames["InProgressSteppedPage"].set_simulation(
            self.simulation)
        self.controller.frames["InProgressSteppedPage"].tkraise()

    def reset_speed(self):
        self.delay.set(0)

    def stop_simulation(self):
        self.controller.frames["StartPage"].tkraise()
        sr.kill_simulation()
