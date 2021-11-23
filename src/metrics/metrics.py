"""
Models performance metrics.
"""

import numpy as np
from numpy.typing import ArrayLike
from src.metrics.metric import Metrics
from src.models.model import Model


class RegressionMetrics(Metrics):
    """Representation of a regression model metrics."""

    def __init__(self, model: Model, X: ArrayLike, y: ArrayLike):
        self.y_true = np.array(y)
        self.X = np.array(X)
        self.y_pred = model.predict(self.X)

    @property
    def r_2(self) -> str:
        """Computes the coefficient of determination R^2."""
        ssr = np.sum((self.y_pred - self.y_true.mean()) ** 2)
        sst = np.sum((self.y_true - self.y_true.mean()) ** 2)
        return f"{ssr / sst:.2f}"

    @property
    def mape(self) -> str:
        """Computes the MAPE."""
        return (
            f"{np.sum(np.absolute((self.y_true - self.y_pred)) / self.y_true)*100:.2f}%"
        )

    @property
    def type(self) -> str:
        """Return the type of metrics."""
        return "regression"


class ClassificationMetrics(Metrics):
    """Representation of a classification model metrics."""

    @property
    def type(self) -> str:
        """Return the type of metrics."""
        return "classification"
