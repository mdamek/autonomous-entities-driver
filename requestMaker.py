import subprocess
import requests
import platform

supervisor_host = "192.168.1.87"
port_of_actors_manager = "8013"
core = "http://%s:%s/" % (supervisor_host, port_of_actors_manager)
timeouts = 5
def start_stepped_simulation():
    path = core + "startSteppedSimulation"
    try:
        requests.get(path, timeout=timeouts)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")

def stop_stepped_simulation():
    path = core + "stopSteppedSimulation"
    try:
        requests.get(path, timeout=timeouts)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")

def make_iteration():
    path = core + "makeIteration"
    try:
        requests.get(path, timeout=timeouts)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")

def set_simulation_delay(delay):
    path = core + "setSimulationDelay"
    params = {'delay' : delay}
    try:
        requests.get(path, params=params, timeout=timeouts)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")


def start_motion_sensor(shape):
    motion_sensor_interface = "192.168.1.20"
    motion_sensor_port = "8888"
    core_sensor = "http://%s:%s/api/v1/" %(motion_sensor_interface, motion_sensor_port)
    path = core_sensor + "startReadingPositions"
    params  ={'shape' : shape}
    requests.get(path, params=params, timeout=10000)

def stop_motion_sensor():
    motion_sensor_interface = "192.168.1.20"
    motion_sensor_port = "8888"
    core_sensor = "http://%s:%s/api/v1/" %(motion_sensor_interface, motion_sensor_port)
    path = core_sensor + "stopReadingPositions"
    requests.get(path, timeout=timeouts)

