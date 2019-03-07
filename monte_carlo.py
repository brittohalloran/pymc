import numpy as np
import scipy.stats as st
import statistics


class RandomVariable:
    """
    Creates a random input variable which follows a normal distribution
    Either supply 90% confidence bounds or a mean and standard deviation
    """

    def __init__(
        self,
        mean: float = None,
        sd: float = None,
        interval: tuple = None,
        interval_proportion: float = 0.90,
    ):
        if interval != None and mean == None and sd == None:
            if len(interval) != 2:
                raise Exception("Interval should be a 2-tuple.")
            self.mean = statistics.mean(interval)
            rng = max(interval) - min(interval)
            z = st.norm.ppf(1 - (1 - interval_proportion) / 2)
            self.sd = rng / (2 * z)
        elif mean != None and sd != None and interval == None:
            self.mean = mean
            self.sd = sd
        else:
            raise Exception(
                "Either supply interval endpoints or mean and sd, but not both."
            )

    def sample(self) -> float:
        return np.random.normal(loc=self.mean, scale=self.sd)

