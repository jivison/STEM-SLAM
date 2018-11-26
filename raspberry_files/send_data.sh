#!/bin/bash

data_file="/home/pi/sensor_data/data.json"
ip="/home/pi/sensor_data/ip"

remotehost="10.32.230.37"

rsync -avz -e 'ssh' $data_file stem-server@$remotehost:/home/stem-server/SLAM_Data/
rsync -avz -e 'ssh' $ip stem-server@$remotehost:/home/stem-server/raspberryIPs/