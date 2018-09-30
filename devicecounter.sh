#! /bin/bash/

while true; do

    TIME_OF_SCAN=`date +'%-M'`
    echo "Running devicecounter.py"
    python3 devicecounter.py
    echo "devicehistory.csv successfully updated, waiting 2 minutes"
    
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