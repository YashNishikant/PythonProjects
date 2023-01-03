import matplotlib.pyplot as plt
import csv

xpoints = []
ypoints = []

with open('CSVExample.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        xpoints.append(int(line[0]))
        ypoints.append(int(line[1]))

plt.plot(xpoints, ypoints)
plt.show()