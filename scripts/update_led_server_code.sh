#!/usr/bin/bash
source raspberry_hosts.sh

USERNAME="pi"

UPDATELEDSERVERSCRIPT="cd Desktop/simulation-platform-for-autonomous-entities;
git pull"

echo Updating led servers...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${UPDATELEDSERVERSCRIPT}"
done
