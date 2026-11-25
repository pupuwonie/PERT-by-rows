import csv

def file(data):
    with open(data, mode = 'r') as file:
        csvFile = csv.reader(file)

        for i in csvFile:
            print(i)
