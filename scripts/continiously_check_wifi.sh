#!/bin/bash

while true ; do
	if ifconfig wlan0 | grep "inet addr:" ; then
		sleep 60
	else
		echo "Network connection down! Attempting reconnection."
		ifup --force wlan0
		sleep 10
	fi
done