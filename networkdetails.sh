#! /bin/bash/
while true; do

    TIME_OF_SCAN=`date +'%-M'`
    printf "################\nCounting devices\n################\n\n"
    
    cd /home/john/slam/devices; python3 devicecounter.py
    
    printf "##########################\nGathering ping information\n##########################\n\n"
    cd /home/john/slam/ping; python3 pingfinder.py

    printf "#############\nSpeedtest-ing\n#############\n\n"
    cd /home/john/slam/network-speed; python3 networkspeed.py

    echo "networkdetails.csv successfully updated, waiting 2 minutes"
    
    while true; do
        
        CURRENT_TIME=`date +'%-M'`
        TIME_DIFFERENCE="$(( CURRENT_TIME - TIME_OF_SCAN ))"

        if [ "$TIME_DIFFERENCE" -gt 3 ]; then
            break
        else
            sleep 1
        fi

    done

done