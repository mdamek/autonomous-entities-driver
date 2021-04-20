from gamePage import GamePage
from torchPage import TorchPage
from fortwistPage import FortwistPage
from mockPage import MockPage
from rabbitsPage import RabbitsPage
from helpers import SimulationDriver
import scripts_runner as sr 
import platform
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk  
         
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ShapePage, InProgressPage, MockPage, OptionsPage, RabbitsPage, FortwistPage, TorchPage, GamePage, DrawPage):
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

    def set_simulation_name_shape_stepped_and_show_frame(self, page_name, simulation_name, shape, stepped):
        self.frames[page_name].set_shape(shape)
        self.frames[page_name].set_simulation_name(simulation_name)
        self.frames[page_name].set_stepped(stepped)
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
        button5 = tk.Button(self, text="Game of life",
                            command=lambda: controller.set_simulation_name_and_show_frame("ShapePage", "game"))
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
        if simulation_name == "game":
            return "GamePage"
        return ""

class DrawPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        self.simulation_name = ""
        self.stepped = False
        
        label = tk.Label(self, text="Draw starting position on panels then click Start", font='Helvetica 14 bold')

        button2 = tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: controller.show_frame("GamePage"))
        button3 = tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0', command=lambda: DrawPage.start_game_and_show_next_page(controller, self.simulation_name, self.shape, 0, True, self.stepped))

        label.pack(side="top", fill="x")
        button1.pack(side="bottom", fill = tk.BOTH, expand = True)
        button2.pack(side="bottom", fill = tk.BOTH, expand = True)
        button3.pack(side="bottom", fill = tk.BOTH, expand = True)

    def set_shape(self, shape):
        self.shape = shape

    def set_simulation_name(self, simulation_name):
        self.simulation_name = simulation_name

    def set_stepped(self, stepped):
        self.stepped = stepped

    @staticmethod
    def start_game_and_show_next_page(controller, simulation_name, shape, lifeSpawnChance, loadFromOutside, stepped):
        print(stepped)
        if stepped == True:
            pass
        else:
            controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_game(shape, lifeSpawnChance, loadFromOutside)

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

class InProgressSteppedPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        self.simulation_text = tk.StringVar()

class SelectStartTypePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        self.simulation_name = ""

        label = tk.Label(self, text="Draw starting position on panels then click Start", font='Helvetica 14 bold')

        button1 = tk.Button(self, text="Stepped simulation", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: SimulationDriver.kill_simulation_and_back_to_start(controller))
        button2 = tk.Button(self, text="Classical simulation", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: SimulationDriver.kill_simulation_and_back_to_start(controller))
        button3 = tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: controller.show_frame("GamePage"))
        button4 = tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: controller.show_frame("StartPage"))

        label.pack(side="top", fill="x")
        button1.pack(side="bottom", fill = tk.BOTH, expand = True)
        button2.pack(side="bottom", fill = tk.BOTH, expand = True)
        button3.pack(side="bottom", fill = tk.BOTH, expand = True)
        button4.pack(side="bottom", fill = tk.BOTH, expand = True)


    def get_valid_simulation_details_page(self, simulation_name):
        if simulation_name == "mock":
            return "MockPage"
        if simulation_name == "rabbits":
            return "RabbitsPage"
        if simulation_name == "fortwist":
            return "FortwistPage"
        if simulation_name == "torch":
            return "TorchPage"
        if simulation_name == "game":
            return "GamePage"
        return ""

    def set_shape(self, shape):
        self.shape = shape
    
    def set_simulation_name(self, simulation_name):
        self.simulation_name = simulation_name

if __name__ == "__main__":
    #sr.run_led_servers()
    app = App()
    if (platform.node() == "DESKTOP-TREPOQV"):
        app.geometry("480x320")
    else:
        app.attributes('-fullscreen', True)
        print("geo")
    app.mainloop()