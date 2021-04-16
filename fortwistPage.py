from helpers import SimulationDriver
import platform
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

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

        for number in range(0, 10):
            self.grid_rowconfigure(number, weight = 1, minsize=4)

        for number in range(0,6):
            self.grid_columnconfigure(number, weight = 1, minsize=4)


        tk.Label(self, text="Foraminifera spawn chance", font='Helvetica 9 bold').grid(row=0, column=0, rowspan=2, sticky='nesw')
        tk.Label(self, text="Foraminifera start energy", font='Helvetica 9 bold').grid(row=2, column=0, rowspan=2, sticky='nesw') 
        tk.Label(self, text="Foraminifera reproduction cost", font='Helvetica 9 bold').grid(row=4, column=0, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Foraminifera reproduction threshold", font='Helvetica 9 bold').grid(row=6, column=0, rowspan=2, sticky='nesw')

        tk.Label(self, textvariable=foraminiferaSpawnChance, borderwidth=2, relief="sunken").grid(row=0, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=foraminiferaStartEnergy, borderwidth=2, relief="sunken").grid(row=2, column=1, rowspan=2, sticky='nesw') 
        tk.Label(self, textvariable=foraminiferaReproductionCost, borderwidth=2, relief="sunken").grid(row=4, column=1, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=foraminiferaReproductionThreshold, borderwidth=2, relief="sunken").grid(row=6, column=1, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaSpawnChance, 0.1, "+")).grid(row=0, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaSpawnChance, 0.1, "-")).grid(row=1, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaStartEnergy, 0.1, "+")).grid(row=2, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaStartEnergy, 0.1, "-")).grid(row=3, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaReproductionCost, 0.1, "+")).grid(row=4, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaReproductionCost, 0.1, "-")).grid(row=5, column=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaReproductionThreshold, 0.1, "+")).grid(row=6, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaReproductionThreshold, 0.1, "-")).grid(row=7, column=2, sticky='nesw')

        tk.Label(self, text="Foraminifera life activity cost", font='Helvetica 9 bold').grid(row=0, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Algae start energy", font='Helvetica 9 bold').grid(row=2, column=3, rowspan=2, sticky='nesw')
        tk.Label(self, text="Algae regeneration rate", font='Helvetica 9 bold').grid(row=4, column=3, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Algae energetic capacity", font='Helvetica 9 bold').grid(row=6, column=3, rowspan=2, sticky='nesw')
          
        tk.Label(self, textvariable=foraminiferaLifeActivityCost, borderwidth=2, relief="sunken").grid(row=0, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=algaeStartEnergy, borderwidth=2, relief="sunken").grid(row=2, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=algaeRegenerationRate, borderwidth=2, relief="sunken").grid(row=4, column=4, rowspan=2, sticky='nesw')  
        tk.Label(self, textvariable=algaeEnergeticCapacity, borderwidth=2, relief="sunken").grid(row=6, column=4, rowspan=2, sticky='nesw')

        tk.Button(self, text="+", command=lambda: self.update_value(foraminiferaLifeActivityCost, 0.1, "+")).grid(row=0, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(foraminiferaLifeActivityCost, 0.1, "-")).grid(row=1, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeStartEnergy, 0.1, "+")).grid(row=2, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeStartEnergy, 0.1, "-")).grid(row=3, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeRegenerationRate, 0.01, "+")).grid(row=4, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeRegenerationRate, 0.01, "-")).grid(row=5, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeEnergeticCapacity, 1, "+")).grid(row=6, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeEnergeticCapacity, 1, "-")).grid(row=7, column=5, sticky='nesw')

        tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0', height=2,
                        command=lambda: SimulationDriver.start_fortwist_and_show_next_page(controller, "fortwist", self.shape, foraminiferaSpawnChance.get(), foraminiferaStartEnergy.get(), foraminiferaReproductionCost.get(), 
                        foraminiferaReproductionThreshold.get(), foraminiferaLifeActivityCost.get(), algaeStartEnergy.get(), algaeRegenerationRate.get(), algaeEnergeticCapacity.get())).grid(row=8, column=0, columnspan=6, sticky='nesw')
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