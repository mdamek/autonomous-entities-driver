import threading
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
        
        tk.Label(self, text="Draw starting position on panels then click Start", font='Helvetica 14 bold').pack(side="top", fill="x")
        tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green, command=lambda: self.go_to_in_progress_page()).pack(side="bottom", fill = tk.BOTH, expand = True)
        tk.Button(self, text="Return", bg=Colors.Red, activebackground=Colors.Red, command=lambda: self.controller["ParametersPage"].tkraise()).pack(side="bottom", fill = tk.BOTH, expand = True)
        tk.Button(self, text="Cancel", bg=Colors.Red, activebackground=Colors.Red, command=lambda: self.controller["StartPage"].tkraise()).pack(side="bottom", fill = tk.BOTH, expand = True)

    def set_simulation(self, simulation):
        self.simulation = simulation

    def go_to_in_progress_page(self):
        threading.Thread(target=stop_motion_sensor).start()
        if self.stepped:
            self.controller.frames["InProgressSteppedPage"].set_simulation(self.simulation)
            self.controller.frames["InProgressSteppedPage"].tkraise()
        else:
            self.controller.frames["InProgressPage"].set_simulation(self.simulation)
            self.controller.frames["InProgressPage"].tkraise()
        #run similation
        #sr.run_game(shape, lifeSpawnChance, loadFromOutside, stepped)
        