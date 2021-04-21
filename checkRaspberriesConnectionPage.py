import platform
import subprocess
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
    from tkinter import BooleanVar, Radiobutton, Frame
else:
    import Tkinter as tk
    from Tkinter import BooleanVar, Radiobutton, Frame


class CkeckRaspberriesConnectionPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        for number in range(0,6):
            self.grid_rowconfigure(number, weight = 1, minsize=4)

        for number in range(0,2):
            self.grid_columnconfigure(number, weight = 1, minsize=4)

        self.avaliable = [tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()]

        self.avaliable[0].set("-")
        self.avaliable[1].set("-")
        self.avaliable[2].set("-")
        self.avaliable[3].set("-")

        hosts = ["192.168.100.180", "192.168.100.185","192.168.100.192","192.168.100.191",]

        tk.Label(self, text="Check connection with Raspberries", font=("Courier", 13)).grid(row=0, column=0, columnspan=2, sticky='nesw')
        tk.Label(self, text="RP-1: " + hosts[0], font=("Courier", 13)).grid(row=1, column=0, sticky='nesw')
        tk.Label(self, text="RP-2: " + hosts[1], font=("Courier", 13)).grid(row=2, column=0, sticky='nesw')
        tk.Label(self, text="RP-3: " + hosts[2], font=("Courier", 13)).grid(row=3, column=0, sticky='nesw')
        tk.Label(self, text="RP-4: " + hosts[3], font=("Courier", 13)).grid(row=4, column=0, sticky='nesw')

        tk.Label(self, textvariable=self.avaliable[0], font=("Courier", 13)).grid(row=1, column=1, sticky='nesw')
        tk.Label(self, textvariable=self.avaliable[1], font=("Courier", 13)).grid(row=2, column=1, sticky='nesw')
        tk.Label(self, textvariable=self.avaliable[2], font=("Courier", 13)).grid(row=3, column=1, sticky='nesw')
        tk.Label(self, textvariable=self.avaliable[3], font=("Courier", 13)).grid(row=4, column=1, sticky='nesw')

        tk.Button(self, text="Start", command=lambda: check_statuses(), bg='#B2FFB0', activebackground='#B2FFB0').grid(row=5, column=0, columnspan=2, sticky='nesw')

        tk.Button(self, text="Return", command=lambda: controller.show_frame("OptionsPage")).grid(row=6, column=0, columnspan=2, sticky='nesw')

        def check_statuses():
            param = '-n' if platform.system().lower()=='windows' else '-c'
    
            for idx, host in enumerate(hosts):   
                command = ['ping', param, '1', host]
                retVal = subprocess.call(command, stdout=subprocess.PIPE)
                if retVal == 0:
                    self.avaliable[idx].set("✔")
                else:
                    self.avaliable[idx].set("✘")

    def clean_statuses(self):
        self.avaliable[0].set("-")
        self.avaliable[1].set("-")
        self.avaliable[2].set("-")
        self.avaliable[3].set("-")