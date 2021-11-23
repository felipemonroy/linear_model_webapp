"""
Models performance metrics.
"""

from abc import ABC, abstractmethod


class Metrics(ABC):
    """Abstract representation of a metric"""

    @property
    @abstractmethod
    def type(self) -> str:
        """Get the type of the metric."""
        ...
