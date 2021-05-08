import subprocess
import json
import paramiko
import os

with open('simulations.json') as json_file:
        config_file = json.load(json_file)
        config = config_file["config"]

def restart_led_servers():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username = config["user"], password=config["localPassword"])
        ssh.exec_command("sudo killall -9 node")
        ssh.exec_command("cd Desktop/simulation-platform-for-autonomous-entities; sudo npx ts-node -T Server/app.ts < /dev/null > /tmp/mylogfile 2>&1 &")
        print(f"Led server restared on {host}")

def restart_all_devices():
    for host in config["hosts"]:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username = config["user"], password=config["localPassword"])
        ssh.exec_command("sudo reboot")
        print(f"Raspberry {host} restarted")

def run_mock(shape, stepped):
    subprocess.call(['scripts/run_mock.sh', '-shape', shape,
                    '-stepped', str(stepped).lower()])


def run_rabbits(shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency, stepped):
    subprocess.call(['scripts/run_rabbits.sh', '-shape', shape, '-spawnChance', str(spawnChance), '-rabbitSpawnChance', str(rabbitSpawnChance), '-rabbitStartEnergy', str(rabbitStartEnergy), '-rabbitReproductionCost',
                     str(rabbitReproductionCost), '-rabbitLifeActivityCost', str(rabbitLifeActivityCost), '-rabbitReproductionThreshold', str(
                         rabbitReproductionThreshold), '-lettuceEnergeticCapacity', str(lettuceEnergeticCapacity), '-lettuceReproductionFrequency',
                     str(lettuceReproductionFrequency), '-stepped', str(stepped).lower()])


def run_fortwist(shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, foraminiferaLifeActivityCost, algaeStartEnergy, algaeRegenerationRate,
                 algaeEnergeticCapacity, stepped):
    subprocess.call(['scripts/run_fortwist.sh', '-shape', shape, '-foraminiferaSpawnChance', str(foraminiferaSpawnChance), '-foraminiferaStartEnergy', str(foraminiferaStartEnergy), '-foraminiferaReproductionCost',
                     str(foraminiferaReproductionCost), '-foraminiferaReproductionThreshold', str(
                         foraminiferaReproductionThreshold), '-foraminiferaLifeActivityCost', str(foraminiferaLifeActivityCost),
                     '-algaeStartEnergy', str(algaeStartEnergy),  '-algaeRegenerationRate', str(algaeRegenerationRate), '-algaeEnergeticCapacity', str(algaeEnergeticCapacity), '-stepped', str(stepped).lower()])


def run_torch(shape, spawnChance, personSpawnChance, fireSpawnChance, exitSpawnChance, personMaxSpeed, fireSpreadingFrequency, stepped):
    subprocess.call(['scripts/run_torch.sh', '-shape', shape, '-spawnChance', str(spawnChance), '-personSpawnChance', str(personSpawnChance), '-fireSpawnChance',
                     str(fireSpawnChance), '-exitSpawnChance', str(
                         exitSpawnChance), '-personMaxSpeed', str(personMaxSpeed),
                     '-fireSpreadingFrequency', str(fireSpreadingFrequency), '-stepped', str(stepped).lower()])


def run_game(shape, lifeSpawnChance, loadFromOutside, stepped):
    subprocess.call(['scripts/run_game.sh', '-shape', shape, '-lifeSpawnChance', str(lifeSpawnChance),
                    '-loadFromOutside', str(loadFromOutside).lower(), '-stepped', str(stepped).lower()])


def run_xinuk(simulation):
    shape = simulation.shape
    loadFromOutside = str(simulation.from_outside).lower()
    stepped = str(simulation.stepped).lower()
    name = simulation.config["name"]
    xinuk_port = config["xinukPort"]
    supervisor_host = config["supervisor"]
    led_panel_port = config["ledPanelPort"]
    allocation_order = ",".join(config["akkaSpawnActorOrder"])
    user = config["user"]
    iterationsNumber = config["iterationsNumber"]
    shapes_config = config_file["shapes"]
    shape = simulation.shape
    selected_shape_config = next(
            filter(lambda shapes_config: shapes_config["name"] == shape, shapes_config))
    width = selected_shape_config["width"]
    height = selected_shape_config["height"]
    width_workers = selected_shape_config["width_workers"]
    height_workers = selected_shape_config["height_workers"]
    workers_manager_port = selected_shape_config["actorsManagerPort"]
    signal_disabled = "false"
    min_nr_of_members = width_workers * height_workers

    for host in config["hosts"]:
        #privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
        #mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username = user, password=config["localPassword"])
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
        args_list.append(f"-Dworker-manager-host={supervisor_host}")
        args_list.append(f"-Dworkers-manager-port={workers_manager_port}")
        args_list.append(f"-D{name}.config.workersRoot=2")
        args_list.append(f"-D{name}.config.iterationsNumber={iterationsNumber}")
        args_list.append(f"-D{name}.config.loadFromOutside={loadFromOutside}")
        args_list.append(f"-D{name}.config.guiType=ledPanel")
        args_list.append(f"-D{name}.config.ledPanelPort={led_panel_port}")
        args_list.append(f"-D{name}.config.worldWidth={width}")
        args_list.append(f"-D{name}.config.worldHeight={height}")
        args_list.append(f"-D{name}.config.workersX={width_workers}")
        args_list.append(f"-D{name}.config.workersY={height_workers}")
        args_list.append(f"-D{name}.config.signalDisabled={signal_disabled}")
        args_list.append(f"-Dshard-allocation-order={allocation_order}")
        args_list.append(f"-jar /home/pi/Desktop/xinuk/{name}/target/scala-2.13/{name}.jar")
        args_list.append("< /dev/null > /tmp/mylogfile 2>&1 &")
        print(' '.join(args_list))
        ssh.exec_command(' '.join(args_list))

def run_led_servers():
    subprocess.call("scripts/run_led_servers.sh")


def kill_simulation():
    subprocess.call("scripts/kill_xinuk.sh")


def turn_off_the_platform():
    subprocess.call("scripts/turn_off_the_platform.sh")
