
# THE JSON FILES HAVE TO STAY IN THE SAME ORDER THAT THEY APPEAR IN THE CSV FILE HEADERS!!!!
# IT WILL NOT WORK IF YOU CHANGE THE ORDER

import json
import csv

import os

data = {}

processed_sensors = []

for file in os.listdir("/home/stem-server/SLAM_Data/"):
    if not file.endswith(".json"):
        print(f'WARNING: Non JSON file in json/ directory ({file})')
    else:
        with open(f'/home/stem-server/SLAM_Data/{file}', "r") as jsonfile:

            j = json.load(jsonfile)

            processed_sensors.append(j['sensor'])

            data.update(j['data'])

print(f'\nProcessed sensors: {processed_sensors}')

fieldnames = []

with open("/home/stem-server/STEM-SLAM/server_files/data/database.csv", "a+") as csvfile:

    reader = csv.DictReader(csvfile)

    for key in data:
        fieldnames.append(key)


    print("The csv headers are:\n")
    for fieldname in fieldnames:
        print(fieldname, end=",")
    print("\n")

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow(data)
