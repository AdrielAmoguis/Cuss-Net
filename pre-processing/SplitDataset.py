import csv
import random

print("This is meant to split the dataset equally into training and test datasets.")

datasetCSV = open(input("Dataset file path: "), 'r')
reader = csv.reader(datasetCSV)

data = []
for row in reader:
    data.append(row)

random.shuffle(data)
mid = len(data) // 2

firstHalf = data[:mid]
secondHalf = data[mid:]

# Write to separate CSV files
firstHalfCSV = open(input("First output file path: "), 'w', newline='', encoding='utf-8')
writer = csv.writer(firstHalfCSV, delimiter=',', quotechar='"')
writer.writerows(firstHalf)
firstHalfCSV.close()

secondHalfCSV = open(input("Second output file path: "), 'w', newline='', encoding='utf-8')
writer = csv.writer(secondHalfCSV, delimiter=',', quotechar='"')
writer.writerows(secondHalf)
firstHalfCSV.close()