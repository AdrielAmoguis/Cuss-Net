import csv
import random

txtPath = input("Input path to positive .txt file: ")

txt = open(txtPath, "r")
mainStr = txt.read()
lines = mainStr.split("\n")
txt.close()

# Add sentiment
sentiments = []
for line in lines:
    sentiments.append([line, "positive"])

txtPath = input("Input path to negative .txt file: ")

txt = open(txtPath, "r")
mainStr = txt.read()
lines = mainStr.split("\n")
txt.close()

# Add sentiment
for line in lines:
    sentiments.append([line, "negative"])

# Randomize the sentiments
doRandomize = input("Randomize list? [y/n]: ")
if doRandomize == 'y' or doRandomize == 'Y':
    random.shuffle(sentiments)

# Create CSV
csvPath = input("Input output .csv file path: ")
csvFile = open(csvPath, 'w', newline='', encoding='utf-8')
csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"')
csvWriter.writerows(sentiments)
csvFile.close()