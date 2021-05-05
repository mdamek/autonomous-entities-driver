from colors import Colors
import platform
import scripts_runner as sr
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import BooleanVar, Radiobutton
else:
    import Tkinter as tk
    from Tkinter import BooleanVar, Radiobutton

class RabbitsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        spawnChance = tk.DoubleVar()  
        rabbitSpawnChance = tk.DoubleVar()  
        rabbitStartEnergy = tk.DoubleVar()  
        rabbitReproductionCost = tk.DoubleVar()  
        rabbitLifeActivityCost = tk.DoubleVar()  
        rabbitReproductionThreshold = tk.DoubleVar()  
        lettuceEnergeticCapacity = tk.DoubleVar()  
        lettuceReproductionFrequency = tk.DoubleVar()  

        spawnChance.set(0.1)
        rabbitSpawnChance.set(0.3)
        rabbitStartEnergy.set(0.5)
        rabbitReproductionCost.set(0.5)
        rabbitLifeActivityCost.set(0.1)
        rabbitReproductionThreshold.set(1)
        lettuceEnergeticCapacity.set(0.6)
        lettuceReproductionFrequency.set(2)

        for number in range(0, 11):
            self.grid_rowconfigure(number, weight = 1, minsize=4)

        for number in range(0,6):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        self.steppedSimulation = BooleanVar()
        self.steppedSimulation.set(False)

        Radiobutton(self, text="Classical simulation", variable=self.steppedSimulation, value=False).grid(row=0, column=0, columnspan=3, sticky='nesw')
        Radiobutton(self, text="Stepped simulation", variable=self.steppedSimulation, value=True).grid(row=0, column=3, columnspan=6, sticky='nesw')

        tk.Label(self, text="Spawn chance", font='Helvetica 9 bold').grid(row=1, column=0, rowspan=2, sticky='nesw')
        tk.Label(self, text="Rabbit spawn chance", font='Helvetica 9 bold').grid(row=3, column=0, rowspan=2, sticky='nesw') 
        tk.Label(self, text="Rabbit start energy", font='Helvetica 9 bold').grid(row=5, column=0, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Rabbit reproduction cost", font='Helvetica 9 bold').grid(row=7, column=0, rowspan=2, sticky='nesw')

        tk.Label(self, textvariable=spawnChance, borderwidth=2, relief="sunken").grid(row=1, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=rabbitSpawnChance, borderwidth=2, relief="sunken").grid(row=3, column=1, rowspan=2, sticky='nesw') 
        tk.Label(self, textvariable=rabbitStartEnergy, borderwidth=2, relief="sunken").grid(row=5, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=rabbitReproductionCost, borderwidth=2, relief="sunken").grid(row=7, column=1, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(spawnChance, 0.1, "+")).grid(row=1, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(spawnChance, 0.1, "-")).grid(row=2, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitSpawnChance, 0.1, "+")).grid(row=3, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitSpawnChance, 0.1, "-")).grid(row=4, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitStartEnergy, 0.1, "+")).grid(row=5, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitStartEnergy, 0.1, "-")).grid(row=6, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitReproductionCost, 0.1, "+")).grid(row=7, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitReproductionCost, 0.1, "-")).grid(row=8, column=2, sticky='nesw')

        tk.Label(self, text="Rabbit life activity cost", font='Helvetica 9 bold').grid(row=1, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Rabbit reproduction threshold", font='Helvetica 9 bold').grid(row=3, column=3, rowspan=2, sticky='nesw')
        tk.Label(self, text="Lettuce energetic capacity", font='Helvetica 9 bold').grid(row=5, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Lettuce reproduction frequency", font='Helvetica 9 bold').grid(row=7, column=3, rowspan=2, sticky='nesw')
          
        tk.Label(self, textvariable=rabbitLifeActivityCost, borderwidth=2, relief="sunken").grid(row=1, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=rabbitReproductionThreshold, borderwidth=2, relief="sunken").grid(row=3, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=lettuceEnergeticCapacity, borderwidth=2, relief="sunken").grid(row=5, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=lettuceReproductionFrequency, borderwidth=2, relief="sunken").grid(row=7, column=4, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(rabbitLifeActivityCost, 0.1, "+")).grid(row=1, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitLifeActivityCost, 0.1, "-")).grid(row=2, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitReproductionThreshold, 0.1, "+")).grid(row=3, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitReproductionThreshold, 0.1, "-")).grid(row=4, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(lettuceEnergeticCapacity, 0.1, "+")).grid(row=5, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(lettuceEnergeticCapacity, 0.1, "-")).grid(row=6, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(lettuceReproductionFrequency, 1, "+")).grid(row=7, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(lettuceReproductionFrequency, 1, "-")).grid(row=8, column=5, sticky='nesw')

        tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green, height=2,
                        command=lambda: self.start_rabbits_and_show_next_page(controller, "rabbits", self.shape, spawnChance.get(), rabbitSpawnChance.get(), rabbitStartEnergy.get(), 
                        rabbitReproductionCost.get(), rabbitLifeActivityCost.get(), rabbitReproductionThreshold.get(), lettuceEnergeticCapacity.get(), lettuceReproductionFrequency.get(), 
                        self.steppedSimulation.get())).grid(row=9, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Return", bg=Colors.Red, activebackground=Colors.Red, 
                        command=lambda: controller.show_frame("ShapePage")).grid(row=10, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Cancel", bg=Colors.Red, activebackground=Colors.Red, 
                        command=lambda: controller.show_frame("StartPage")).grid(row=11, column=0, columnspan=6, sticky='nesw')

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

    def start_rabbits_and_show_next_page(self, controller, simulation_name, shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, 
    rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency, stepped):
        if stepped == True:
            controller.set_simulation_name_shape_and_show_frame("InProgressSteppedPage", simulation_name, shape)
        else:
            controller.frames["InProgressPage"].set_shape(shape)
            controller.frames["InProgressPage"].set_simulation_name(simulation_name)
            controller.frames["InProgressPage"].reset_speed()
            controller.frames["InProgressPage"].tkraise()
        sr.run_rabbits(shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency, stepped)