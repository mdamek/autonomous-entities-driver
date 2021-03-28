#!/usr/bin/bash
source raspberry_hosts.sh

USERNAME="pi"

KILLLEDSERVERSCRIPT="sudo killall node"

echo Killing all led servers...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${KILLLEDSERVERSCRIPT}"
    echo Sever killed on ${HOSTNAME}
done