#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"
APPLICATION_NAME="mock"
SHAPE="square"

while test $# -gt 0; do
    case "$1" in
    -shape)
        shift
        SHAPE=$1
        shift
        ;;
    -name)
        shift
        APPLICATION_NAME=$1
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
"vertical")
    WORLD_WIDTH=32
    WORLD_HEIGHT=128
    WORKERS_X=1
    WORKERS_Y=4
    ;;
"horizontal")
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

if [ ${APPLICATION_NAME} != mock ]; then
    echo "Define application name with flag -name: mock"
    exit 0
fi

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
-Dmock.config.isSupervisor=${isSupervisor} -Dclustering.ip=${deviceIp} -Dclustering.port=${XINUK_PORT} -Dclustering.supervisor.ip=${RASPBERRY1} -Dclustering.supervisor.port=${XINUK_PORT} 
-Dclustering.min-nr-of-members=${MIN_NR_OF_MEMBERS} -Dmock.config.worldWidth=${WORLD_WIDTH} -Dmock.config.workersX=${WORKERS_X} -Dmock.config.workersY=${WORKERS_Y} 
-Dmock.config.signalDisabled=${SIGNAL_DISABLED} -Dmock.config.worldHeight=${WORLD_HEIGHT} -Dmock.config.guiType=${GUI_TYPE} -Dmock.config.ledPanelPort=${LED_PANEL_PORT} 
-Dmock.config=workersRoot=${WORKERS_ROOT}  -jar /home/pi/Desktop/xinuk/${APPLICATION_NAME}/target/scala-2.13/${APPLICATION_NAME}.jar"

    ssh -l ${USERNAME} $1 ${RUN_SCRIPT} "< /dev/null > /tmp/mylogfile 2>&1 &"
    echo Run Xinuk: ${APPLICATION_NAME} on ${deviceIp}
}

echo Running Xinuk on every machine...
run_xinuk ${RASPBERRY1} true
run_xinuk ${RASPBERRY2} false
run_xinuk ${RASPBERRY3} false
run_xinuk ${RASPBERRY4} false
