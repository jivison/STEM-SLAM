#!/bin/bash

interval=600 #time interval between scans in seconds

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

    # data_dir="/home/mattecatte/STEM-SLAM/data/json"
    # remotehost="10.32.230.37"

    # rsync -avz -e 'ssh' $data_dir stem-server@$remotehost:/home/stem-server/SLAM_Data

    cd /home/mattecatte/STEM-SLAM/data/
    # Adding data to flat file database
    python3 add_json_to_csv.py

    # Jank, don't worry about it

    echo "#comment" >> /home/mattecatte/STEM-SLAM/visualization/visualize.py
    sed -i '$ d' /home/mattecatte/STEM-SLAM/visualization/visualize.py

    echo "Wating $interval seconds"

    while true; do
        
        current_time=$(date +%s)
        time_difference=$((current_time - init_time))

        echo "Current time:           $current_time"
        echo "Time difference:        $time_difference"

        if [[ $time_difference -ge $interval ]]; then
            echo Done waiting
            break
        fi

        sleep 3

    done



done