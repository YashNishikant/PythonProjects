import csv

names1 = []
names2 = []

with open('Y2YAttendance.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        names1.append(line[0] + " " + line[1])

with open('PTPY2Y.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        names2.append(line[1] + " " + line[0])

for a in names1:
    for b in names2:
        if a.__eq__(b):
            print(a)