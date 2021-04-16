from helpers import SimulationDriver
import platform
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class MockPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: SimulationDriver.start_mock_and_show_next_page(controller, "mock", self.shape))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

    def set_shape(self, shape):
        self.shape = shape