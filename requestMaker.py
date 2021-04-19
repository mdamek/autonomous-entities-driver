import requests

supervisor_host = "192.168.100.180"
port_of_actors_manager = "8013"
core = "http://%s:%s/" % (supervisor_host, port_of_actors_manager)

def start_stepped_simulation():
    path = core + "startSteppedSimulation"
    try:
        requests.get(path, timeout=5)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")

def stop_stepped_simulation():
    path = core + "stopSteppedSimulation"
    try:
        requests.get(path, timeout=5)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")

def make_iteration():
    path = core + "makeIteration"
    try:
        requests.get(path, timeout=5)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")

def set_simulation_delay(delay):
    path = core + "setSimulationDelay"
    params = {'delay' : delay}
    try:
        requests.get(path, params=params, timeout=5)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")