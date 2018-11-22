
# THE JSON FILES HAVE TO STAY IN THE SAME ORDER THAT THEY APPEAR IN THE CSV FILE HEADERS!!!!
# IT WILL NOT WORK IF YOU CHANGE THE ORDER

import json
import csv

import os

data = {}

processed_sensors = []

for file in os.listdir("json/"):
    if not file.endswith(".json"):
        print(f'WARNING: Non JSON file in json/ directory ({file})')
    else:
        with open(f'json/{file}', "r") as jsonfile:

            j = json.load(jsonfile)

            processed_sensors.append(j['sensor'])

            data.update(j['data'])

print(f'\nProcessed sensors: {processed_sensors}')

fieldnames = []

with open("database.csv", "a+") as csvfile:

    reader = csv.DictReader(csvfile)

    for key in data:
        fieldnames.append(key)


    print("The csv headers are:\n")
    for fieldname in fieldnames:
        print(fieldname, end=",")
    print("\n")

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow(data)
