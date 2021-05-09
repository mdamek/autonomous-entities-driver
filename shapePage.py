from colors import Colors
import tkinter as tk


class ShapePage(tk.Frame):
    def __init__(self, parent, controller, config):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape_config = config["shapes"]
        for shape in self.shape_config:
            shape_name = shape["name"]
            tk.Button(self, text=shape_name.capitalize(),
                      command=lambda shape_name=shape_name: self.go_to_parameters_page(shape_name)).pack(fill=tk.BOTH, expand=True)

        tk.Button(self, text="Cancel", bg=Colors.Red,
                  command=lambda: self.controller.frames["StartPage"].tkraise()).pack(fill=tk.BOTH, expand=True)

    def set_simulation(self, simulation):
        self.simulation = simulation

    def go_to_parameters_page(self, shape):
        selected_shape_config = next(
            filter(lambda shape_config: shape_config["name"] == shape, self.shape_config))
        self.simulation.set_shape_data(selected_shape_config["width_workers"], selected_shape_config["height_workers"],
                                       selected_shape_config["width"], selected_shape_config["height"], selected_shape_config["name"])
        self.controller.frames["ParametersPage"].generate_page(self.simulation)
        self.controller.frames["ParametersPage"].tkraise()
