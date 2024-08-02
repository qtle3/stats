""" This program uses the stats.py statistics module. """

import stats_calculations as stats
from stats_calculations import (
    getNumbers,
    mean,
    stdDev,
    median,
    mode,
    geometricMean,
    variance,
)


def main():
    print("This program computes basic statistics for a list of numbers.")

    # get the numbers from the user
    data = stats.getNumbers()
    xbar = stats.mean(data)
    variance = stats.variance(data)
    std = stats.stdDev(data)
    med = stats.median(data)
    mode = stats.mode(data)
    geometricMean = stats.geometricMean(data)

    # display the results
    print("\nThe mean is", xbar)
    print("The median is", med)
    print("The mode is", mode)
    print("The variance is", variance)
    print("The standard deviation is", std)
    print("The geometric mean is", geometricMean)


main()
