#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"
APPLICATION_NAME="rabbits"
SHAPE="square"

SPAWNCHANCE=0
RABBITSPAWNCHANCE=0
RABBITSTARTENERGY=0
RABBITREPRODUCTIONCOST=0
RABBITREPRODUCTIONTHRESHOLD=0
LETTUCEENERGETICCAPACITY=0
LETTUCEREPRODUCTIONFREQUENCY=0
RABBITLIFEACTIVITYCOST=0
STEPPED=false

while test $# -gt 0; do
    case "$1" in
    -shape)
        shift
        SHAPE=$1
        shift
        ;;
    -spawnChance)
        shift
        SPAWNCHANCE=$1
        shift
        ;;
    -rabbitSpawnChance)
        shift
        RABBITSPAWNCHANCE=$1
        shift
        ;;
    -rabbitStartEnergy)
        shift
        RABBITSTARTENERGY=$1
        shift
        ;;
    -rabbitReproductionCost)
        shift
        RABBITREPRODUCTIONCOST=$1
        shift
        ;;
    -rabbitReproductionThreshold)
        shift
        RABBITREPRODUCTIONTHRESHOLD=$1
        shift
        ;;
    -lettuceEnergeticCapacity)
        shift
        LETTUCEENERGETICCAPACITY=$1
        shift
        ;;
    -lettuceReproductionFrequency)
        shift
        LETTUCEREPRODUCTIONFREQUENCY=$1
        shift
        ;;
    -rabbitLifeActivityCost)
        shift
        RABBITLIFEACTIVITYCOST=$1
        shift
        ;;
    -stepped)
        shift
        STEPPED=$1
        shift
        ;;
    *)
        echo "$1 is not a recognized flag!"
        exit 0
        ;;
    esac
done

WORLD_WIDTH=0
WORLD_HEIGHT=0
WORKERS_X=0
WORKERS_Y=0

case ${SHAPE} in
"square")
    WORLD_WIDTH=64
    WORLD_HEIGHT=64
    WORKERS_X=2
    WORKERS_Y=2
    ;;
"horizontal")
    WORLD_WIDTH=32
    WORLD_HEIGHT=128
    WORKERS_X=1
    WORKERS_Y=4
    ;;
"vertical")
    WORLD_WIDTH=128
    WORLD_HEIGHT=32
    WORKERS_X=4
    WORKERS_Y=1
    ;;
*)
    echo "Define the shape of the space with flag -shape: square, horizontal or vertical"
    exit 0
    ;;
esac

MIN_NR_OF_MEMBERS=4
GUI_TYPE="ledPanel"
LED_PANEL_PORT=8000
XINUK_PORT=2551
WORKERS_ROOT=2

ITERATIONS_NUMBER=100
SIGNAL_DISABLED=false

function run_mock() {
    local deviceIp=${1}
    local isSupervisor=${2}
    RUN_SCRIPT="java 
-D${APPLICATION_NAME}.config.isSupervisor=${isSupervisor} -Dclustering.ip=${deviceIp} -Dclustering.port=${XINUK_PORT} -Dclustering.supervisor.ip=${RASPBERRY1} -Dclustering.supervisor.port=${XINUK_PORT} 
-Dclustering.min-nr-of-members=${MIN_NR_OF_MEMBERS} -D${APPLICATION_NAME}.config.worldWidth=${WORLD_WIDTH} -D${APPLICATION_NAME}.config.workersX=${WORKERS_X} -D${APPLICATION_NAME}.config.workersY=${WORKERS_Y} 
-D${APPLICATION_NAME}.config.signalDisabled=${SIGNAL_DISABLED} -D${APPLICATION_NAME}.config.worldHeight=${WORLD_HEIGHT} -D${APPLICATION_NAME}.config.guiType=${GUI_TYPE} -D${APPLICATION_NAME}.config.ledPanelPort=${LED_PANEL_PORT} 
-D${APPLICATION_NAME}.config.workersRoot=${WORKERS_ROOT} -D${APPLICATION_NAME}.config.spawnChance=${SPAWNCHANCE} -D${APPLICATION_NAME}.config.rabbitSpawnChance=${RABBITSPAWNCHANCE} -D${APPLICATION_NAME}.config.rabbitStartEnergy=${RABBITSTARTENERGY}
-D${APPLICATION_NAME}.config.rabbitReproductionCost=${RABBITREPRODUCTIONCOST} -D${APPLICATION_NAME}.config.rabbitLifeActivityCost=${RABBITLIFEACTIVITYCOST} -D${APPLICATION_NAME}.config.rabbitReproductionThreshold=${RABBITREPRODUCTIONTHRESHOLD}
-D${APPLICATION_NAME}.config.lettuceEnergeticCapacity=${LETTUCEENERGETICCAPACITY} -D${APPLICATION_NAME}.config.lettuceReproductionFrequency=${LETTUCEREPRODUCTIONFREQUENCY} -D${APPLICATION_NAME}.start-stepped=${STEPPED} -jar /home/pi/Desktop/xinuk/${APPLICATION_NAME}/target/scala-2.13/${APPLICATION_NAME}.jar"

    ssh -l ${USERNAME} $1 ${RUN_SCRIPT} "< /dev/null > /tmp/mylogfile 2>&1 &"
    echo Run Xinuk ${APPLICATION_NAME}: ${APPLICATION_NAME} on ${deviceIp}
}

echo Running Xinuk ${APPLICATION_NAME} on every machine...
run_mock ${RASPBERRY2} false
run_mock ${RASPBERRY3} false
run_mock ${RASPBERRY4} false
run_mock ${RASPBERRY1} true
