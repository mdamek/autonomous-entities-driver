#!/usr/bin/bash
source $(dirname $0)/raspberry_hosts.sh

USERNAME="pi"

UPDATEXINUKSCRIPT="cd Desktop/xinuk;
git pull;"


if ! [ $# -eq 0 ] 
   then
    UPDATEXINUKSCRIPT="${UPDATEXINUKSCRIPT} sbt ${1}/assembly"
fi

echo Updating Xinuk...
echo $UPDATEXINUKSCRIPT
for HOSTNAME in ${RASPBERRYHOSTS[@]} ; do
    ssh -l ${USERNAME} ${HOSTNAME} ${UPDATEXINUKSCRIPT} "< /dev/null > /tmp/mylogfile 2>&1 &"
done
