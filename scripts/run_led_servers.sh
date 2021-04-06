#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

RUNLEDSERVERSCRIPT="cd Desktop/simulation-platform-for-autonomous-entities;
sudo npx ts-node -T Server/app.ts < /dev/null > /tmp/mylogfile 2>&1 &"

echo Running all led servers...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${RUNLEDSERVERSCRIPT}"
    echo Led server started on ${HOSTNAME}
done


