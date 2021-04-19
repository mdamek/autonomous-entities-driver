import requests

supervisor_host = "192.168.100.180"
port_of_actors_manager = "8013"
core = "http://%s:%s/" % (supervisor_host, port_of_actors_manager)

def start_stepped_simulation():
    path = core + "startSteppedSimulation"
    requests.get(path, timeout=5)

def stop_stepped_simulation():
    path = core + "stopSteppedSimulation"
    requests.get(path, timeout=5)

def make_iteration():
    path = core + "makeIteration"
    requests.get(path, timeout=5)

def set_simulation_delay(delay):
    path = core + "setSimulationDelay"
    params = {'delay' : delay}
    requests.get(path, params=params, timeout=5)
