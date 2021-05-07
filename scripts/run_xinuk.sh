#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

GUI_TYPE="ledPanel"
LED_PANEL_PORT=8000
XINUK_PORT=2551
SIGNAL_DISABLED=false

function run_mock() {
    local deviceIp=${1}
    local isSupervisor=${2}
    local applicationScript=${3}
    RUN_SCRIPT="java 
-D${APPLICATION_NAME}.config.isSupervisor=${isSupervisor} -Dclustering.ip=${deviceIp} -Dclustering.port=${XINUK_PORT} -Dclustering.supervisor.ip=${RASPBERRY1} -Dclustering.supervisor.port=${XINUK_PORT} 
-Dclustering.min-nr-of-members=${MIN_NR_OF_MEMBERS} -D${APPLICATION_NAME}.config.worldWidth=${WORLD_WIDTH} -D${APPLICATION_NAME}.config.workersX=${WORKERS_X} -D${APPLICATION_NAME}.config.workersY=${WORKERS_Y} 
-D${APPLICATION_NAME}.config.signalDisabled=${SIGNAL_DISABLED} -D${APPLICATION_NAME}.config.worldHeight=${WORLD_HEIGHT} -D${APPLICATION_NAME}.config.guiType=${GUI_TYPE} -D${APPLICATION_NAME}.config.ledPanelPort=${LED_PANEL_PORT} 
-D${APPLICATION_NAME}.config.workersRoot=${WORKERS_ROOT} -D${APPLICATION_NAME}.config.spawnChance=${SPAWNCHANCE} -D${APPLICATION_NAME}.config.rabbitSpawnChance=${RABBITSPAWNCHANCE} -D${APPLICATION_NAME}.config.rabbitStartEnergy=${RABBITSTARTENERGY}
-D${APPLICATION_NAME}.config.rabbitReproductionCost=${RABBITREPRODUCTIONCOST} -D${APPLICATION_NAME}.config.rabbitLifeActivityCost=${RABBITLIFEACTIVITYCOST} -D${APPLICATION_NAME}.config.rabbitReproductionThreshold=${RABBITREPRODUCTIONTHRESHOLD}
-D${APPLICATION_NAME}.config.lettuceEnergeticCapacity=${LETTUCEENERGETICCAPACITY} -D${APPLICATION_NAME}.config.lettuceReproductionFrequency=${LETTUCEREPRODUCTIONFREQUENCY} -Dstart-stepped=${STEPPED} -jar /home/pi/Desktop/xinuk/${APPLICATION_NAME}/target/scala-2.13/${APPLICATION_NAME}.jar"

    ssh -l ${USERNAME} $1 ${RUN_SCRIPT} "< /dev/null > /tmp/mylogfile 2>&1 &"
    echo Run Xinuk ${APPLICATION_NAME}: ${APPLICATION_NAME} on ${deviceIp}
}

for arg in $@
do
	echo arg
done

#echo Running Xinuk ${APPLICATION_NAME} on every machine...
#run_mock ${RASPBERRY2} false
#run_mock ${RASPBERRY3} false
#run_mock ${RASPBERRY4} false
#run_mock ${RASPBERRY1} true
