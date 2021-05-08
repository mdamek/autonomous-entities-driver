#!/usr/bin/bash

RASPBERRIES=()
jq -c '.config.hosts | .[]' ../simulations.json | while read i; do
    echo ${i}
    RASPBERRIES+=(${i})
done

for HOSTNAME in ${RASPBERRIES[@]} ; do
    echo "asdsad" ${HOSTNAME}

done

RASPBERRY1="192.168.1.87"
RASPBERRY2="192.168.1.172"
RASPBERRY3="192.168.1.205"
RASPBERRY4="192.168.1.196"

RASPBERRYHOSTS=($RASPBERRY1 $RASPBERRY2 $RASPBERRY3 $RASPBERRY4)