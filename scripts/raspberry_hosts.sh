#!/usr/bin/bash
declare -a RASPBERRIES
jq -c '.config.hosts | .[]' ../simulations.json | while read i; do
    RASPBERRIES[${#RASPBERRIES[@]}]=${i}
    dsa=${i}
    echo ${i}
done
echo ${dsa}
echo "SS"

echo ${#RASPBERRIES[@]}

RASPBERRY1="192.168.1.87"
RASPBERRY2="192.168.1.172"
RASPBERRY3="192.168.1.205"
RASPBERRY4="192.168.1.196"

RASPBERRYHOSTS=($RASPBERRY1 $RASPBERRY2 $RASPBERRY3 $RASPBERRY4)