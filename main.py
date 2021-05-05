from shapePage import ShapePage
from optionsPage import OptionsPage
from parametersPage import ParametersPage
from Simulation import Simulation
from checkRaspberriesConnectionPage import CkeckRaspberriesConnectionPage
from gamePage import GamePage
from inProgressSteppedPage import InProgressSteppedPage
from drawPage import DrawPage
from inProgressPage import InProgressPage
from torchPage import TorchPage
from fortwistPage import FortwistPage
from mockPage import MockPage
from rabbitsPage import RabbitsPage

import json
import threading
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

        with open('simulations.json') as json_file:
            config = json.load(json_file)

        self.frames = {}

        start_frame = StartPage(
            parent=container, controller=self, config=config)
        self.frames[StartPage.__name__] = start_frame
        start_frame.grid(row=0, column=0, sticky="nsew")

        shape_frame = ShapePage(
            parent=container, controller=self, config=config)
        self.frames[ShapePage.__name__] = shape_frame
        shape_frame.grid(row=0, column=0, sticky="nsew")

        for page in (InProgressPage, InProgressSteppedPage, OptionsPage, DrawPage, CkeckRaspberriesConnectionPage, ParametersPage):
            page_name = page.__name__
            frame = page(parent=container, controller=self)
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
    def __init__(self, parent, controller, config):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config = config

        for simulation in config['simulations']:
            simulation_name = simulation['name']

            button = tk.Button(self, text=simulation_name.capitalize(), command=lambda simulation_name=simulation_name: self.go_to_shape_page(
                self.get_valid_config(simulation_name)))
            button.pack(fill=tk.BOTH, expand=True)

        options_button = tk.Button(self, text="Service", bg='#FFFEB0',
                                   activebackground='#FFFEB0', command=lambda: controller.show_frame("OptionsPage"))
        options_button.pack(fill=tk.BOTH, expand=True)

    def get_valid_config(self, config_name):
        simulations = self.config['simulations']
        selected_config = next(
            filter(lambda simulation: simulation["name"] == config_name, simulations))
        return selected_config

    def go_to_shape_page(self, simulation_config):
        simulation = Simulation(simulation_config)
        self.controller.frames["ShapePage"].set_simulation(simulation)
        self.controller.frames["ShapePage"].tkraise()


if __name__ == "__main__":
    # sr.run_led_servers()
    app = App()
    if (platform.node() == "DESKTOP-TREPOQV"):
        app.geometry("480x320")
    else:
        app.attributes('-fullscreen', True)
    app.mainloop()
