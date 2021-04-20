from requestMaker import set_simulation_delay, start_stepped_simulation
from helpers import SimulationDriver
import platform
import threading
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import Radiobutton
else:
    import Tkinter as tk
    from Tkinter import Radiobutton

if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class InProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = tk.StringVar()
        self.simulation_text = tk.StringVar()
        self.simulation_name = tk.StringVar()
        self.delay = tk.IntVar()

        self.grid_rowconfigure(0, weight = 1, minsize=4)
        self.grid_rowconfigure(1, weight = 5, minsize=4)
        self.grid_rowconfigure(2, weight = 2, minsize=4)
        self.grid_rowconfigure(3, weight = 2, minsize=4)

        for number in range(0,10):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        tk.Label(self, textvariable=self.simulation_text, font=("Courier", 13)).grid(row=0, column=0, columnspan=10, sticky='nesw')

        Radiobutton(self, text="0ms", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=0, command=self.set_new_delay).grid(row=1, column=0, sticky='nesw')
        Radiobutton(self, text="100ms", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=100, command=self.set_new_delay).grid(row=1, column=1, sticky='nesw')
        Radiobutton(self, text="300ms", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=300, command=self.set_new_delay).grid(row=1, column=2, sticky='nesw')
        Radiobutton(self, text="500ms", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=500, command=self.set_new_delay).grid(row=1, column=3, sticky='nesw')
        Radiobutton(self, text="1s", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=1000, command=self.set_new_delay).grid(row=1, column=4, sticky='nesw')
        Radiobutton(self, text="1.5s", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=1500, command=self.set_new_delay).grid(row=1, column=5, sticky='nesw')
        Radiobutton(self, text="2s", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=2000, command=self.set_new_delay).grid(row=1, column=6, sticky='nesw')
        Radiobutton(self, text="2.5s", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=2500, command=self.set_new_delay).grid(row=1, column=7, sticky='nesw')
        Radiobutton(self, text="3s", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=3000, command=self.set_new_delay).grid(row=1, column=8, sticky='nesw')
        Radiobutton(self, text="5s", variable=self.delay, bg='#B2FFB0', activebackground='#B2FFB0', value=5000, command=self.set_new_delay).grid(row=1, column=9, sticky='nesw')

        
        tk.Button(self, text="Stepped simulation", bg='#3399ff', activebackground='#3399ff',
                           command=lambda: self.show_stepped_simulation(self.controller, self.simulation_name.get(), self.shape.get()), font=("Courier", 13)).grid(row=2, column=0, columnspan=10, sticky='nesw')

        tk.Button(self, text="Stop", bg='#FFBEB0', activebackground='#FFBEB0',
                           command=lambda: SimulationDriver.kill_simulation_and_back_to_start(controller), font=("Courier", 13)).grid(row=3, column=0, columnspan=10, sticky='nesw')

    def set_shape(self, shape):
        self.shape.set(shape)

    def set_new_delay(self):
        threading.Thread(target=set_simulation_delay, args=(self.delay.get(),)).start()
        
    def show_stepped_simulation(self, controller, simulation_name, shape):
        start_stepped_simulation()
        controller.frames["InProgressSteppedPage"].set_shape(shape)
        controller.frames["InProgressSteppedPage"].set_simulation_name(simulation_name)
        controller.frames["InProgressSteppedPage"].tkraise()

    def set_simulation_name(self, simulation_name):
        self.simulation_name.set(simulation_name)
        text = simulation_name + " " + self.shape.get() + " simulation in progress..." 
        self.simulation_text.set(text.capitalize())