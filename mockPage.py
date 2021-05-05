from colors import Colors
import platform
import scripts_runner as sr 
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import BooleanVar, Radiobutton, Frame
else:
    import Tkinter as tk
    from Tkinter import BooleanVar, Radiobutton, Frame

class MockPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        self.steppedSimulation = BooleanVar()

        topframe = Frame(self)
        topframe.pack(side="top")

        r1 = Radiobutton(topframe, text="Classical simulation", variable=self.steppedSimulation, value=False)
        r2 = Radiobutton(topframe, text="Stepped simulation", variable=self.steppedSimulation, value=True)
        
        button1 = tk.Button(self, text="Start", bg=Colors.Green, activebackground=Colors.Green,
                        command=lambda: self.start_mock_and_show_next_page(controller, "mock", self.shape, self.steppedSimulation.get()))
        button2 = tk.Button(self, text="Return", bg=Colors.Red, activebackground=Colors.Red,
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", bg=Colors.Red, activebackground=Colors.Red,
                        command=lambda: controller.show_frame("StartPage"))

        r1.pack(side=tk.LEFT)
        r2.pack(side=tk.LEFT)

        button1.pack(side="bottom", fill = tk.BOTH, expand = True)
        button2.pack(side="bottom", fill = tk.BOTH, expand = True)
        button3.pack(side="bottom", fill = tk.BOTH, expand = True)

    def set_shape(self, shape):
        self.shape = shape

    def start_mock_and_show_next_page(self, controller, simulation_name, shape, stepped):
        if stepped == True:
            controller.set_simulation_name_shape_and_show_frame("InProgressSteppedPage", simulation_name, shape)
        else:
            controller.frames["InProgressPage"].set_shape(shape)
            controller.frames["InProgressPage"].set_simulation_name(simulation_name)
            controller.frames["InProgressPage"].reset_speed()
            controller.frames["InProgressPage"].tkraise()
        sr.run_mock(shape, stepped)