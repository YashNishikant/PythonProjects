import matplotlib.pyplot as plt
import numpy as np


def scatterPlot():
    countries = ['Brazil', 'Madagascar', 'S. Korea', 'United States',
                 'Ethiopia', 'Pakistan', 'China', 'Belize']
    birth_rate = [16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0]
    life_expectancy = [73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7]
    population = np.array([214, 28, 51, 331, 117, 225, 1412, 1])

    # Figure is our window and graph. (The figure of whats in our window)
    fig = plt.figure()
    ax = fig.add_subplot(111)  # just alignment. 111 is the center
    # ex. 221 is the top left.

    # Some random colours:
    # Range gives us the sequence of numbers.
    # The sequence is the length of the countries array.
    # We want a different random color for each country.
    # c and s are optional parameters, but must be named this way
    colours = range(len(countries))
    ax.scatter(birth_rate, life_expectancy, c=colours, s=population)

    # Set limits
    ax.set_xlim(5, 45)
    ax.set_ylim(60, 85)

    # Labels
    ax.set_xlabel('Birth rate per 1000 population')
    ax.set_ylabel('Life expectancy at birth (years)')

    # Loop to space out our text
    # We loop through multiple lists at once
    # va is vertical alignment
    offset = 1
    for x, y, s, country in zip(birth_rate, life_expectancy, population, countries):
        ax.text(x + offset, y, country + ' - ' + str(s), va='center')

    plt.show()


def heatmapPlot():
    # Declare your arrays
    states = ["New Jersey", "Arizona", "Virginia", "California",
              "Nevada", "Florida", "Hawaii"]
    years = ["2017", "2018", "2019",
             "2020", "2021", "2022", "2023"]

    # create your value table
    values = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                       [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                       [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                       [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                       [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                       [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                       [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

    # get axis value from the tuple from subplots()
    fig, ax = plt.subplots()
    ax.imshow(values)

    # Show all ticks and label them with the respective list entries
    # np.arange gives us a list of evenly spaced values between an interval.
    # Takes our array and gives evenly spaced intervals between the first and last index
    ax.set_xticks(np.arange(len(years)), years)
    ax.set_yticks(np.arange(len(states)), states)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(states)):
        for j in range(len(years)):
            ax.text(j, i, values[i, j], ha="center", va="center", color="w")

    # Title
    ax.set_title("Annual Temperatures of States")
    plt.show()


scatterPlot()
heatmapPlot()
