#!/bin/bash

interval=300 #time interval between scans in seconds

while :
do
    # unix time
    init_time=$(date +%s)

    echo "Executing scripts"

    ansible-playbook -i /home/stem-server/STEM-SLAM/server_files/controls/ansible/SLAM-hosts /home/stem-server/STEM-SLAM/server_files/controls/ansible/gatherData.yaml

    cd /home/stem-server/STEM-SLAM/server_files/data/
    # Adding data to flat file database
    python3 /home/stem-server/STEM-SLAM/server_files/data/add_JSON_to_database.py

    # Jank, don't worry about it

    echo "#comment" >> /home/stem-server/STEM-SLAM/server_files/data/visuals/generate_visuals.py
    sed -i '$ d' /home/stem-server/STEM-SLAM/server_files/data/visuals/generate_visuals.py

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
