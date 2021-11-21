"""
Statistics from models.
"""

import numpy as np
import numpy.typing as npt
from scipy.stats import shapiro
from src.statistics.statistic import Interval, TestHypotheses, TestValue
from statsmodels.stats.stattools import durbin_watson


class ShapiroWilkTest(TestHypotheses):
    """Shapiro Wilk test class."""

    def __init__(self, resid: npt.ArrayLike, alpha: float = 0.05):
        self.resid = np.array(resid)
        self.alpha = alpha

    @property
    def statistic(self) -> float:
        """Get the test statistic."""
        return shapiro(self.resid).statistic

    @property
    def confidence_interval(self) -> Interval:
        """Get the test statistic confidence interval."""
        raise NotImplementedError(
            "Confidence intervals are not implemented for this test"
        )

    @property
    def p_value(self) -> float:
        """Get the p-value."""
        return shapiro(self.resid).pvalue

    @property
    def hypotheses(self) -> str:
        """Get the hypotheses."""
        return """
            H_0: The residuals are normally distributed
            H_a: The residuals are not normally distributed
            """

    @property
    def conclusion(self) -> str:
        """Get the test conclusion."""
        if self.p_value > self.alpha:
            return """
                There is not enough evidence to conclude that
                the residuals do not come from a normal distribution
                """
        else:
            return """
                There is enough evidence to conclude that
                the residuals do not come from a normal distribution
                """


class DarwinWatsonTest(TestValue):
    """Darwin Watson test class."""

    def __init__(
        self, resid: npt.ArrayLike, lower_limit: float = 2.5, upper_limit: float = 3.5
    ):
        self.resid = np.array(resid)
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    @property
    def value(self):
        """Get the Darwin Watson value to be tested."""
        return durbin_watson(self.resid)

    @property
    def interval(self) -> Interval:
        """Get the interval where the test is satisfied."""
        return Interval(self.lower_limit, self.upper_limit)

    @property
    def conclusion(self) -> str:
        """Get the test conclusion."""
        if self.interval.lower_limit <= self.value <= self.interval.upper_limit:
            return """
                Pass
                """
        else:
            return """
                Pass
                """
