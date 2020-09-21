# (P1) Consider a Gaussian distribution X ~ N(0, 1). Generate 3 different set of samples from this distribution for
# each of the three sample sizes N = 100, N = 1000, and N = 100000, and construct the corresponding histograms.
# Plot the resulting histograms and the underlying probability density function.


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def plotNormal(num):
    data = norm.rvs(0, 1, num)
    plt.hist(data, bins=25, density=True)

    mean, std = norm.fit(data)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2)

    plt.show()
    filename = "./P1figures/histogram_" + str(num)
    print(filename)
    plt.savefig(filename)


def main():
    plotNormal(100)
    plotNormal(1000)
    plotNormal(100000)


if __name__ == '__main__':
    main()
