#!/usr/bin/bash
source raspberry_hosts.sh

USERNAME="pi"

RUNLEDSERVERSCRIPT="cd Desktop/simulation-platform-for-autonomous-entities;
sudo npm run start < /dev/null > /tmp/mylogfile 2>&1 &"

echo Running all led servers...

for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${RUNLEDSERVERSCRIPT}"
    echo Led server started on ${HOSTNAME}
done


