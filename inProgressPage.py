from colors import Colors
from requestMaker import set_simulation_delay, start_stepped_simulation
import scripts_runner as sr
import threading
import tkinter as tk
from tkinter import Radiobutton, Label


class InProgressPage(tk.Frame):
    def __init__(self, parent, controller, config):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config = config

    def render_page(self, simualtion):
        self.simulation = simualtion
        self.delay = tk.IntVar()

        self.grid_rowconfigure(0, weight=1, minsize=4)
        self.grid_rowconfigure(1, weight=1, minsize=4)
        self.grid_rowconfigure(4, weight=2, minsize=4)
        self.grid_rowconfigure(5, weight=2, minsize=4)

        for number in range(0, 10):
            self.grid_columnconfigure(number, weight=1, minsize=4)

        tk.Label(self, text=self.simulation.config["name"].capitalize() + " simulation", font=("Courier", 13)).grid(
            row=0, column=0, columnspan=10, sticky='nesw')
        tk.Label(self, text="Iteration space time", font=("Courier", 10)).grid(
            row=1, column=0, columnspan=10, sticky='nesw')

        for idx, delay in enumerate(self.config["delayValues"]):
            Radiobutton(self, variable=self.delay, value=delay["value"],
                        command=self.set_new_delay).grid(row=2, column=idx)
            Label(self, text=delay["name"]).grid(row=3, column=idx)

        tk.Button(self, text="Step simulation", bg=Colors.Blue, activebackground=Colors.Blue,
                  command=lambda: self.show_stepped_simulation(), font=("Courier", 13)).grid(row=4, column=0, columnspan=10, sticky='nesw')

        tk.Button(self, text="Stop", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.stop_simulation(), font=("Courier", 13)).grid(row=5, column=0, columnspan=10, sticky='nesw')

    def set_new_delay(self):
        threading.Thread(target=set_simulation_delay,
                         args=(self.delay.get(),)).start()

    def show_stepped_simulation(self):
        start_stepped_simulation()
        self.controller.frames["InProgressSteppedPage"].render_in_progress_simulation(
            self.simulation)
        self.controller.frames["InProgressSteppedPage"].tkraise()

    def reset_speed(self):
        self.delay.set(0)

    def stop_simulation(self):
        self.controller.frames["StartPage"].tkraise()
        sr.kill_simulation()
