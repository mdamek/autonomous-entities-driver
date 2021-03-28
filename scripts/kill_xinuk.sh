#!/usr/bin/bash
source raspberry_hosts.sh

USERNAME="pi"

KILLXINUKSCRIPT="sudo killall java"

echo Killing Xinuk...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${KILLXINUKSCRIPT}"
    echo Xinuk killed on ${HOSTNAME}
done