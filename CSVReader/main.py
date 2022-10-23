import csv

with open('a1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    counter = 0

    for line in csv_reader:
        if float(line[1]) >= 5.0:
            print(line[0] + "\t\t" + line[1])
            counter = counter + 1

print(counter)
