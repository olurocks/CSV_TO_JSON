import csv
import json
import hashlib



def csvToJson(csv_path, json_path):
    jsonData = []


    with open(csv_path, encoding="utf-8") as csvfile:

        csvData = csv.DictReader(csvfile)

        for rows in csvData:
            jsonData.append(rows)

    with open(json_path,'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(jsonData, indent = 5))

csv_path = r'teamNames.csv'
json_path = r'jsonfile.json'

csvToJson(csv_path, json_path)


#find SHA256 hexadecimal of json file and append to output.csv

def sha256Calc(fileName):
    with open(fileName,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        return readable_hash


json_sha256=sha256Calc(json_path)
new_file = r'output.csv'
i = 0

with open(csv_path,'r') as origFile:
    with open(new_file,'w') as newFile:

        lineList = []
        for line in origFile:
            strippedLine = line.strip()
            lineList = strippedLine.split(',')

            lineList.append(json_sha256)
            lineStr = str(lineList)
            lineStr = lineStr.replace("'", "").replace("[","").replace("]","")
            lineStr = lineStr

            newFile.write(lineStr)
            newFile.write('\n') #Insert a new line
            i += 1
