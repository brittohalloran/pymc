import statistics
import time

import numpy as np
import scipy.stats as st
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
        start_time = time.time()
        s = []
        for _ in range(self.n):
            s.append(self.f())

        end_time = time.time()
        print(f"{self.n:,} simulations completed in {end_time - start_time:.1f} s")
        print(f"Mean    : {statistics.mean(s):8,.4f}")
        print(f"St. dev : {statistics.stdev(s):8,.4f}")
        print("")
        print("Percentiles:")
        print(f"5%  : {np.percentile(s, 5):,.4f}")
        print(f"10% : {np.percentile(s, 10):,.4f}")
        print(f"25% : {np.percentile(s, 25):,.4f}")
        print(f"50% : {np.percentile(s, 50):,.4f}")
        print(f"75% : {np.percentile(s, 75):,.4f}")
        print(f"90% : {np.percentile(s, 90):,.4f}")
        print(f"95% : {np.percentile(s, 95):,.4f}")

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
