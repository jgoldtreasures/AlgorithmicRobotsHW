# (P4) Consider a mixture of two Gaussians, fx = p1 * f1 + p2 * f2, where p1 = 0.3, p2 = 0.7 and f1 ~ N(0, 1), f2 ~
# N(2, 0.5), with the domain of [-5, 5]. Generate the samples from this distribution using the sample size of
# N = 100000, then construct the resulting histogram. Plot the resulting histogram and the underlying probability
# density function.

import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def f(x):
    return 0.7 * norm.pdf(x, 0, 1) + 0.3 * norm.pdf(2, 0.5)


def rejectionsample():
    while True:
        x = random.uniform(-5, 5)
        y = random.uniform(0, 5)
        if y <= f(x):
            return x


def plot(num):
    data = [rejectionsample() for _ in range(num)]
    plt.hist(data, bins=25, density=True)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    pdf = [f(i) for i in x]
    plt.plot(x, pdf, linewidth=2)

    plt.show()
    filename = "./P3figures/histogram_" + str(num)
    print(filename)
    plt.savefig(filename)


def main():
    plot(100000)


if __name__ == '__main__':
    main()
