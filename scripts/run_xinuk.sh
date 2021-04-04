#!/usr/bin/bash
source raspberry_hosts.sh

USERNAME="pi"

APLICATION_NAME="mock"

WORLD_WIDTH=128
WORLD_HEIGHT=32
ITERATIONS_NUMBER=100
MIN_NR_OF_MEMBERS=4
GUI_TYPE="ledPanel"
LED_PANEL_PORT=8000
WORKERS_ROOT=2
WORKERS_X=4
WORKERS_Y=1
XINUK_PORT=2551
SIGNAL_DISABLED=true

function run_xinuk () {
RUN_SCRIPT="java -Dmock.config.isSupervisor=$2  
-Dclustering.ip=$1 -Dclustering.port=${XINUK_PORT} 
-Dclustering.supervisor.ip=${RASPBERRY1} -Dclustering.supervisor.port=${XINUK_PORT} 
-Dclustering.min-nr-of-members=${MIN_NR_OF_MEMBERS} -Dmock.config.worldWidth=${WORLD_WIDTH}
-Dmock.config.workersX=${WORKERS_X} -Dmock.config.workersY=${WORKERS_Y} -Dmock.config.signalDisabled=${SIGNAL_DISABLED}
-Dmock.config.worldHeight=${WORLD_HEIGHT} -Dmock.config.guiType=${GUI_TYPE}
-Dmock.config.ledPanelPort=${LED_PANEL_PORT} -Dmock.config=workersRoot=${WORKERS_ROOT} 
-jar /home/pi/Desktop/xinuk/${APLICATION_NAME}/target/scala-2.13/${APLICATION_NAME}.jar"

ssh -l ${USERNAME} $1 ${RUN_SCRIPT} "< /dev/null > /tmp/mylogfile 2>&1 &"
echo Run Xinuk: ${APPLICATION_NAME} on $1
}

echo Running Xinuk on every machine...
run_xinuk ${RASPBERRY1} true
run_xinuk ${RASPBERRY2} false
run_xinuk ${RASPBERRY3} false
run_xinuk ${RASPBERRY4} false
