import numpy as np
import scipy.stats as st
import statistics
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


class Simulation:
    """
    Creates a Monte Carlo simulation object which takes in a sampling function 
    f and can be run. 
    """

    def __init__(self, f, n=20000):
        self.f = f
        self.n = n

    @property
    def s(self) -> float:
        return self.f()

    def run(self, plot=True):
        s = []
        for _ in range(self.n):
            s.append(self.f())

        print("{} simulations completed...".format(self.n))
        print("Mean: ", statistics.mean(s))
        print("St. dev: ", statistics.stdev(s))
        if plot:
            sns.distplot(s, kde=False, norm_hist=True)
            plt.show()


class Norm:
    """
    Creates a random input variable which follows a normal distribution
    Either supply 90% confidence bounds or a mean and standard deviation
    """

    def __init__(
        self,
        mean: float = None,
        sd: float = None,
        interval: tuple = None,
        proportion: float = 0.90,
    ):
        if interval != None and mean == None and sd == None:
            if len(interval) != 2:
                raise Exception("Interval should be a 2-tuple.")
            self.mean = statistics.mean(interval)
            rng = max(interval) - min(interval)
            z = st.norm.ppf(1 - (1 - proportion) / 2)
            self.sd = rng / (2 * z)
        elif mean != None and sd != None and interval == None:
            self.mean = mean
            self.sd = sd
        else:
            raise Exception(
                "Either supply interval endpoints or mean and sd, but not both."
            )

    @property
    def s(self) -> float:
        return np.random.normal(loc=self.mean, scale=self.sd)


class Binom:
    """
    Creates a random binomial variable which outputs 1 or 0. Probability p is
    the probability of getting 1. 
    """

    def __init__(self, p=0.5):
        self.p = p

    @property
    def s(self) -> float:
        return np.random.binomial(n=1, p=self.p)
