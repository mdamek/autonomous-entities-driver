from colors import Colors
import scripts_runner as sr
import tkinter as tk
from tkinter import BooleanVar, Radiobutton  


class FortwistPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        foraminiferaSpawnChance = tk.DoubleVar()
        foraminiferaStartEnergy = tk.DoubleVar()
        foraminiferaReproductionCost = tk.DoubleVar()
        foraminiferaReproductionThreshold = tk.DoubleVar()
        foraminiferaLifeActivityCost = tk.DoubleVar()
        algaeStartEnergy = tk.DoubleVar()
        algaeRegenerationRate = tk.DoubleVar()
        algaeEnergeticCapacity = tk.DoubleVar()


        foraminiferaSpawnChance.set(0.3)
        foraminiferaStartEnergy.set(0.3)
        foraminiferaReproductionCost.set(0.5)
        foraminiferaReproductionThreshold.set(0.8)
        foraminiferaLifeActivityCost.set(0.2)
        algaeStartEnergy.set(1)
        algaeRegenerationRate.set(0.07)
        algaeEnergeticCapacity.set(0.1)

        for number in range(0, 11):
            self.grid_rowconfigure(number, weight = 1, minsize=4)

        for number in range(0,6):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        self.steppedSimulation = BooleanVar()
        self.steppedSimulation.set(False)

        Radiobutton(self, text="Classical simulation", variable=self.steppedSimulation, value=False).grid(row=0, column=0, columnspan=3, sticky='nesw')
        Radiobutton(self, text="Stepped simulation", variable=self.steppedSimulation, value=True).grid(row=0, column=3, columnspan=6, sticky='nesw')

        tk.Label(self, text="Foramini spawn chance", font='Helvetica 9 bold').grid(row=1, column=0, rowspan=2, sticky='nesw')
        tk.Label(self, text="Foramini start energy", font='Helvetica 9 bold').grid(row=3, column=0, rowspan=2, sticky='nesw') 
        tk.Label(self, text="Foramini reproduction cost", font='Helvetica 9 bold').grid(row=5, column=0, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Foramini reproduction threshold", font='Helvetica 9 bold').grid(row=7, column=0, rowspan=2, sticky='nesw')

        tk.Label(self, textvariable=foraminiferaSpawnChance, borderwidth=2, relief="sunken").grid(row=1, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=foraminiferaStartEnergy, borderwidth=2, relief="sunken").grid(row=3, column=1, rowspan=2, sticky='nesw') 
        tk.Label(self, textvariable=foraminiferaReproductionCost, borderwidth=2, relief="sunken").grid(row=5, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=foraminiferaReproductionThreshold, borderwidth=2, relief="sunken").grid(row=7, column=1, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaSpawnChance, 0.1, "+")).grid(row=1, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaSpawnChance, 0.1, "-")).grid(row=2, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaStartEnergy, 0.1, "+")).grid(row=3, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaStartEnergy, 0.1, "-")).grid(row=4, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaReproductionCost, 0.1, "+")).grid(row=5, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaReproductionCost, 0.1, "-")).grid(row=6, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaReproductionThreshold, 0.1, "+")).grid(row=7, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaReproductionThreshold, 0.1, "-")).grid(row=8, column=2, sticky='nesw')

        tk.Label(self, text="Foramini life activity cost", font='Helvetica 9 bold').grid(row=1, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Algae start energy", font='Helvetica 9 bold').grid(row=3, column=3, rowspan=2, sticky='nesw')
        tk.Label(self, text="Algae regeneration rate", font='Helvetica 9 bold').grid(row=5, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Algae energetic capacity", font='Helvetica 9 bold').grid(row=7, column=3, rowspan=2, sticky='nesw')
          
        tk.Label(self, textvariable=foraminiferaLifeActivityCost, borderwidth=2, relief="sunken").grid(row=1, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=algaeStartEnergy, borderwidth=2, relief="sunken").grid(row=3, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=algaeRegenerationRate, borderwidth=2, relief="sunken").grid(row=5, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=algaeEnergeticCapacity, borderwidth=2, relief="sunken").grid(row=7, column=4, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaLifeActivityCost, 0.1, "+")).grid(row=1, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaLifeActivityCost, 0.1, "-")).grid(row=2, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeStartEnergy, 0.1, "+")).grid(row=3, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeStartEnergy, 0.1, "-")).grid(row=4, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeRegenerationRate, 0.1, "+")).grid(row=5, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeRegenerationRate, 0.1, "-")).grid(row=6, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeEnergeticCapacity, 1, "+")).grid(row=7, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeEnergeticCapacity, 1, "-")).grid(row=8, column=5, sticky='nesw')

        tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green, height=2,
                        command=lambda: self.start_fortwist_and_show_next_page(controller, "fortwist", self.shape, foraminiferaSpawnChance.get(), foraminiferaStartEnergy.get(), foraminiferaReproductionCost.get(), 
                        foraminiferaReproductionThreshold.get(), foraminiferaLifeActivityCost.get(), algaeStartEnergy.get(), algaeRegenerationRate.get(), 
                        algaeEnergeticCapacity.get(), self.steppedSimulation.get())).grid(row=9, column=0, columnspan=6, sticky='nesw')
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

    def start_fortwist_and_show_next_page(self, controller, simulation_name, shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, 
    foraminiferaLifeActivityCost, algaeStartEnergy, algaeRegenerationRate, algaeEnergeticCapacity, stepped):
        if stepped == True:
            controller.set_simulation_name_shape_and_show_frame("InProgressSteppedPage", simulation_name, shape)
        else:
            controller.frames["InProgressPage"].set_shape(shape)
            controller.frames["InProgressPage"].set_simulation_name(simulation_name)
            controller.frames["InProgressPage"].reset_speed()
            controller.frames["InProgressPage"].tkraise()
        sr.run_fortwist(shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, foraminiferaLifeActivityCost, algaeStartEnergy, 
        algaeRegenerationRate, algaeEnergeticCapacity, stepped)