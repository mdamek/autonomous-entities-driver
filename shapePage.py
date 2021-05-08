from colors import Colors
import tkinter as tk


class ShapePage(tk.Frame):
    def __init__(self, parent, controller, config):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        shape_config = config["shapes"]
        for shape in shape_config:
            shape_name = shape["name"]
            tk.Button(self, text=shape_name.capitalize(),
                      command=lambda shape_name=shape_name: self.go_to_parameters_page(shape_name)).pack(fill=tk.BOTH, expand=True)

        tk.Button(self, text="Cancel", bg=Colors.Red,
                  command=lambda: self.controller.frames["StartPage"].tkraise()).pack(fill=tk.BOTH, expand=True)

    def set_simulation(self, simulation):
        self.simulation = simulation

    def go_to_parameters_page(self, shape):
        self.simulation.set_shape(shape)
        self.controller.frames["ParametersPage"].generate_page(self.simulation)
        self.controller.frames["ParametersPage"].tkraise()
