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


        tk.Label(self, text="Fora spawn chance", font='Helvetica 9 bold').grid(row=0, column=0, rowspan=2, sticky='nesw')
        tk.Label(self, text="Fora start energy", font='Helvetica 9 bold').grid(row=2, column=0, rowspan=2, sticky='nesw') 
        tk.Label(self, text="Fora reproduction cost", font='Helvetica 9 bold').grid(row=4, column=0, rowspan=2, sticky='nesw')  
        tk.Label(self, text="Fora reproduction threshold", font='Helvetica 9 bold').grid(row=6, column=0, rowspan=2, sticky='nesw')

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

        tk.Label(self, text="Fora life activity cost", font='Helvetica 9 bold').grid(row=0, column=3, rowspan=2, sticky='nesw')  
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
        tk.Button(self, text="+", command=lambda: self.update_value(algaeRegenerationRate, 0.1, "+")).grid(row=4, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeRegenerationRate, 0.1, "-")).grid(row=5, column=5, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(algaeEnergeticCapacity, 1, "+")).grid(row=6, column=5, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(algaeEnergeticCapacity, 1, "-")).grid(row=7, column=5, sticky='nesw')

        tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0', height=2,
                        command=lambda: SimulationDriver.start_fortwist_and_show_next_page(controller, "fortwist", self.shape, foraminiferaSpawnChance.get(), foraminiferaStartEnergy.get(), foraminiferaReproductionCost.get(), 
                        foraminiferaReproductionThreshold.get(), foraminiferaLifeActivityCost.get(), algaeStartEnergy.get(), algaeRegenerationRate.get(), algaeEnergeticCapacity.get())).grid(row=8, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0', 
                        command=lambda: controller.show_frame("ShapePage")).grid(row=9, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0', 
                        command=lambda: controller.show_frame("StartPage")).grid(row=10, column=0, columnspan=6, sticky='nesw')

    def set_shape(self, shape):
        self.shape = shape