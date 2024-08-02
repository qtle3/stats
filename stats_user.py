""" This program uses the stats.py statistics module. """

import stats_calculations as stats
from stats_calculations import getNumbers, mean, stdDev, median, mode, geometricMean


def main():
    print("This program computes mean, median and standard deviation.")
    data = stats.getNumbers()
    xbar = stats.mean(data)
    std = stats.stdDev(data, xbar)
    med = stats.median(data)
    mode = stats.mode(data)
    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)


main()
