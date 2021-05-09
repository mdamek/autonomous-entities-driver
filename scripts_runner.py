import json
import paramiko
import requests

with open('simulations.json') as json_file:
    config_file = json.load(json_file)
    config = config_file["config"]


def restart_led_servers():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=config["user"],
                    password=config["localPassword"])
        ssh.exec_command("sudo killall -9 node")
        ssh.exec_command(
            "cd Desktop/simulation-platform-for-autonomous-entities; sudo npx ts-node -T Server/app.ts < /dev/null > /tmp/mylogfile 2>&1 &")
        print(f"Led server restared on {host}")


def restart_all_devices():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=config["user"],
                    password=config["localPassword"])
        ssh.exec_command("sudo reboot")
        print(f"Raspberry {host} restarted")


def run_xinuk(simulation):
    loadFromOutside = str(simulation.from_outside).lower()
    stepped = str(simulation.stepped).lower()
    name = simulation.config["name"]
    xinuk_port = config["xinukPort"]
    supervisor_host = config["supervisor"]
    led_panel_port = config["ledPanelPort"]
    allocation_order = ",".join(config["akkaSpawnActorOrder"])
    user = config["user"]
    iterationsNumber = config["iterationsNumber"]
    width = simulation.x
    height = simulation.y
    width_workers = simulation.x_nodes
    height_workers = simulation.y_nodes
    workers_manager_port = config["actorsManagerPort"]
    signal_disabled = "false"
    min_nr_of_members = width_workers * height_workers

    for host in config["hosts"]:
        #privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
        #mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=config["localPassword"])
        args_list = []
        args_list.append("java")
        for key in simulation.parameters:
            parameter_name = key
            parameter_value = str(simulation.parameters[key].get())
            args_list.append(
                f"-D{name}.config.{parameter_name}={parameter_value}")
        args_list.append(f"-D{name}.config.isSupervisor=true") if host == config["supervisor"] else args_list.append(
            f"-D{name}.config.isSupervisor=false")
        args_list.append(f"-Dclustering.ip={host}")
        args_list.append(f"-Dclustering.port={xinuk_port}")
        args_list.append(f"-Dclustering.supervisor.ip={supervisor_host}")
        args_list.append(f"-Dclustering.supervisor.port={xinuk_port}")
        args_list.append(f"-Dclustering.min-nr-of-members={min_nr_of_members}")
        args_list.append(f"-Dstart-stepped={stepped}")
        args_list.append(f"-Dsupervisor={supervisor_host}")
        args_list.append(f"-Dworkers-manager-port={workers_manager_port}")
        args_list.append(f"-D{name}.config.workersRoot=2")
        args_list.append(
            f"-D{name}.config.iterationsNumber={iterationsNumber}")
        args_list.append(f"-D{name}.config.loadFromOutside={loadFromOutside}")
        args_list.append(f"-D{name}.config.guiType=ledPanel")
        args_list.append(f"-D{name}.config.ledPanelPort={led_panel_port}")
        args_list.append(f"-D{name}.config.worldWidth={width}")
        args_list.append(f"-D{name}.config.worldHeight={height}")
        args_list.append(f"-D{name}.config.workersX={width_workers}")
        args_list.append(f"-D{name}.config.workersY={height_workers}")
        args_list.append(f"-D{name}.config.signalDisabled={signal_disabled}")
        args_list.append(f"-Dshard-allocation-order={allocation_order}")
        args_list.append(
            f"-jar /home/pi/Desktop/xinuk/{name}/target/scala-2.13/{name}.jar")
        args_list.append("< /dev/null > /tmp/mylogfile 2>&1 &")
        print(' '.join(args_list))
        ssh.exec_command(' '.join(args_list))


def run_led_servers():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=config["user"],
                    password=config["localPassword"])
        ssh.exec_command(
            "cd Desktop/simulation-platform-for-autonomous-entities; sudo npx ts-node -T Server/app.ts < /dev/null > /tmp/mylogfile 2>&1 &")
        print(f"Led server started on {host}")


def kill_simulation():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=config["user"],
                    password=config["localPassword"])
        ssh.exec_command("sudo killall -9 java")
        led_panel_port = config["ledPanelPort"]
        requests.get(f"http://{host}:{led_panel_port}/clear")
        print(f"Xinuk killed on {host}")


def turn_off_the_platform():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=config["user"],
                    password=config["localPassword"])
        ssh.exec_command("sudo shutdown -h now")
        print(f"Platform off on {host}")
