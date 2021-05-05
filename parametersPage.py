import scripts_runner as sr
import platform
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import BooleanVar, Radiobutton
else:
    import Tkinter as tk
    from Tkinter import BooleanVar, Radiobutton


class ParametersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def extract_values_for_parameter(self, parameter):
        name = parameter["name"]
        text = parameter["text"]
        if "initialValue" in parameter:
            initial_value = parameter["initialValue"]
        else:
            initial_value = self.simulation.config["defaultInitialValue"]
        if "changeOnClick" in parameter:
            change_on_click = parameter["changeOnClick"]
        else:
            change_on_click = self.simulation.config["defaultChangeValue"]
        return name, text, initial_value, float(change_on_click)

    def update_value(self, value_to_update, value, direction):
        actual_value = self.parameters_collection[value_to_update].get()
        if (direction == "+"):
            new_value = round(actual_value + value, 1)
            if (new_value < self.simulation.config["maxValue"]):
                self.parameters_collection[value_to_update].set(new_value)
        if (direction == "-"):
            new_value = round(actual_value - value, 1)
            if (new_value > self.simulation.config["minValue"]):
                self.parameters_collection[value_to_update].set(new_value)
        return

    def generate_page(self, simulation):
        print(simulation.shape)
        self.simulation = simulation
        self.parameters_collection = {}
        parameters = simulation.config["parameters"]

        number_of_parameters = len(parameters)

        number_of_addition_buttons = 5

        for number in range(0, number_of_parameters + number_of_addition_buttons):
            self.grid_rowconfigure(number, weight=1)

        for number in range(0, 6):
            self.grid_columnconfigure(number, weight=1, minsize=4)

        self.steppedSimulation = BooleanVar()
        self.steppedSimulation.set(False)

        self.drawInitialPosition = BooleanVar()
        self.drawInitialPosition.set(False)

        tk.Label(self, text=self.simulation.config["name"].capitalize(
        ) + " simulation", font='Helvetica 14 bold').grid(row=0, column=0, columnspan=6, sticky='nesw')
        Radiobutton(self, text="Classical simulation", variable=self.steppedSimulation,
                    value=False).grid(row=1, column=0, columnspan=3, sticky='nesw')
        Radiobutton(self, text="Stepped simulation", variable=self.steppedSimulation,
                    value=True).grid(row=1, column=3, columnspan=6, sticky='nesw')
        Radiobutton(self, text="Random initial position", variable=self.drawInitialPosition,
                    value=False).grid(row=2, column=0, columnspan=3, sticky='nesw')
        Radiobutton(self, text="Draw initial position", variable=self.drawInitialPosition,
                    value=True).grid(row=2, column=3, columnspan=6, sticky='nesw')

        for index, parameter in enumerate(parameters):
            name, text, initial_value, change_on_click = self.extract_values_for_parameter(
                parameter)
            self.parameters_collection[name] = tk.DoubleVar()
            self.parameters_collection[name].set(initial_value)

            if index % 2 == 0:
                on_left = True
            else:
                on_left = False

            tk.Label(self, text=text, font='Helvetica 9 bold').grid(
                row=index + 3 if on_left else index + 2, column=0 if on_left else 3, rowspan=2, sticky='nesw')
            tk.Label(self, textvariable=self.parameters_collection[name], borderwidth=2, relief="sunken").grid(
                row=index + 3 if on_left else index + 2, column=1 if on_left else 4, rowspan=2, sticky='nesw')
            tk.Button(self, text="+", command=lambda name=name, change_on_click=change_on_click: self.update_value(name,
                      change_on_click, "+")).grid(row=index + 3 if on_left else index + 2, column=2 if on_left else 5, sticky='nesw')
            tk.Button(self, text="-", command=lambda name=name, change_on_click=change_on_click: self.update_value(name,
                      change_on_click, "-")).grid(row=index + 4 if on_left else index + 3, column=2 if on_left else 5, sticky='nesw')

        tk.Button(self, text="Start", bg='#B2FFB0',
                  activebackground='#B2FFB0', command=lambda: print("SD")).grid(row=number_of_parameters + 3, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0', command=lambda: self.controller.show_frame(
            "ShapePage")).grid(row=number_of_parameters + 4, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0',
                  command=lambda:  self.controller.show_frame("StartPage")).grid(row=number_of_parameters + 5, column=0, columnspan=6, sticky='nesw')
