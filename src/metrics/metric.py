"""
Models performance metrics.
"""

from abc import ABC, abstractmethod

import numpy as np
from numpy.typing import ArrayLike
from src.models.model import Model


class Metrics(ABC):
    """Abstract representation of a metric"""

    def __init__(self, model: Model, X: ArrayLike, y: ArrayLike):
        self.y_true = np.array(y)
        self.X = np.array(X)
        self.y_pred = model.predict(self.X)

    @property
    @abstractmethod
    def type(self) -> str:
        """Get the type of the metric."""
        ...
