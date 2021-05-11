import json
import requests

with open('simulations.json') as json_file:
    config = json.load(json_file)

supervisor_host = config["config"]["supervisor"]
port_of_actors_manager = config["config"]["actorsManagerPort"]
motion_sensor_host = config["config"]["motionSensor"]["host"]
motion_sensor_port = config["config"]["motionSensor"]["port"]

drawing_server_hosts = config["config"]["hosts"]
drawing_server_port = config["config"]["ledPanelPort"]

actor_manager_core = f"http://{supervisor_host}:{port_of_actors_manager}/"
motion_sensor_core = f"http://{motion_sensor_host}:{motion_sensor_port}/api/v1/"

timeout = 3


def start_stepped_simulation():
    print("Start stepped simulation")
    path = actor_manager_core + "startSteppedSimulation"
    try:
        requests.get(path, timeout=timeout)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")


def stop_stepped_simulation():
    print("Stop stepped simulation")
    path = actor_manager_core + "stopSteppedSimulation"
    try:
        requests.get(path, timeout=timeout)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")


def make_iteration():
    print("Make iteration")
    path = actor_manager_core + "makeIteration"
    try:
        requests.get(path, timeout=timeout)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")


def set_simulation_delay(delay):
    print("Set simulation delay")
    path = actor_manager_core + "setSimulationDelay"
    params = {'delay': delay}
    try:
        requests.get(path, params=params, timeout=timeout)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")


def configure_drawing_server(simulation):
    print("Configure drawing server")
    avaliableColors = simulation.config["avaliableToDraw"]
    body = {"nodes": drawing_server_hosts, "xNodes": simulation.x_nodes,
            "yNodes": simulation.y_nodes, "avaliableColors": avaliableColors}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    for host in drawing_server_hosts:
        try:
            requests.post(f"http://{host}:{drawing_server_port}/configureDrawing", data=json.dumps(body), headers=headers)
        except requests.Timeout:
            print("Timeout on: ", host)
        except requests.ConnectionError:
            print("Request error")

def set_color(color):
    print(f"Set server color on {color}")
    color = color.replace("#", "")
    for host in drawing_server_hosts:
        try:
            requests.get(f"http://{host}:{drawing_server_port}/setColor/{color}")
        except requests.Timeout:
            print("Timeout on: ", host)
        except requests.ConnectionError:
            print("Request error")


def start_motion_sensor(shape):
    print("Start motion sensor")
    path = motion_sensor_core + "startReadingPositions"
    params = {'shape': shape}
    try:
        requests.get(path, params=params, timeout=timeout)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")


def stop_motion_sensor():
    print("Stop motion sensor")
    path = motion_sensor_core + "stopReadingPositions"
    try:
        requests.get(path, timeout=timeout)
    except requests.Timeout:
        print("Timeout on: ", path)
    except requests.ConnectionError:
        print("Request error")
