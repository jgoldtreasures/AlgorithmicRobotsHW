# (P5) Consider a Gaussian distribution X ~ N(1, 0.5) with the domain of [-3, 3], generate its histogram h(X) using
# sample size of N = 100000. For any x element of X, there is a nonlinear transformation y = x^2, what is the histogram of
# Y? Show your results of the histogram of X and the histogram of Y. Set the sample size N = 1000, generate the
# histogram of X and the histogram of Y, then plot their corresponding density distribution based on the samples of
# X and Y (you can use ”line” function to mark the density distribution, an example is given below).

import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def f(x):
    return norm.pdf(x, 1, 0.5)


def rejectionsample():
    while True:
        x = random.uniform(-3, 3)
        y = random.uniform(0, 3)
        if y <= f(x):
            return x


def plot(num):
    data = [rejectionsample() for _ in range(num)]
    plt.hist(data, bins=25, density=True)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    pdf = [f(i) for i in x]
    plt.plot(x, pdf, linewidth=2)
    if num == 1000:
        plt.plot(data, [0.01] * len(data), '|')
    plt.show()
    filenamex = "./P5figures/Xhistogram_" + str(num)
    plt.savefig(filenamex)

    data = np.square(data)
    plt.hist(data, bins=25, density=True)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    pdf = [f(i) for i in x]
    plt.plot(x, pdf, linewidth=2)
    if num == 1000:
        plt.plot(data, [0.01] * len(data), '|')

    plt.show()

    filenamey = "./P5figures/Yhistogram_" + str(num)
    plt.savefig(filenamey)


def main():
    plot(100000)
    plot(1000)


if __name__ == '__main__':
    main()