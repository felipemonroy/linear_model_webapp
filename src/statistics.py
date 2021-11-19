"""
Statistics from models.
"""

from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol, Tuple

import numpy as np
import numpy.typing as npt
from scipy.stats import shapiro
from statsmodels.stats.stattools import durbin_watson


class TestHypotheses(Protocol):
    """Protocol that represents an hypotheses test."""

    @property
    @abstractmethod
    def statistic(self):
        """Get the test statistic."""
        ...

    @property
    @abstractmethod
    def confidence_interval(self):
        """Get the test statistic confidence interval."""
        ...

    @property
    @abstractmethod
    def p_value(self):
        """Get the p-value."""
        ...

    @property
    @abstractmethod
    def hypotheses(self):
        """Get the hypotheses."""
        ...

    @property
    @abstractmethod
    def conclusion(self):
        """Get the test conclusion."""
        ...


class TestValue(Protocol):
    """Protocol that represents a value tested."""

    @property
    @abstractmethod
    def value(self):
        """Get the value to be tested."""
        ...

    @property
    @abstractmethod
    def interval(self):
        """Get the interval where the test is satisfied."""
        ...

    @property
    @abstractmethod
    def conclusion(self):
        """Get the test conclusion."""
        ...


@dataclass
class Interval:
    """Representation of an interval."""

    lower_limit: float
    upper_limit: float
    name: str = "Interval"

    def contain(self, value: float) -> bool:
        """Check if the value is inside the interval."""
        if self.lower_limit <= value <= self.upper_limit:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.name}: [{self.lower_limit}, {self.upper_limit}]"


class ShapiroWilkTest:
    """Shapiro Wilk test class."""

    def __init__(self, resid: npt.ArrayLike, alpha: float = 0.05):
        self.resid = np.array(resid)
        self.alpha = alpha

    @property
    def statistic(self) -> float:
        """Get the test statistic."""
        return shapiro(self.resid).statistic

    @property
    def confidence_interval(self) -> Tuple[float, float]:
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


class DarwinWatsonTest:
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
