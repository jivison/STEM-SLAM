#! /bin/bash/

Infinite while
    TIME_OF_SCAN=$TIME #(or smth idk)
    python3 devicecounter.py
    while [[ $TIME - $TIME_OF_SCAN > 5 ]]; do
        :
    done