import json

import networkspeed
import pingfinder
import devicecounter

sensor = "Raspberry Pi" # Whatever the sensor is called

# replace spaces with underscores and keep it all lowercase. This will make things more consistent with file names 
data_type = "devicecount|ping|upload_speed|download_speed"
print("Gathering {} from sensor {}\n".format(data_type, sensor))


def run(operation):
    if operation == 'device_count':
        return devicecounter.run()

    elif operation == 'ping':
        return pingfinder.run()

    elif operation == 'uploadspeed':
        return networkspeed.upload()

    elif operation == 'downloadspeed':
        return networkspeed.download()


# Sample data structure. You must adhere to Python dictionary notation
# Replace spaces with underscores

# If you need multiple data points, please see me

data = {
    'sensor' : sensor,

    'data': {
        'device_count'   :  run('device_count') + " devices",
        'avg_ping'       :  run('ping') + " ms", 
        'upload_speed'   :  run('uploadspeed') + " mbps",
        'download_speed' :  run('downloadspeed') + " mbps"
    }

}


with open("../data/{}.json".format(data_type), "w+") as outfile:
    json.dump(data, outfile)

print("Finished gathering {} from sensor {} \n".format(data_type, sensor))
