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

def run_led_servers():
    subprocess.call("scripts/run_led_servers.sh")

def kill_simulation():
    subprocess.call("scripts/kill_xinuk.sh")

def turn_off_the_platform():
    subprocess.call("scripts/turn_off_the_platform.sh")