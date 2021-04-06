import Tkinter as tk      
import scripts_runner as sr          
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ShapePage, InProgressPage, MockPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def set_shape_and_show_frame(self, page_name, shape):
        self.frames[page_name].set_shape(shape)
        self.frames[page_name].tkraise()

    def set_simulation_name_and_show_frame(self, page_name, simulation_name):
        self.frames[page_name].set_simulation_name(simulation_name)
        self.frames[page_name].tkraise()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Mock",
                            command=lambda: controller.show_frame("ShapePage"))
        button2 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("ShapePage"))
        button4 = tk.Button(self, text="Restart LED servers", bg='#FFFEB0',
                            command=lambda: sr.restart_led_servers())                            
        button5 = tk.Button(self, text="Restart all devices", bg='#FFBEB0',
                            command=lambda: sr.restart_all_devices())                            
        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)
        button5.pack(fill = tk.BOTH, expand = True)

class ShapePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = tk.Button(self, text="Square",
                           command=lambda: controller.set_shape_and_show_frame("MockPage", "square"))
        button2 = tk.Button(self, text="Vertical",
                           command=lambda: controller.set_shape_and_show_frame("MockPage", "vertical"))
        button3 = tk.Button(self, text="Horizontal",
                           command=lambda: controller.set_shape_and_show_frame("MockPage", "horizontal"))                   
        button4 = tk.Button(self, text="Cancel", bg='#FFBEB0',
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack(fill = tk.BOTH, expand = True)

class InProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.simulation_text = tk.StringVar()

        label = tk.Label(self, textvariable=self.simulation_text, font=("Courier", 44))
        button1 = tk.Button(self, text="Stop", bg='#FFBEB0',
                           command=lambda: controller.show_frame("StartPage"), font=("Courier", 44))

        label.pack(side="top", fill="x")
        button1.pack(side="bottom", fill = tk.BOTH, expand = True)

    def set_simulation_name(self, simulation_name):
        self.simulation_text.set(simulation_name + " simulation in progress...")


class MockPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = tk.StringVar()

        button1 = tk.Button(self, text="Start", height=8, bg='#B2FFB0',
                        command=lambda: controller.set_simulation_name_and_show_frame("InProgressPage", "Mock"))
        button2 = tk.Button(self, text="Return", height=4, bg='#FFBEB0',
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel", height=4, bg='#FFBEB0',
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button3.pack(side="bottom", fill="x")

    def set_shape(self, shape):
        self.shape.set(shape)

if __name__ == "__main__":
    app = App()
    #app.attributes('-fullscreen', True)
    app.mainloop()