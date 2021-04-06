#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

UPDATELEDSERVERSCRIPT="cd Desktop/simulation-platform-for-autonomous-entities;
git pull"

echo Updating led servers...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${UPDATELEDSERVERSCRIPT}"
done
