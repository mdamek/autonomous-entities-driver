import platform

if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk  
else:
    import Tkinter as tk 

class InProgressSteppedPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = ""
        self.simulation_text = tk.StringVar()