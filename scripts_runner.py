import subprocess

def restart_led_servers():
    subprocess.call("scripts/kill_led_servers.sh")
    subprocess.call("scripts/run_led_servers.sh")

def restart_all_devices():
    subprocess.call("scripts/restart_all_devices.sh")

def run_mock(shape, stepped):
    subprocess.call(['scripts/run_mock.sh', '-shape', shape, '-stepped', str(stepped).lower()])

def run_rabbits(shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency, stepped):
    subprocess.call(['scripts/run_rabbits.sh', '-shape', shape, '-spawnChance', str(spawnChance), '-rabbitSpawnChance', str(rabbitSpawnChance), '-rabbitStartEnergy', str(rabbitStartEnergy), '-rabbitReproductionCost',
    str(rabbitReproductionCost), '-rabbitLifeActivityCost', str(rabbitLifeActivityCost), '-rabbitReproductionThreshold', str(rabbitReproductionThreshold), '-lettuceEnergeticCapacity', str(lettuceEnergeticCapacity), '-lettuceReproductionFrequency',
    str(lettuceReproductionFrequency), '-stepped', str(stepped).lower()])

def run_fortwist(shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, foraminiferaLifeActivityCost, algaeStartEnergy, algaeRegenerationRate, 
    algaeEnergeticCapacity, stepped):
    subprocess.call(['scripts/run_fortwist.sh', '-shape', shape, '-foraminiferaSpawnChance', str(foraminiferaSpawnChance), '-foraminiferaStartEnergy', str(foraminiferaStartEnergy), '-foraminiferaReproductionCost',
    str(foraminiferaReproductionCost), '-foraminiferaReproductionThreshold', str(foraminiferaReproductionThreshold), '-foraminiferaLifeActivityCost', str(foraminiferaLifeActivityCost), 
    '-algaeStartEnergy', str(algaeStartEnergy),  '-algaeRegenerationRate', str(algaeRegenerationRate), '-algaeEnergeticCapacity', str(algaeEnergeticCapacity), '-stepped', str(stepped).lower()])

def run_torch(shape, spawnChance, personSpawnChance, fireSpawnChance, exitSpawnChance, personMaxSpeed, fireSpreadingFrequency, stepped):
    subprocess.call(['scripts/run_torch.sh', '-shape', shape, '-spawnChance', str(spawnChance), '-personSpawnChance', str(personSpawnChance), '-fireSpawnChance',
    str(fireSpawnChance), '-exitSpawnChance', str(exitSpawnChance), '-personMaxSpeed', str(personMaxSpeed), 
    '-fireSpreadingFrequency', str(fireSpreadingFrequency), '-stepped', str(stepped).lower()])

def run_game(shape, lifeSpawnChance, loadFromOutside, stepped):
    subprocess.call(['scripts/run_game.sh', '-shape', shape, '-lifeSpawnChance', str(lifeSpawnChance), '-loadFromOutside', str(loadFromOutside).lower(), '-stepped', str(stepped).lower()])

def run_xinuk(simulation):
    shape = simulation.shape
    loadFromOutside = simulation.from_outside
    stepped = simulation.stepped
    name = simulation.config["name"]
    args_list = []
    for key in simulation.parameters:
        parameter_name = key
        parameter_value = str(simulation.parameters[key].get())
        args_list.append(parameter_name)
        args_list.append(parameter_value)
    args_list.append("shape")
    args_list.append(shape)
    args_list.append("loadFromOutside")
    args_list.append(str(loadFromOutside).lower())
    args_list.append("stepped")
    args_list.append(str(stepped).lower())
    args_list.append("name")
    args_list.append(str(name).lower())
    print("All selected parameters: " + ' '.join(args_list))
    subprocess.call(['scripts/run_xinuk.sh'] + args_list)
    



def run_led_servers():
    subprocess.call("scripts/run_led_servers.sh")

def kill_simulation():
    subprocess.call("scripts/kill_xinuk.sh")

def turn_off_the_platform():
    subprocess.call("scripts/turn_off_the_platform.sh")