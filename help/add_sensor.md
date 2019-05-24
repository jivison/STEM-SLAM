# Adding a sensor to the program

## Getting the code

To grab all the code, type in the terminal (CTRL + ALT + T):
```bash
git clone https://github.com/MatteCatte/STEM-SLAM
```
This will download all of the files to a directory called ```STEM-SLAM```. You will find everything you need under either ```raspberry_files``` or ```templates```.


## Templating the code

The first step is to make sure your code is readable by the program. Under ```/templates/```  you should find ```template.py```, which is a guideline for how your sensor code is set up. It looks like this:

Please, don't edit this file, copy/paste it instead.

```python
import json

sensor = "Sample Sensor" # Whatever the sensor is called

# replace spaces with underscores and keep it all lowercase. This will make things more consistent with file names 
data_type = "sample_data"
print("Gathering {} from sensor {}\n".format(data_type, sensor))


def run():
    # YOUR CODE HERE

    # Must return the value like the following:

    sample_data = 100

    return str(sample_data)


# Sample data structure. You must adhere to Python dictionary notation
# Replace spaces with underscores

# If you need multiple data points, please see me

data = {
    # Don't change this one
    'sensor' : sensor,

    'data' : {
        data_type : run(), 
    }
}

# Make sure to update this path if it should need changing
with open("/home/mattecatte/STEM-SLAM/data/json/{}.json".format(data_type), "w+") as outfile:
    json.dump(data, outfile)

print("Finished gathering {} from sensor {} \n".format(data_type, sensor))
```

### Step 1:
Change ```sensor``` to whatever your sensor is called, eg. ```MQ7```.

### Step 2: 
Change ```data_type``` to the data type your sensor will be producing, examples include: &nbsp;methane_levels, networkdetails, or noise_level.

As per the comment, it cannot contain spaces or special characters. Try to keep it all lowercase.

### Step 3:
Add your code!

Under 
```python
def run():
```
replace ```# YOUR CODE HERE``` with your sensor code. Make sure to move any ```include```s outside of the function definition, preferably above or below ```import json```

If you have any extra functions, make sure to move those outside of 
```python
def run():
```
as well.

### Step 4:
We have to make sure that the code writes the right data to the JSON file, so change ```sample_data``` to equal the output of your sensor. For example:

```python
import sensor

def run():

    sensor_data = sensor.get_value(now)

    return str(sensor_data)

```

### Step 5:
You need to change the path under ```with open():```.
Change this to ```/home/<hostname>/sensor_data/{}.json```

(Change ```<hostname>``` to your actual hostname, which you can get by typing ```hostname``` in terminal)

### Step 6:
Save your new file under ```main.py```
It will NOT work if called another name.

### Step 7:
Create a new folder under the home directory called ```sensor``` and move ```main.py``` as well as any other files you may need into this new folder.

## Setting up the file system on the Pi

For the program to run correctly, we need to correctly set up the filesystem so the program knows where to find something.

Open terminal and, under the home directory, (type ```cd ``` to get there), create a folder called ```sensor_data``` (```mkdir sensor_data```). 

This directory will hold the data temporarily.

&nbsp;

## Editing paths and stuff.

### send_data.sh

First, edit the file ```~/STEM-SLAM/raspberry_files/send_data.sh```. It should look like this:

```bash
#!/bin/bash

data_file="/home/pi/sensor_data/data.json"
ip="/home/pi/sensor_data/ip"

remotehost="10.32.230.37"

rsync -avz -e 'ssh' $data_file stem-server@$remotehost:/home/stem-server/SLAM_Data/
rsync -avz -e 'ssh' $ip stem-server@$remotehost:/home/stem-server/raspberryIPs/
```

Under the variable ```data_file```, change ```data.json``` to ```data_type.json``` where data_type is whatever you put under data_type in the python file.

## Once you are done all of this,

Tell me your IP address (by running ```hostname -I```), and everything should be good to go.