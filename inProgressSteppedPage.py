import platform
from requestMaker import make_iteration, stop_stepped_simulation
from helpers import SimulationDriver
import threading

if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class InProgressSteppedPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = tk.StringVar()
        self.simulation_name = tk.StringVar()
        self.simulation_text = tk.StringVar()

        self.grid_rowconfigure(0, weight = 1, minsize=4)
        self.grid_rowconfigure(1, weight = 2, minsize=4)
        self.grid_rowconfigure(2, weight = 2, minsize=4)
        self.grid_rowconfigure(3, weight = 2, minsize=4)

        for number in range(0,1):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        tk.Label(self, textvariable=self.simulation_text, font=("Courier", 13)).grid(row=0, column=0, columnspan=1, sticky='nesw')
        tk.Button(self, text="Next iteration", bg='#B2FFB0', activebackground='#B2FFB0',
                            command=lambda: self.make_next_iteration()).grid(row=1, column=0, columnspan=1, sticky='nesw')
        tk.Button(self, text="Smooth simulation", bg='#3399ff', activebackground='#3399ff',
                            command=lambda: self.show_classical_simulation(self.controller, self.simulation_name.get(), self.shape.get())).grid(row=2, column=0,columnspan=1, sticky='nesw')
        tk.Button(self, text="Stop", bg='#FFBEB0', activebackground='#FFBEB0',
                            command=lambda: SimulationDriver.kill_simulation_and_back_to_start(controller)).grid(row=3, column=0,columnspan=1, sticky='nesw')

    def set_shape(self, shape):
        self.shape.set(shape)

    def show_classical_simulation(self, controller, simulation_name, shape):
        stop_stepped_simulation()
        controller.frames["InProgressPage"].set_shape(shape)
        controller.frames["InProgressPage"].set_simulation_name(simulation_name)
        controller.frames["InProgressPage"].tkraise()

    def make_next_iteration(self):
        threading.Thread(target=make_iteration).start()

    def set_simulation_name(self, simulation_name):
        self.simulation_name.set(simulation_name)
        text = simulation_name + " " + self.shape.get() + " simulation in progress..." 
        self.simulation_text.set(text.capitalize())
