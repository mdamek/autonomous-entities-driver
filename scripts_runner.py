import subprocess
import os

def restart_led_servers():
    subprocess.call("scripts/kill_led_servers.sh")
    subprocess.call("scripts/run_led_servers.sh")