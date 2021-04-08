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
        for F in (StartPage, ShapePage, InProgressPage, MockPage, OptionsPage, RabbitsPage, FortwistPage):
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
        button4 = tk.Button(self, text="TODO",
                            command=lambda: controller.show_frame("ShapePage"))
        button5 = tk.Button(self, text="Service", bg='#FFFEB0', activebackground='#FFFEB0',
                            command=lambda: controller.show_frame("OptionsPage"))
        
        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)
        button5.pack(fill = tk.BOTH, expand = True)

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
        print("SDASDASDAS", simulation_name)
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

        label = tk.Label(self, textvariable=self.simulation_text, font=("Courier", 10))
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

        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_simulation_and_show_next_page(controller, "rabbit", self.shape))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

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
        
class SimulationDriver:
    @staticmethod
    def start_simulation_and_show_next_page(controller, simulation_name, shape):
        controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_simulation(simulation_name, shape)
    @staticmethod
    def kill_simulation_and_back_to_start(controller):
        controller.show_frame("StartPage")
        sr.kill_simulation()
        

if __name__ == "__main__":
    #sr.run_led_servers()
    app = App()
    app.attributes('-fullscreen', True)
    app.mainloop()