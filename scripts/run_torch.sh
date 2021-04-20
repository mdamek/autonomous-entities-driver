#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"
APPLICATION_NAME="torch"
SHAPE="square"

SPAWNCHANCE=0
PERSONSPAWNCHANCE=0
FIRESPAWNCHANCE=0
EXITSPAWNCHANCE=0
PERSONMAXSPEED=0
FIRESPREADINGFREQUENCY=0
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
    -personSpawnChance)
        shift
        PERSONSPAWNCHANCE=$1
        shift
        ;;
    -fireSpawnChance)
        shift
        FIRESPAWNCHANCE=$1
        shift
        ;;
    -exitSpawnChance)
        shift
        EXITSPAWNCHANCE=$1
        shift
        ;;
    -personMaxSpeed)
        shift
        PERSONMAXSPEED=$1
        shift
        ;;
    -fireSpreadingFrequency)
        shift
        FIRESPREADINGFREQUENCY=$1
        shift
        ;;
    -stepped)
        shift
        STEPPED=$1
        shift
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

ITERATIONS_NUMBER=100
SIGNAL_DISABLED=false

MIN_NR_OF_MEMBERS=4
GUI_TYPE="ledPanel"
LED_PANEL_PORT=8000
XINUK_PORT=2551
WORKERS_ROOT=2

function run_xinuk() {
    local deviceIp=${1}
    local isSupervisor=${2}
    RUN_SCRIPT="java 
-D${APPLICATION_NAME}.config.isSupervisor=${isSupervisor} -Dclustering.ip=${deviceIp} -Dclustering.port=${XINUK_PORT} -Dclustering.supervisor.ip=${RASPBERRY1} -Dclustering.supervisor.port=${XINUK_PORT} 
-Dclustering.min-nr-of-members=${MIN_NR_OF_MEMBERS} -D${APPLICATION_NAME}.config.worldWidth=${WORLD_WIDTH} -D${APPLICATION_NAME}.config.workersX=${WORKERS_X} -D${APPLICATION_NAME}.config.workersY=${WORKERS_Y} 
-D${APPLICATION_NAME}.config.signalDisabled=${SIGNAL_DISABLED} -D${APPLICATION_NAME}.config.worldHeight=${WORLD_HEIGHT} -D${APPLICATION_NAME}.config.guiType=${GUI_TYPE} -D${APPLICATION_NAME}.config.ledPanelPort=${LED_PANEL_PORT} 
-D${APPLICATION_NAME}.config.workersRoot=${WORKERS_ROOT} -D${APPLICATION_NAME}.config.spawnChance=${SPAWNCHANCE} -D${APPLICATION_NAME}.config.personSpawnChance=${PERSONSPAWNCHANCE}
-D${APPLICATION_NAME}.config.fireSpawnChance=${FIRESPAWNCHANCE} -D${APPLICATION_NAME}.config.exitSpawnChance=${EXITSPAWNCHANCE} -D${APPLICATION_NAME}.config.personMaxSpeed=${PERSONMAXSPEED}
-D${APPLICATION_NAME}.config.fireSpreadingFrequency=${FIRESPREADINGFREQUENCY} -D${APPLICATION_NAME}.start-stepped=${STEPPED} -jar /home/pi/Desktop/xinuk/${APPLICATION_NAME}/target/scala-2.13/${APPLICATION_NAME}.jar"

    ssh -l ${USERNAME} $1 ${RUN_SCRIPT}
    echo Run Xinuk: ${APPLICATION_NAME} on ${deviceIp}
}

echo Running Xinuk ${APPLICATION_NAME} on every machine...
run_xinuk ${RASPBERRY2} false
run_xinuk ${RASPBERRY3} false
run_xinuk ${RASPBERRY4} false
run_xinuk ${RASPBERRY1} true
