import tkinter as tk                 
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
        button4 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("ShapePage"))                            
        button5 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("ShapePage"))                            
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
        button4 = tk.Button(self, text="Cancel",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack(fill = tk.BOTH, expand = True)
        button2.pack(fill = tk.BOTH, expand = True)
        button3.pack(fill = tk.BOTH, expand = True)
        button4.pack()

class InProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

class MockPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shape = tk.StringVar()

        button1 = tk.Button(self, text="Start",
                        command=lambda: controller.show_frame("InProgressPage"))
        button2 = tk.Button(self, text="Return",
                        command=lambda: controller.show_frame("ShapePage"))
        button3 = tk.Button(self, text="Cancel",
                        command=lambda: controller.show_frame("StartPage"))

        button1.pack()
        button2.pack()
        button3.pack()

    def set_shape(self, shape):
        self.shape.set(shape)

if __name__ == "__main__":
    app = App()
    #app.attributes('-fullscreen', True)
    app.mainloop()