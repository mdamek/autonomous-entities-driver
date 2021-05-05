import platform
import threading
import scripts_runner as sr 
if (platform.node() == "DESKTOP-TREPOQV"):
    import tkinter as tk
else:
    import Tkinter as tk

class OptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Button(self, text="Restart LED servers", bg='#FFFEB0', activebackground='#FFFEB0',
                  command=lambda: threading.Thread(target=sr.restart_led_servers).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Check Raspberries avaliability", bg='#FFFEB0', activebackground='#FFFEB0',
                  command=lambda: threading.Thread(target=self.open_avaliability_check).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Stop Xinuk", bg='#FFFEB0', activebackground='#FFFEB0',
                  command=lambda: threading.Thread(target=sr.kill_simulation).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Restart all devices", bg='#FFBEB0', activebackground='#FFBEB0',
                  command=lambda: threading.Thread(target=sr.restart_all_devices).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Turn off platform", bg='#FFBEB0', activebackground='#FFBEB0',
                            command=lambda: threading.Thread(target=sr.turn_off_the_platform).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Return",
                            command=lambda: controller.show_frame("StartPage")).pack(fill=tk.BOTH, expand=True)

    def open_avaliability_check(self):
        self.controller.frames["CkeckRaspberriesConnectionPage"].clean_statuses()
        self.controller.show_frame("CkeckRaspberriesConnectionPage")