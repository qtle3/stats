""" This module implements simple statistics functions. """

from math import sqrt


def getNumbers():
    """This function gets numbers from a user and returns it in a list."""
    nums = []  # start with an empty list

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)  # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums


def mean(nums):
    """This function takes a list of numbers as a parameter
    and returns the mean."""
    sum = 0.0  # initialize the sum to 0
    for num in nums:
        sum = sum + num  # increment the sum
    return sum / len(nums)


def stdDev(nums, xbar):
    """This function takes a list of numbers and a mean as parameters
    and returns the sample standard deviation."""
    sumDevSq = 0.0  # initialize the sum of deviation squares to 0
    for num in nums:
        dev = xbar - num  # deviation from mean
        sumDevSq = sumDevSq + dev * dev  # increment
    return sqrt(sumDevSq / (len(nums) - 1))


def median(nums):
    """This function takes a list of numbers as a paremeter
    and returns the median."""
    nums.sort()  # sort the numbers
    size = len(nums)
    midPos = size // 2  # middle position (by integer division by 2)
    if size % 2 == 0:  # even
        median = (nums[midPos] + nums[midPos - 1]) / 2
    else:  # odd
        median = nums[midPos]
    return median


def geometricMean(nums):
    m = 1
    n = len(nums)
    for i in nums:
        m = m * i
    geometric_mean = m ** (1 / n)
    print("Geometric Mean is: " + str(geometric_mean))
