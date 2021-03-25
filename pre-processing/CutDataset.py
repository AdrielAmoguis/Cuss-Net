import csv
from os import write
import random

csv1 = open(input("Enter filepath for first dataset: "), "r")

csvData = []

# Read List
reader = csv.reader(csv1, delimiter=",")
for row in reader:
    csvData.append(row)

csv1.close()

print("This dataset has {} entries.".format(len(csvData)))
upperLimit = int(input("Take how many entries from this dataset?: "))

# Take randomly
cutList = []
while(len(cutList) < upperLimit):
    e = random.choose(csvData)
    if not e in cutList:
        cutList.append(e)

# Write Data to CSV
writeFile = open(input("Output file path: "), 'w', newline='', encoding='utf-8')
writer = csv.writer(writeFile, delimiter=',', quotechar='"')
writer.writerows(cutList)
writeFile.close()