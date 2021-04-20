import platform
import scripts_runner as sr 
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import BooleanVar, Radiobutton, Frame
    from tkinter.constants import TOP
else:
    import Tkinter as tk
    from Tkinter import BooleanVar, Radiobutton, Frame
    from Tkinter.constants import TOP

class MockPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""

        self.steppedSimulation = BooleanVar()

        topframe = Frame(self)
        topframe.pack(side=TOP)

        r1 = Radiobutton(topframe, text="Classical simulation", variable=self.steppedSimulation, value=False)
        r2 = Radiobutton(topframe, text="Stepped simulation", variable=self.steppedSimulation, value=True)
        
        button1 = tk.Button(self, text="Start", bg='#B2FFB0', activebackground='#B2FFB0',
                        command=lambda: self.start_mock_and_show_next_page(controller, "mock", self.shape, self.steppedSimulation.get()))
        button2 = tk.Button(self, text="Return", bg='#FFBEB0', activebackground='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", bg='#FFBEB0', activebackground='#FFBEB0',
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
            pass
        else:
            controller.set_simulation_name_shape_and_show_frame("InProgressPage", simulation_name, shape)
        sr.run_mock(shape)