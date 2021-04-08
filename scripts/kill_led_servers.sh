#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

KILLLEDSERVERSCRIPT="sudo killall -9 node"

echo Killing all led servers...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${KILLLEDSERVERSCRIPT}"
    echo Sever killed on ${HOSTNAME}
done