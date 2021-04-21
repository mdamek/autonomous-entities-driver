from checkRaspberriesConnectionPage import CkeckRaspberriesConnectionPage
from gamePage import GamePage
from inProgressSteppedPage import InProgressSteppedPage
from drawPage import DrawPage
from inProgressPage import InProgressPage
from torchPage import TorchPage
from fortwistPage import FortwistPage
from mockPage import MockPage
from rabbitsPage import RabbitsPage

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
        for F in (StartPage, ShapePage, InProgressPage, InProgressSteppedPage, MockPage, OptionsPage, RabbitsPage, FortwistPage, TorchPage, GamePage, DrawPage, CkeckRaspberriesConnectionPage):
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
        button2 = tk.Button(self, text="Check Raspberries avaliability", bg='#FFFEB0', activebackground='#FFFEB0', 
                            command=lambda: self.open_avaliability_check(controller))
        button3 = tk.Button(self, text="Stop Xinuk", bg='#FFFEB0', activebackground='#FFFEB0',
                            command=lambda: sr.kill_xinuk())
        button4 = tk.Button(self, text="Restart all devices", bg='#FFBEB0', activebackground='#FFBEB0',
                            command=lambda: sr.restart_all_devices())
        button5 = tk.Button(self, text="Turn off platform", bg='#FFBEB0', activebackground='#FFBEB0',
                            command=lambda: sr.turn_off_the_platform())                        
        button6 = tk.Button(self, text="Return", 
                            command=lambda: controller.show_frame("StartPage"))

        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)
        button5.pack(fill = tk.BOTH, expand = True)
        button6.pack(fill = tk.BOTH, expand = True)

    def open_avaliability_check(self, controller):
        controller.frames["CkeckRaspberriesConnectionPage"].clean_statuses()
        controller.show_frame("CkeckRaspberriesConnectionPage")


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

if __name__ == "__main__":
    #sr.run_led_servers()
    app = App()
    if (platform.node() == "DESKTOP-TREPOQV"):
        app.geometry("480x320")
    else:
        app.attributes('-fullscreen', True)
        print("geo")
    app.mainloop()