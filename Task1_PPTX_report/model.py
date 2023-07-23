import csv
import json


with open("sample.json") as file:
    json_data = json.load(file)


with open("sample.csv") as file:
    csvRead = csv.reader(file, delimiter=';')
    csv_data = list(csvRead)


