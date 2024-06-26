import math
from statistics import mean

import matplotlib.pyplot as plt
import numpy as npy

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]

y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]

y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]

y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]


def correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    numerator = sum(npy.multiply((x - mean_x), (y - mean_y)))
    denominator = math.sqrt(sum(npy.power(x - mean_x, 2)) * sum(npy.power(y - mean_y, 2)))

    return numerator / denominator


def regression(x, y, a):
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum(npy.multiply((x - mean_x), (y - mean_y)))
    denominator = sum(npy.power(x - mean_x, 2))

    b1 = numerator / denominator
    b0 = mean_y - b1 * mean_x

    return b0, b1


def demo(x, y, a):
    b0, b1 = regression(x, y, a)
    r = correlation(x, y)
    plt.title("Correlação: " + str(r) + " B0: " + str(b0) + " B1: " + str(b1))
    plt.scatter(x, y)
    plt.plot(a, b0 + b1 * a)
    plt.show()


demo(npy.array(x1), npy.array(y1), npy.array(x1))
demo(npy.array(x2), npy.array(y2), npy.array(x2))
demo(npy.array(x3), npy.array(y3), npy.array(x3))
