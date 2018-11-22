import json
import csv

json_path = "devicecount|ping|upload_speed|upload_speed|download_speed.json"
csv_path = "database.csv"

with open(json_path, "w+") as jsonfile:
    with open(csv_path, "a+") as csvfile:

        fieldnames = ["device_count", "avg_ping", "upload_speed", "download_speed"]
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            print(row)
