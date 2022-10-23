import csv

import matplotlib.pyplot as plt
import numpy as np

listX = []
listY = []

with open('CSVExample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        listX.append(line[0])
        listY.append(line[1])


xpoints = np.array(listX)
ypoints = np.array(listY)
plt.plot(xpoints, ypoints)
plt.show()




