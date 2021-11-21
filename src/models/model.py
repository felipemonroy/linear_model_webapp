"""
Models structure.
"""

from typing import Protocol

import numpy as np
from numpy.typing import ArrayLike


class Model(Protocol):
    """Abstract representation of a model"""

    def fit(self, X: ArrayLike, y: ArrayLike) -> None:
        """Fit the model."""

    def predict(self, X: ArrayLike) -> np.ndarray:
        """Predict the response variable given predictors."""


class RegressionModel(Model):
    """Abstract representation of a regression model object."""


class ClassificationModel(Model):
    """Abstract representation of a classification model object."""
