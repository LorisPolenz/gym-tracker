import requests
import csv
import pandas as pd
import time

print("[LOG] Script started")

locations = {
    "GymLocation1": "id",
    "GymLocation1": "id",
    # Append new values here
}


def writeCSV(csvRow):
    with open('./gym-data/gym-logs.csv', 'a', encoding='utf-8') as csvFile:

        csv_writer = csv.writer(
            csvFile, quoting=csv.QUOTE_MINIMAL, doublequote=True)

        csv_writer.writerow(csvRow)

        csvFile.close()


requestsMade = 0

csvHeader = ['timestamp', 'time', 'dayOfWeek']

for location in locations:
    csvHeader.append(location)

writeCSV(csvHeader)

while True:
    csvRow = []

    timestamp = pd.Timestamp.now()

    minute = "0%d" % timestamp.round("5T").minute
    hour = "0%d" % timestamp.hour

    currentTime = "%s:%s" % (hour[-2:], minute[-2:])

    csvRow.append(round(timestamp.timestamp()))
    csvRow.append(currentTime)
    csvRow.append(timestamp.weekday())

    for location in locations:

        requestsMade = requestsMade + 1

        response = requests.get(
            "<url to api with center id as %s>" % locations[location])

        csvRow.append(response.json()['<json_key_with_peoplecount>'])

    writeCSV(csvRow)

    print("[LOG] Requests made: %d Last update: %s" %
          (requestsMade, timestamp), end='\r', flush=True)

    time.sleep(300)
