from helpers import SimulationDriver
import platform
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class TorchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        spawnChance = tk.DoubleVar()  
        personSpawnChance = tk.DoubleVar()  
        fireSpawnChance = tk.DoubleVar()  
        exitSpawnChance = tk.DoubleVar()  
        personMaxSpeed = tk.DoubleVar()  
        fireSpreadingFrequency = tk.DoubleVar()  

        spawnChance.set(0.1)
        personSpawnChance.set(0.06)
        fireSpawnChance.set(0.03)
        exitSpawnChance.set(0.02)
        personMaxSpeed.set(1)
        fireSpreadingFrequency.set(5)

        for number in range(0, 8):
            self.grid_rowconfigure(number, weight = 1, minsize=4)

        for number in range(0,6):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        tk.Label(self, text="Spawn chance", font='Helvetica 9 bold').grid(row=0, column=0, rowspan=2, sticky='nesw')
        tk.Label(self, text="Person spawn chance", font='Helvetica 9 bold').grid(row=2, column=0, rowspan=2, sticky='nesw') 
        tk.Label(self, text="Fire spawn chance", font='Helvetica 9 bold').grid(row=4, column=0, rowspan=2, sticky='nesw')  

        tk.Label(self, textvariable=spawnChance, borderwidth=2, relief="sunken").grid(row=0, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=personSpawnChance, borderwidth=2, relief="sunken").grid(row=2, column=1, rowspan=2, sticky='nesw') 
        tk.Label(self, textvariable=fireSpawnChance, borderwidth=2, relief="sunken").grid(row=4, column=1, rowspan=2, sticky='nesw')  

        tk.Button(self, text="+", command=lambda: self.update_value(spawnChance, 0.1, "+")).grid(row=0, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(spawnChance, 0.1, "-")).grid(row=1, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(personSpawnChance, 0.1, "+")).grid(row=2, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(personSpawnChance, 0.1, "-")).grid(row=3, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(fireSpawnChance, 0.1, "+")).grid(row=4, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(fireSpawnChance, 0.1, "-")).grid(row=5, column=2, sticky='nesw')

        tk.Label(self, text="Exit spawn chance", font='Helvetica 9 bold').grid(row=0, column=3, rowspan=2, sticky='nesw')
        tk.Label(self, text="Person max speed", font='Helvetica 9 bold').grid(row=2, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Fire spreading frequency", font='Helvetica 9 bold').grid(row=4, column=3, rowspan=2, sticky='nesw')

        tk.Label(self, textvariable=exitSpawnChance, borderwidth=2, relief="sunken").grid(row=0, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=personMaxSpeed, borderwidth=2, relief="sunken").grid(row=2, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=fireSpreadingFrequency, borderwidth=2, relief="sunken").grid(row=4, column=4, rowspan=2, sticky='nesw')  

        tk.Button(self, text="+", command=lambda: self.update_value(exitSpawnChance, 0.1, "+")).grid(row=0, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(exitSpawnChance, 0.1, "-")).grid(row=1, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(personMaxSpeed, 1, "+")).grid(row=2, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(personMaxSpeed, 1, "-")).grid(row=3, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(fireSpreadingFrequency, 1, "+")).grid(row=4, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(fireSpreadingFrequency, 1, "-")).grid(row=5, column=5, sticky='nesw')


        tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0', height=2,
                        command=lambda: SimulationDriver.start_torch_and_show_next_page(controller, "torch", self.shape, spawnChance.get(), personSpawnChance.get(), fireSpawnChance.get(), 
                        exitSpawnChance.get(), personMaxSpeed.get(), fireSpreadingFrequency.get())).grid(row=6, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0', 
                        command=lambda: controller.show_frame("ShapePage")).grid(row=7, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0', 
                        command=lambda: controller.show_frame("StartPage")).grid(row=8, column=0, columnspan=6, sticky='nesw')

    def update_value(self, value_to_update, value, direction):
        if (direction == "+"):
            new_value = round(value_to_update.get() + value, 1)
            if (new_value < 5):
                value_to_update.set(new_value)
        if (direction == "-"):
            new_value = round(value_to_update.get() - value, 1)
            if (new_value > 0):
                value_to_update.set(new_value)
        return

    def set_shape(self, shape):
        self.shape = shape