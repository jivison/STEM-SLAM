# Running the program

To ensure SLAM is functioning correctly, ensure the following:

### **Raspberry Pi**
- The Pi is plugged in to power
- The Pi is plugged into Ethernet, it will not work on WiFi
- The Arduino and sensors are plugged into the Pi

*No programs need to be run on the Pi itself, as long as everything is connected and plugged in the server should do everything*

### **The server**
- The computer is on
- The computer is plugged into Ethernet, it will not work on WiFi
- You then have to run the following commands;
```bash
cd ~/STEM-SLAM/server_files/; bash SLAM_Cycle.sh
cd data/visuals; python generate_visuals.py
```
Then, open a new firefox tab, and enter the following into the URL bar:

```http://127.0.0.1:8050/```

This should open the display.

If you have errors with ```SLAM_Cycle.sh```, try checking the connections to the Pi and server.
