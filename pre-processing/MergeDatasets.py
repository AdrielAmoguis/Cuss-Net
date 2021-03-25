import csv
import random

csv1 = open(input("Enter filepath for first dataset: "), "r")
csv2 = open(input("Enter filepath for second dataset: "), "r")

csvData1 = []
csvData2 = []

# Read List
reader = csv.reader(csv1, delimiter=",")
for row in reader:
    csvData1.append(row)

reader = csv.reader(csv2, delimiter=",")
for row in reader:
    csvData2.append(row)

csv1.close()
csv2.close()

masterCSV = csvData1 + csvData2

if input("Randomize master CSV list? [y/n]: ").lower() == 'y':
    random.shuffle(masterCSV)

# Write CSV
csvMasterFile = open(input("Enter output file path: "), 'w', newline='', encoding='utf-8')
writer = csv.writer(csvMasterFile, delimiter=',', quotechar='"')
writer.writerows(masterCSV)
csvMasterFile.close()