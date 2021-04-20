import subprocess

def restart_led_servers():
    subprocess.call("scripts/kill_led_servers.sh")
    subprocess.call("scripts/run_led_servers.sh")

def restart_all_devices():
    subprocess.call("scripts/restart_all_devices.sh")

def run_mock(shape):
    subprocess.call(['scripts/run_mock.sh', '-shape', shape])

def run_rabbits(shape, spawnChance, rabbitSpawnChance, rabbitStartEnergy, rabbitReproductionCost, rabbitLifeActivityCost, rabbitReproductionThreshold, lettuceEnergeticCapacity, lettuceReproductionFrequency):
    subprocess.call(['scripts/run_rabbits.sh', '-shape', shape, '-spawnChance', str(spawnChance), '-rabbitSpawnChance', str(rabbitSpawnChance), '-rabbitStartEnergy', str(rabbitStartEnergy), '-rabbitReproductionCost',
    str(rabbitReproductionCost), '-rabbitLifeActivityCost', str(rabbitLifeActivityCost), '-rabbitReproductionThreshold', str(rabbitReproductionThreshold), '-lettuceEnergeticCapacity', str(lettuceEnergeticCapacity), '-lettuceReproductionFrequency',
    str(lettuceReproductionFrequency)])

def run_fortwist(shape, foraminiferaSpawnChance, foraminiferaStartEnergy, foraminiferaReproductionCost, foraminiferaReproductionThreshold, foraminiferaLifeActivityCost, algaeStartEnergy, algaeRegenerationRate, 
    algaeEnergeticCapacity):
    subprocess.call(['scripts/run_fortwist.sh', '-shape', shape, '-foraminiferaSpawnChance', str(foraminiferaSpawnChance), '-foraminiferaStartEnergy', str(foraminiferaStartEnergy), '-foraminiferaReproductionCost',
    str(foraminiferaReproductionCost), '-foraminiferaReproductionThreshold', str(foraminiferaReproductionThreshold), '-foraminiferaLifeActivityCost', str(foraminiferaLifeActivityCost), 
    '-algaeStartEnergy', str(algaeStartEnergy),  '-algaeRegenerationRate', str(algaeRegenerationRate), '-algaeEnergeticCapacity', str(algaeEnergeticCapacity)])

def run_torch(shape, spawnChance, personSpawnChance, fireSpawnChance, exitSpawnChance, personMaxSpeed, fireSpreadingFrequency):
    subprocess.call(['scripts/run_torch.sh', '-shape', shape, '-spawnChance', str(spawnChance), '-personSpawnChance', str(personSpawnChance), '-fireSpawnChance',
    str(fireSpawnChance), '-exitSpawnChance', str(exitSpawnChance), '-personMaxSpeed', str(personMaxSpeed), 
    '-fireSpreadingFrequency', str(fireSpreadingFrequency)])

def run_game(shape, lifeSpawnChance, loadFromOutside):
    subprocess.call(['scripts/run_game.sh', '-shape', shape, '-lifeSpawnChance', str(lifeSpawnChance), '-loadFromOutside', str(loadFromOutside).lower()])

def run_led_servers():
    subprocess.call("scripts/run_led_servers.sh")

def kill_simulation():
    subprocess.call("scripts/kill_xinuk.sh")

def turn_off_the_platform():
    subprocess.call("scripts/turn_off_the_platform.sh")