# (P3) Consider the probability distribution
#             { |x| when x in [-1, 1]
# X ~ f (x) = {
#             {  0  otherwise
# with a domain of [-2, 2]. Generate a set of samples from this distribution for a sample size of N = 100000 using
# rejection sampling, and construct the corresponding histogram. Plot the resulting histogram and the underlying
# probability density function.
import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return abs(x) if abs(x) <= 1 else 0


def rejectionsample():
    while True:
        x = random.uniform(-2, 2)
        y = random.uniform(0, 1)
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
