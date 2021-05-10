from colors import Colors
import platform
import subprocess
import tkinter as tk


class CkeckRaspberriesConnectionPage(tk.Frame):

    def __init__(self, parent, controller, hosts):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        for number in range(0, len(hosts) + 3):
            self.grid_rowconfigure(number, weight=1, minsize=4)

        for number in range(0, 2):
            self.grid_columnconfigure(number, weight=1, minsize=4)

        self.avaliable = []
        for i in range(0, len(hosts)):
            self.avaliable.append(tk.StringVar())

        tk.Label(self, text="Check connection with Raspberries", font=(
            "Courier", 13)).grid(row=0, column=0, columnspan=2, sticky='nesw')

        for idx, host in enumerate(hosts):
            tk.Label(self, text=f"RP-{idx}: {host}", font=("Courier",
                     13)).grid(row=idx + 1, column=0, sticky='nesw')
            tk.Label(self, textvariable=self.avaliable[idx], font=(
                "Courier", 13)).grid(row=idx + 1, column=1, sticky='nesw')

        tk.Button(self, text="Start", command=lambda: check_statuses(), bg=Colors.Green,
                  activebackground=Colors.Green).grid(row=5, column=0, columnspan=2, sticky='nesw')

        tk.Button(self, text="Return", command=lambda:  self.controller.frames[
            "OptionsPage"].tkraise()).grid(row=6, column=0, columnspan=2, sticky='nesw')

        def check_statuses():
            param = '-n' if platform.system().lower() == 'windows' else '-c'

            for idx, host in enumerate(hosts):
                command = ['ping', param, '1', host]
                retVal = subprocess.call(command, stdout=subprocess.PIPE)
                if retVal == 0:
                    self.avaliable[idx].set("Ok")
                else:
                    self.avaliable[idx].set("Fail")

    def clean_statuses(self):
        for i in range(0, len(self.avaliable)):
            self.avaliable[i].set("-")
