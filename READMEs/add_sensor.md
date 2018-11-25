# Adding a sensor to the program

## Templating the code

The first step is to make sure your code is readable by the program. Under ```/controllers/```  you should find ```template.py```, which is a guideline for how your sensor code is set up. It looks like this:

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

As per the comment, it cannot contain spaces or special characters. Tr to keep it all lowercase.

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
Don't worry about changing the path at the bottom under ```with open(...``` 

### Step 6:
Save your new file under ```main.py```

## Adding your file to the file system

Under ```/sensors/```, add a new folder with the general name of what data you're collecting, eg. ```methane```.

Copy ```main.py``` to this new folder and you should be good to go.