"""
Models performance metrics.
"""

import numpy as np
from src.metrics.metric import Metrics


class RegressionMetrics(Metrics):
    """Representation of a regression model metrics."""

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
