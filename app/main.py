
import Tkinter as tk                 
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, DemoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select simulation")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start demo",
                            command=lambda: controller.show_frame("DemoPage"))
        button2 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("DemoPage"))
        button3 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("DemoPage"))
        button4 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("DemoPage"))                            
        button5 = tk.Button(self, text="Start...",
                            command=lambda: controller.show_frame("DemoPage"))                            
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()



class DemoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Stop",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.attributes('-fullscreen', True)
    app.mainloop()
