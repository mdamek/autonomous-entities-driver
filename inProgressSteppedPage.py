from colors import Colors
from requestMaker import make_iteration, stop_stepped_simulation
import scripts_runner as sr
import threading
import tkinter as tk


class InProgressSteppedPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def render_in_progress_simulation(self, simulation):
        self.simulation = simulation
        self.grid_rowconfigure(0, weight=1, minsize=4)
        self.grid_rowconfigure(1, weight=2, minsize=4)
        self.grid_rowconfigure(2, weight=2, minsize=4)
        self.grid_rowconfigure(3, weight=2, minsize=4)

        for number in range(0, 1):
            self.grid_columnconfigure(number, weight=1, minsize=4)

        tk.Label(self, text=self.simulation.config["name"].capitalize() + " simulation", font=(
            "Courier", 13)).grid(row=0, column=0, columnspan=1, sticky='nesw')
        tk.Button(self, text="Next iteration", bg=Colors.Green, activebackground=Colors.Green,
                  command=lambda: self.make_next_iteration()).grid(row=1, column=0, columnspan=1, sticky='nesw')
        tk.Button(self, text="Continuous simulation", bg=Colors.Blue, activebackground=Colors.Blue,
                  command=lambda: self.show_classical_simulation()).grid(row=2, column=0, columnspan=1, sticky='nesw')
        tk.Button(self, text="Stop", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: self.stop_simulation()).grid(row=3, column=0, columnspan=1, sticky='nesw')

    def show_classical_simulation(self):
        stop_stepped_simulation()
        self.controller.frames["InProgressPage"].render_page(
            self.simulation)
        self.controller.frames["InProgressPage"].tkraise()

    def make_next_iteration(self):
        threading.Thread(target=make_iteration).start()

    def stop_simulation(self):
        self.controller.frames["StartPage"].tkraise()
        sr.kill_simulation()
