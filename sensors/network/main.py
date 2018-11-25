import json

import networkspeed
import pingfinder
import devicecounter

ip = "192.168.0"

sensor = "Network Sensor" # Whatever the sensor is called

# replace spaces with underscores and keep it all lowercase. This will make things more consistent with file names 
data_type = "networkdetails"
print("Gathering {} from sensor {}\n".format(data_type, sensor))


def run(operation):
    if operation == 'device_count':
        return devicecounter.run(ip)

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
        'device_count'   :  run('device_count'),
        'avg_ping'       :  run('ping'), 
        'upload_speed'   :  run('uploadspeed'),
        'download_speed' :  run('downloadspeed')
    }

}


with open("../../data/json/{}.json".format(data_type), "w+") as outfile:
    json.dump(data, outfile)

print("Finished gathering {} from sensor {} \n".format(data_type, sensor))
