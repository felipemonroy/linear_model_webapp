"""
Statistics from models.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


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


class TestHypotheses(ABC):
    """Protocol that represents an hypotheses test."""

    @property
    @abstractmethod
    def statistic(self) -> float:
        """Get the test statistic."""
        ...

    @property
    @abstractmethod
    def confidence_interval(self) -> Interval:
        """Get the test statistic confidence interval."""
        ...

    @property
    @abstractmethod
    def p_value(self) -> float:
        """Get the p-value."""
        ...

    @property
    @abstractmethod
    def hypotheses(self) -> str:
        """Get the hypotheses."""
        ...

    @property
    @abstractmethod
    def conclusion(self) -> str:
        """Get the test conclusion."""
        ...


class TestValue(ABC):
    """Protocol that represents a value tested."""

    @property
    @abstractmethod
    def value(self) -> float:
        """Get the value to be tested."""
        ...

    @property
    @abstractmethod
    def interval(self) -> Interval:
        """Get the interval where the test is satisfied."""
        ...

    @property
    @abstractmethod
    def conclusion(self) -> str:
        """Get the test conclusion."""
        ...
