#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

KILLXINUKSCRIPT="sudo killall java"

echo Killing Xinuk...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${KILLXINUKSCRIPT}"
    curl http://${HOSTNAME}:8000/clear
    echo .Xinuk killed on ${HOSTNAME}
done