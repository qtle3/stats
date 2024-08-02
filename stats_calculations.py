""" This module implements simple statistics functions. """

from math import sqrt
from collections import Counter
import statistics


def getNumbers():
    """This function gets numbers from a user and returns it in a list."""
    while True:
        try:
            numbers = input("Enter a list of numbers separated by spaces: ")
            num_list = [float(num) for num in numbers.split()]
            if not num_list:
                print("Please enter a valid list of numbers.")
            return num_list
        except ValueError as e:
            print("Please enter a valid list of numbers.")


def mean(numbers):
    """This function takes a list of numbers as a parameter
    and returns the mean."""
    return sum(numbers) / len(numbers)


def variance(numbers):
    """This function takes a list of numbers as a parameter
    and returns the variance."""
    xbar = mean(numbers)
    sumDevSq = 0.0  # initialize the sum of deviation squares to 0
    for num in numbers:
        dev = xbar - num  # deviation from mean
        sumDevSq = sumDevSq + dev * dev  # increment
    return round(sumDevSq / (len(numbers) - 1), 3)


def stdDev(numbers):
    """This function takes a list of numbers and a mean as parameters
    and returns the sample standard deviation."""
    return round(sqrt(variance(numbers)), 3)


def quick_select(numbers, k):
    """This function takes a list of numbers and an index k as parameters
    and returns the kth smallest element in the list."""
    if len(numbers) == 1:
        return numbers[0]
    pivot = numbers[len(numbers) // 2]
    less = [i for i in numbers if i < pivot]  # all elements less than the pivot
    greater = [i for i in numbers if i > pivot]  # 3 all elements greater than the pivot
    equal = [i for i in numbers if i == pivot]  # all elements equal to the pivot
    if k < len(less):
        return quick_select(less, k)
    elif k < len(less) + len(equal):
        return equal[0]
    else:
        return quick_select(greater, k - len(less) - len(equal))


def median(numbers):
    """This function takes a list of numbers as a paremeter
    and returns the median."""
    size = len(numbers)
    if size == 0:
        raise ValueError("list is empty, median requires at least one data point")

    if size % 2 == 1:
        return quick_select(numbers, size // 2)
    else:
        return (
            quick_select(numbers, size // 2 - 1) + quick_select(numbers, size // 2) / 2
        )


def mode(numbers):
    """This function takes a list of numbers as a parameter
    and returns the mode."""
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return "No unique mode found"


def geometricMean(numbers):
    m = 1
    n = len(numbers)
    for i in numbers:
        m = m * i
    geometric_mean = m ** (1 / n)
    print("Geometric Mean is: " + str(geometric_mean))
