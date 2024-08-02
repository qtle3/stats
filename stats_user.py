""" This program uses the stats.py statistics module. """

import stats_calculations


def main():
    print("This program computes mean, median and standard deviation.")
    data = stats_calculations.getNumbers()
    xbar = stats_calculations.mean(data)
    std = stats_calculations.stdDev(data, xbar)
    med = stats_calculations.median(data)
    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)


main()
