from colors import Colors
from shapePage import ShapePage
from optionsPage import OptionsPage
from parametersPage import ParametersPage
from Simulation import Simulation
from checkRaspberriesConnectionPage import CkeckRaspberriesConnectionPage
from inProgressSteppedPage import InProgressSteppedPage
from drawPage import DrawPage
from inProgressPage import InProgressPage
import json
import tkinter as tk
import scripts_runner as sr


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

        in_progress_frame = InProgressPage(
            parent=container, controller=self, config=config["continiousSimulation"])
        self.frames[InProgressPage.__name__] = in_progress_frame
        in_progress_frame.grid(row=0, column=0, sticky="nsew")

        raspberries_frame = CkeckRaspberriesConnectionPage(
            parent=container, controller=self, hosts=config["config"]["hosts"])
        self.frames[CkeckRaspberriesConnectionPage.__name__] = raspberries_frame
        raspberries_frame.grid(row=0, column=0, sticky="nsew")

        draw_frame = DrawPage(
            parent=container, controller=self, hosts=config["config"]["hosts"])
        self.frames[DrawPage.__name__] = draw_frame
        draw_frame.grid(row=0, column=0, sticky="nsew")

        for page in (InProgressSteppedPage, OptionsPage, ParametersPage):
            page_name = page.__name__
            frame = page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.frames["StartPage"].tkraise()

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

        options_button = tk.Button(self, text="Service", bg=Colors.Yellow,
                                   activebackground=Colors.Yellow, command=lambda: self.controller.frames["OptionsPage"].tkraise())
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
    sr.restart_led_servers()
    app = App()
    app.geometry("480x320")
    app.attributes('-fullscreen', True)
    app.mainloop()
