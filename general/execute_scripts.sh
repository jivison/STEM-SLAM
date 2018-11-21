#!/bin/bash 

for script in "$@"; do
    python3 $script &
done

wait