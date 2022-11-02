import csv
import json



def csvToJson(csv_path, json_path):
    jsonData = {}


    with open(csv_path, encoding="utf-8") as csvfile:

        csvData = csv.DictReader(csvfile)
        for rows in csvData:
            key = rows['Filename']
            jsonData[key] = rows

    with open(json_path,'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(jsonData, indent = 5))

csv_path = r'teamNames.csv'
json_path = r'jsonfile.json'

csvToJson(csv_path, json_path)

