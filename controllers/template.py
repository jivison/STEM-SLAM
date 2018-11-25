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
