import subprocess

def restart_led_servers():
    subprocess.call("scripts/kill_led_servers.sh")
    subprocess.call("scripts/run_led_servers.sh")

def restart_all_devices():
    subprocess.call("scripts/restart_all_devices.sh")

def run_simulation(name, shape):
     subprocess.call(['scripts/run_xinuk.sh', '-name', name, '-shape', shape])

def run_led_servers():
    subprocess.call("scripts/run_led_servers.sh")

def kill_simulation():
    subprocess.call("scripts/kill_xinuk.sh")