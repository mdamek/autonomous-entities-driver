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
        rabbitLifeActivityCost .set(0.1)
        rabbitReproductionThreshold.set(1)
        lettuceEnergeticCapacity.set(0.6)
        lettuceReproductionFrequency.set(2)

        labelNum1 = tk.Label(self, text="spawn chance").grid(row=1, column=0, padx=3) 
        labelNum2 = tk.Label(self, text="rabbit spawn chance").grid(row=2, column=0) 
        labelNum3 = tk.Label(self, text="rabbit start energy").grid(row=3, column=0)  
        labelNum4 = tk.Label(self, text="rabbit reproduction cost").grid(row=4, column=0)
        labelNum5 = tk.Label(self, text="rabbit life activity cost").grid(row=1, column=2)  
        labelNum6 = tk.Label(self, text="rabbit reproduction threshold").grid(row=2, column=2)
        labelNum7 = tk.Label(self, text="lettuce energetic capacity").grid(row=3, column=2)  
        labelNum8 = tk.Label(self, text="lettuce reproduction frequency").grid(row=4, column=2, padx=3) 

        entryNum1 = tk.Entry(self, textvariable=spawnChance).grid(row=1, column=1)  
        entryNum2 = tk.Entry(self, textvariable=rabbitSpawnChance).grid(row=2, column=1) 
        entryNum3 = tk.Entry(self, textvariable=rabbitStartEnergy).grid(row=3, column=1)  
        entryNum4 = tk.Entry(self, textvariable=rabbitReproductionCost).grid(row=4, column=1)  
        entryNum5 = tk.Entry(self, textvariable=rabbitLifeActivityCost).grid(row=1, column=3)  
        entryNum6 = tk.Entry(self, textvariable=rabbitReproductionThreshold).grid(row=2, column=3)  
        entryNum7 = tk.Entry(self, textvariable=lettuceEnergeticCapacity).grid(row=3, column=3)  
        entryNum8 = tk.Entry(self, textvariable=lettuceReproductionFrequency).grid(row=4, column=3)    

        button1 = tk.Button(self, text="Start", height=6, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "rabbits", self.shape)).grid(row=5, column=0, columnspan=4, sticky='nesw')
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage")).grid(row=6, column=0, columnspan=4, sticky='nesw')
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage")).grid(row=7, column=0, columnspan=4, sticky='nesw')

        #button1.pack(side="bottom", fill="x")
        #button2.pack(side="bottom", fill="x")
        #button3.pack(side="bottom", fill="x")

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
    #app.geometry("800x480")
    app.attributes('-fullscreen', True)
    app.mainloop()