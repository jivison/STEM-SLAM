import json
import random

sensor = "MQ5" # Whatever the sensor is called

# replace spaces with underscores and keep it all lowercase. This will make things more consistent with file names 
data_type = "methane_levels"
print("Gathering {} from sensor {}\n".format(data_type, sensor))


def run():
    # YOUR CODE HERE

    # Must return the value like the following:

    sample_data = random.randint(700, 1005)

    return str(sample_data)


# Sample data structure. You must adhere to Python dictionary notation
# Replace spaces with underscores

# If you need multiple data points, please see me

data = {
    # Don't change this one
    'sensor' : sensor,

    'data' : {
        # Change singular_data_point to your data type, eg. device_count, methane_levels
        data_type : run(), 
    },

    # Change this to the appropriate units
    'units' : 'ppm'
}

# '../' points to the parent directory. Make sure to update this path if it should need changing
with open("/home/mattecatte/STEM-SLAM/data/json/{}.json".format(data_type), "w+") as outfile:
    json.dump(data, outfile)

print("Finished gathering {} from sensor {} \n".format(data_type, sensor))
