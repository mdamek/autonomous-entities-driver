from helpers import SimulationDriver
import platform
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        lifeSpawnChance = tk.DoubleVar()

        lifeSpawnChance.set(0.1)

        for number in range(0,5):
            self.grid_rowconfigure(number, weight = 1)

        for number in range(0,5):
            self.grid_columnconfigure(number, weight = 1)

        tk.Label(self, text="Random", font='Helvetica 16 bold', bg='#3399ff', borderwidth=1, relief="solid").grid(row=0, column=0, columnspan=3, sticky='nesw')
        tk.Message(self, text="Spawn chance").grid(row=1, column=0, rowspan=2, sticky='nesw')
        tk.Message(self, textvariable=lifeSpawnChance, borderwidth=2, relief="sunken").grid(row=1, column=1, rowspan=2, sticky='nesw')
        tk.Button(self, text="+", command=lambda: self.update_value(lifeSpawnChance, 0.1, "+")).grid(row=1, column=2, sticky='nesw')
        tk.Button(self, text="-", command=lambda: self.update_value(lifeSpawnChance, 0.1, "-")).grid(row=2, column=2, sticky='nesw')
        tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_game_and_show_next_page(controller, "game", self.shape, lifeSpawnChance.get(), False)).grid(row=3, column=0, columnspan=3, sticky='nesw')

        tk.Label(self, text="Finger", font='Helvetica 16 bold', bg='#3399ff', borderwidth=1, relief="solid").grid(row=0, column=3, columnspan=6, sticky='nesw')
        tk.Message(self, text="You can select initial position by your finger. Just click 'Draw' and draw selected initial position on panels!", font='Helvetica 9 bold').grid(row=1, column=3, columnspan=6,rowspan=2, sticky='nesw')
        tk.Button(self, text="Draw", bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_game_and_show_draw_page(controller, "game", self.shape)).grid(row=3, column=3, columnspan=6, sticky='nesw')

        tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage")).grid(row=4, column=0, columnspan=6, sticky='nesw')
        tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage")).grid(row=5, column=0, columnspan=6, sticky='nesw')

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