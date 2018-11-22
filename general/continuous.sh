#!/bin/bash

interval=60 #time interval between scans in seconds

# This doesn't work

while :
do
    # unix time
    init_time=$(date +%s)

    echo "Executing scripts"

    for dir in "$@"; do
        cd $dir

        python3 main.py &

    done

    wait

    echo "Sending data"

    data_dir="/home/mattecatte/STEM-SLAM/data"
    remotehost="10.32.230.37"

    rsync -avz -e 'ssh' $data_dir stem-server@$remotehost:/home/stem-server/SLAM_Data

    echo "Wating $interval seconds"

    while true; do
        
        current_time=$(date +%s)
        time_difference=$((init_time - current_time))

        if [[ $time_difference -ge $interval ]]; then
            break
        fi

    done

    echo 'Done waiting'

done