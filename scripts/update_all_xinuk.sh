#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

PROJECTS=("mock" "torch" "fortwist" "game" "rabbits")

echo Updating Xinuk...
echo $UPDATEXINUKSCRIPT
for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "cd Desktop/xinuk; git pull;"
    for PROJECT in ${PROJECTS[@]} ; do
        echo ${HOSTNAME} : ${PROJECT}
        ssh -l ${USERNAME} ${HOSTNAME} "cd Desktop/xinuk; sbt ${PROJECT}/assembly < /dev/null > /tmp/mylogfile 2>&1 &";
    done
done
