from colors import Colors
import platform
from requestMaker import stop_motion_sensor
import scripts_runner as sr
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class DrawPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        self.simulation_name = ""
        self.stepped = False
        
        label = tk.Label(self, text="Draw starting position on panels then click Start", font='Helvetica 14 bold')

        button2 = tk.Button(self, text="Return", bg=Colors.Red, activebackground=Colors.Red, command=lambda: controller.show_frame("GamePage"))
        button3 = tk.Button(self, text="Cancel", bg=Colors.Red, activebackground=Colors.Red, command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green, command=lambda: DrawPage.start_game_and_show_next_page(controller, self.simulation_name, self.shape, 0, True, self.stepped))

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
        if stepped == True:
            controller.set_simulation_name_shape_and_show_frame("InProgressSteppedPage", simulation_name, shape)
        else:
            controller.frames["InProgressPage"].set_shape(shape)
            controller.frames["InProgressPage"].set_simulation_name(simulation_name)
            controller.frames["InProgressPage"].reset_speed()
            controller.frames["InProgressPage"].tkraise()
        if loadFromOutside:
            stop_motion_sensor()
        sr.run_game(shape, lifeSpawnChance, loadFromOutside, stepped)
        