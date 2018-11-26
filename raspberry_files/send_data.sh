#!/bin/bash

data_dir="/home/mattecatte/STEM-SLAM/data"
remotehost="10.32.230.37"

# scp -r stem-server@$remotehost:/home/stem-server/SLAM_Data/ $data_dir

rsync -avz -e 'ssh' $data_dir stem-server@$remotehost:/home/stem-server/SLAM_Data