import matplotlib.pyplot as plt
import numpy as np
from numpy.lib import twodim_base


def first():
    n = np.linspace(1, 100)
    plt.plot(n, 7 * n * n + 6 * n + 5)
    plt.show()


def second():
    n = np.linspace(1, 100)
    plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    plt.plot(n, 20 * n, label="20n")
    plt.legend(loc="upper left")
    plt.show()


def third():
    n = np.linspace(1, 5)
    plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    plt.plot(n, 7 * n * n, label="7n^2")
    plt.legend(loc="upper left")
    plt.show()


def fourth():
    n = np.linspace(1, 100)
    plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    plt.plot(n, 7 * n * n, label="7n^2")
    plt.legend(loc="upper left")
    plt.show()


def fifth():
    n = np.linspace(1, 100)
    plt.plot(n, (7 * n * n + 6 * n + 5) / (7 * n * n))
    plt.show()


def six():
    n = np.linspace(1, 10)
    plt.plot(n, n, label="n")
    plt.plot(n, n**2, label="n²")
    plt.plot(n, n**3, label="n³")
    plt.legend(loc="upper left")
    plt.show()


def seven():
    n = np.linspace(1, 100)
    plt.plot(n, n, label="n")
    plt.plot(n, n**2, label="n²")
    plt.plot(n, n**3, label="2^n")
    plt.legend(loc="upper left")
    plt.show()


def eigth():
    n = np.linspace(1, 10)
    plt.plot(n, n**3, label="n³")
    plt.plot(n, 2**n, label="2^n")
    plt.legend(loc="upper left")
    plt.show()


def nine():
    n = np.linspace(1, 20)
    plt.plot(n, n**4, label="n⁴")
    plt.plot(n, 2**n, label="2^n")
    plt.legend(loc="upper left")
    plt.show()


def ten():
    n = np.linspace(1, 20)
    plt.plot(n, n, label="n")
    plt.plot(n, np.log(n), label="log n")
    plt.legend(loc="upper left")
    plt.show()


def eleven():
    n = np.linspace(1, 100)
    plt.plot(n, n**0.5, label="n^.5")
    plt.plot(n, np.log(n) ** 3, label="(log n) ^ 3")
    plt.legend(loc="upper left")
    plt.show()


def twelve():
    n = np.linspace(1, 10**6)
    plt.plot(n, n**0.5, label="n^.5")
    plt.plot(n, np.log(n) ** 3, label="(log n) ^ 3")
    plt.legend(loc="upper left")
    plt.show()


def thirteen():
    n = np.linspace(1, 10**8)
    plt.plot(n, n**0.5, label="n^.5")
    plt.plot(n, np.log(n) ** 3, label="(log n) ^ 3")
    plt.legend(loc="upper left")
    plt.show()


def fourteen():
    n = np.linspace(1, 10**120)
    plt.plot(n, n**0.5, label="n^.5")
    plt.plot(n, np.log(n) ** 3, label="(log n) ^ 3")
    plt.legend(loc="upper left")
    plt.show()


if __name__ == "__main__":
    first()
    second()
    third()
    fourth()
    fifth()
    six()
    seven()
    eigth()
    nine()
    ten()
    eleven()
    twelve()
    thirteen()
    fourteen()
