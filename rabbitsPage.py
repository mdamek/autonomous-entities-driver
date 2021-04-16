from helpers import SimulationDriver
import tkinter as tk  

class RabbitsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        spawnChance = tk.DoubleVar()  
        rabbitSpawnChance = tk.DoubleVar()  
        rabbitInitialSignal = tk.DoubleVar()  
        lettuceInitialSignal = tk.DoubleVar()  
        rabbitStartEnergy = tk.DoubleVar()  
        rabbitReproductionCost = tk.DoubleVar()  
        rabbitLifeActivityCost = tk.DoubleVar()  
        rabbitReproductionThreshold = tk.DoubleVar()  
        lettuceEnergeticCapacity = tk.DoubleVar()  
        lettuceReproductionFrequency = tk.DoubleVar()  

        spawnChance.set(0.1)
        rabbitSpawnChance.set(0.3)
        rabbitInitialSignal.set(-1)
        lettuceInitialSignal.set(1)
        rabbitStartEnergy.set(0.5)
        rabbitReproductionCost.set(0.5)
        rabbitLifeActivityCost.set(0.1)
        rabbitReproductionThreshold.set(1)
        lettuceEnergeticCapacity.set(0.6)
        lettuceReproductionFrequency.set(2)

        for number in range(0, 10):
            self.grid_rowconfigure(number, weight = 1, minsize=4)

        for number in range(0,6):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        tk.Label(self, text="Spawn chance", font='Helvetica 9 bold').grid(row=0, column=0, rowspan=2, sticky='nesw')
        tk.Label(self, text="Rabbit spawn chance", font='Helvetica 9 bold').grid(row=2, column=0, rowspan=2, sticky='nesw') 
        tk.Label(self, text="Rabbit start energy", font='Helvetica 9 bold').grid(row=4, column=0, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Rabbit reproduction cost", font='Helvetica 9 bold').grid(row=6, column=0, rowspan=2, sticky='nesw')

        tk.Label(self, textvariable=spawnChance, borderwidth=2, relief="sunken").grid(row=0, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=rabbitSpawnChance, borderwidth=2, relief="sunken").grid(row=2, column=1, rowspan=2, sticky='nesw') 
        tk.Label(self, textvariable=rabbitStartEnergy, borderwidth=2, relief="sunken").grid(row=4, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=rabbitReproductionCost, borderwidth=2, relief="sunken").grid(row=6, column=1, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(spawnChance, 0.1, "+")).grid(row=0, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(spawnChance, 0.1, "-")).grid(row=1, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitSpawnChance, 0.1, "+")).grid(row=2, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitSpawnChance, 0.1, "-")).grid(row=3, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitStartEnergy, 0.1, "+")).grid(row=4, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitStartEnergy, 0.1, "-")).grid(row=5, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitReproductionCost, 0.1, "+")).grid(row=6, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitReproductionCost, 0.1, "-")).grid(row=7, column=2, sticky='nesw')

        tk.Label(self, text="Rabbit life activity cost", font='Helvetica 9 bold').grid(row=0, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Rabbit reproduction threshold", font='Helvetica 9 bold').grid(row=2, column=3, rowspan=2, sticky='nesw')
        tk.Label(self, text="Lettuce energetic capacity", font='Helvetica 9 bold').grid(row=4, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Lettuce reproduction frequency", font='Helvetica 9 bold').grid(row=6, column=3, rowspan=2, sticky='nesw')
          
        tk.Label(self, textvariable=rabbitLifeActivityCost, borderwidth=2, relief="sunken").grid(row=0, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=rabbitReproductionThreshold, borderwidth=2, relief="sunken").grid(row=2, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=lettuceEnergeticCapacity, borderwidth=2, relief="sunken").grid(row=4, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=lettuceReproductionFrequency, borderwidth=2, relief="sunken").grid(row=6, column=4, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(rabbitLifeActivityCost, 0.1, "+")).grid(row=0, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitLifeActivityCost, 0.1, "-")).grid(row=1, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(rabbitReproductionThreshold, 0.1, "+")).grid(row=2, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(rabbitReproductionThreshold, 0.1, "-")).grid(row=3, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(lettuceEnergeticCapacity, 0.1, "+")).grid(row=4, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(lettuceEnergeticCapacity, 0.1, "-")).grid(row=5, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(lettuceReproductionFrequency, 1, "+")).grid(row=6, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(lettuceReproductionFrequency, 1, "-")).grid(row=7, column=5, sticky='nesw')

        tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0', height=2,
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "rabbits", self.shape)).grid(row=8, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0', 
                        command=lambda: controller.show_frame("ShapePage")).grid(row=9, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0', 
                        command=lambda: controller.show_frame("StartPage")).grid(row=10, column=0, columnspan=6, sticky='nesw')

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