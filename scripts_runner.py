import subprocess
import json
import paramiko
import os

def restart_led_servers():
    subprocess.call("scripts/kill_led_servers.sh")
    subprocess.call("scripts/run_led_servers.sh")


def restart_all_devices():
    subprocess.call("scripts/restart_all_devices.sh")


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
    with open('simulations.json') as json_file:
        config = json.load(json_file)["config"]
        xinuk_port = config["xinukPort"]
        supervisor_host = config["supervisor"]
        led_panel_port = config["ledPanelPort"]
        allocation_order = config["akkaSpawnActorOrder"]
        user = config["user"]
    for host in config["hosts"]:
        privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
        mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username = user, pkey = mykey)
        args_list = []
        args_list.append("java")
        for key in simulation.parameters:
            parameter_name = key
            parameter_value = str(simulation.parameters[key].get())
            args_list.append(
                f"-D{name}.config.{parameter_name}={parameter_value}")
        args_list.append(f"-D{name}.config.isSupervisor=true") if host == config["supervisor"] else args_list.append(
            f"-D{name}.config.isSupervisor=true")
        args_list.append(f"-Dclustering.ip={host}")
        args_list.append(f"-Dclustering.port={xinuk_port}")
        args_list.append(f"-Dclustering.supervisor.ip={supervisor_host}")
        args_list.append(f"-Dclustering.supervisor.port={xinuk_port}")
        args_list.append(f"-Dclustering.min-nr-of-members=4")
        args_list.append(f"-D{name}.config.guiType=ledPanel")
        args_list.append(f"-D{name}.config.ledPanelPort={led_panel_port}")
        args_list.append(f"-D{name}.config.workersRoot=2")
        args_list.append(f"-D{name}.config.loadFromOutside={loadFromOutside}")
        args_list.append(f"-Dstart-stepped={stepped}")
        #args_list.append(f"-Dshard-allocation-order={allocation_order}")
        args_list.append(f"-jar /home/pi/Desktop/xinuk/{name}/target/scala-2.13/{name}.jar")
        args_list.append("< /dev/null > /tmp/mylogfile 2>&1 &")
        ssh.exec_command(' '.join(args_list))

def run_led_servers():
    subprocess.call("scripts/run_led_servers.sh")


def kill_simulation():
    subprocess.call("scripts/kill_xinuk.sh")


def turn_off_the_platform():
    subprocess.call("scripts/turn_off_the_platform.sh")
