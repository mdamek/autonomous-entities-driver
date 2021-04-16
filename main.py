from helpers import Helpers
import Tkinter as tk      
import scripts_runner as sr          
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ShapePage, InProgressPage, MockPage, OptionsPage, RabbitsPage, FortwistPage, TorchPage, UrbanPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def set_shape_and_show_frame(self, page_name, shape):
        self.frames[page_name].set_shape(shape)
        self.frames[page_name].tkraise()

    def set_simulation_name_and_show_frame(self, page_name, simulation_name):
        self.frames[page_name].set_simulation_name(simulation_name)
        self.frames[page_name].tkraise()

    def set_simulation_name_shape_and_show_frame(self, page_name, simulation_name, shape):
        self.frames[page_name].set_shape(shape)
        self.frames[page_name].set_simulation_name(simulation_name)
        self.frames[page_name].tkraise()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Mock", 
                            command=lambda: controller.set_simulation_name_and_show_frame("ShapePage", "mock"))
        button2 = tk.Button(self, text="Rabbits", 
                            command=lambda: controller.set_simulation_name_and_show_frame("ShapePage", "rabbits"))
        button3 = tk.Button(self, text="Fortwist", 
                            command=lambda: controller.set_simulation_name_and_show_frame("ShapePage", "fortwist"))
        button4 = tk.Button(self, text="Torch",
                            command=lambda: controller.set_simulation_name_and_show_frame("ShapePage", "torch"))
        button5 = tk.Button(self, text="Urban",
                            command=lambda: controller.set_simulation_name_and_show_frame("ShapePage", "urban"))
        button6 = tk.Button(self, text="Service", bg='#FFFEB0', activebackground='#FFFEB0',
                            command=lambda: controller.show_frame("OptionsPage"))
        
        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)
        button5.pack(fill = tk.BOTH, expand = True)
        button6.pack(fill = tk.BOTH, expand = True)

class OptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Restart LED servers", bg='#FFFEB0', activebackground='#FFFEB0', 
                            command=lambda: sr.restart_led_servers())
        button2 = tk.Button(self, text="Stop Xinuk", bg='#FFFEB0', activebackground='#FFFEB0',
                            command=lambda: sr.kill_xinuk())
        button3 = tk.Button(self, text="Restart all devices", bg='#FFBEB0', activebackground='#FFBEB0',
                            command=lambda: sr.restart_all_devices())
        button4 = tk.Button(self, text="Turn off platform", bg='#E83838', activebackground='#E83838',
                            command=lambda: sr.turn_off_the_platform())                        
        button5 = tk.Button(self, text="Return", 
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)
        button5.pack(fill = tk.BOTH, expand = True)   

class ShapePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.simulation_name = ""

        button1 = tk.Button(self, text="Square",
                           command=lambda: controller.set_shape_and_show_frame(self.get_valid_details_page(self.simulation_name), "square"))
        button2 = tk.Button(self, text="Vertical",
                           command=lambda: controller.set_shape_and_show_frame(self.get_valid_details_page(self.simulation_name), "vertical"))
        button3 = tk.Button(self, text="Horizontal",
                           command=lambda: controller.set_shape_and_show_frame(self.get_valid_details_page(self.simulation_name), "horizontal"))                   
        button4 = tk.Button(self, text="Cancel", bg='#FFBEB0',
                           command=lambda: controller.show_frame("StartPage"))

        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)

    def set_simulation_name(self, simulation_name):
        self.simulation_name = simulation_name

    def get_valid_details_page(self, simulation_name):
        if simulation_name == "mock":
            return "MockPage"
        if simulation_name == "rabbits":
            return "RabbitsPage"
        if simulation_name == "fortwist":
            return "FortwistPage"
        if simulation_name == "torch":
            return "TorchPage"
        if simulation_name == "urban":
            return "UrbanPage"
        return ""

class InProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        self.simulation_text = tk.StringVar()

        label = tk.Label(self, textvariable=self.simulation_text, font=("Courier", 13))
        button1 = tk.Button(self, text="Stop", bg='#FFBEB0', activebackground='#FFBEB0',
                           command=lambda: SimulationDriver.kill_simulation_and_back_to_start(controller), font=("Courier", 40))

        label.pack(side="top", fill="x")
        button1.pack(side="bottom", fill = tk.BOTH, expand = True)

    def set_shape(self, shape):
        self.shape = shape

    def set_simulation_name(self, simulation_name):
        text = simulation_name + " " + self.shape + " simulation in progress..." 
        self.simulation_text.set(text.capitalize())

class MockPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "mock", self.shape))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

    def set_shape(self, shape):
        self.shape = shape

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

class FortwistPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "fortwist", self.shape))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

    def set_shape(self, shape):
        self.shape = shape

class TorchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "torch", self.shape))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

    def set_shape(self, shape):
        self.shape = shape

class UrbanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "urban", self.shape))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

    def set_shape(self, shape):
        self.shape = shape
        
class SimulationDriver:
    @staticmethod
    def start_simulation_and_show_next_page(controller, simulation_name, shape):
        print(simulation_name, shape)
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_simulation(simulation_name, shape)
    @staticmethod
    def kill_simulation_and_back_to_start(controller):
        controller.show_frame("StartPage")
        sr.kill_simulation()
        

if __name__ == "__main__":
    #sr.run_led_servers()
    app = App()
    #app.geometry("480x320")
    app.attributes('-fullscreen', True)
    app.mainloop()