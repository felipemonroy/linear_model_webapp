"""
Models performance metrics.
"""

import numpy as np
from src.metrics.metric import Metrics


class RegressionMetrics(Metrics):
    """Representation of a regression model metrics."""

    @property
    def r_2(self) -> float:
        """Computes the coefficient of determination R^2."""
        ssr = np.sum((self.y_pred - self.y_true.mean()) ** 2)
        sst = np.sum((self.y_true - self.y_true.mean()) ** 2)
        return ssr / sst

    @property
    def mape(self) -> float:
        """Computes the MAPE."""
        return np.sum(np.absolute((self.y_true - self.y_pred)) / self.y_true)

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
