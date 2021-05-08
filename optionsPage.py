from colors import Colors
import threading
import scripts_runner as sr
import tkinter as tk


class OptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Button(self, text="Restart LED servers", bg=Colors.Yellow, activebackground=Colors.Yellow,
                  command=lambda: threading.Thread(target=sr.restart_led_servers).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Check Raspberries avaliability", bg=Colors.Yellow, activebackground=Colors.Yellow,
                  command=lambda: threading.Thread(target=self.open_avaliability_check).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Stop Xinuk", bg=Colors.Yellow, activebackground=Colors.Yellow,
                  command=lambda: threading.Thread(target=sr.kill_simulation).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Restart all devices", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: threading.Thread(target=sr.restart_all_devices).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Turn off platform", bg=Colors.Red, activebackground=Colors.Red,
                  command=lambda: threading.Thread(target=sr.turn_off_the_platform).start()).pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="Return",
                  command=lambda: controller.show_frame("StartPage")).pack(fill=tk.BOTH, expand=True)

    def open_avaliability_check(self):
        self.controller.frames["CkeckRaspberriesConnectionPage"].clean_statuses(
        )
        self.controller.show_frame("CkeckRaspberriesConnectionPage")
