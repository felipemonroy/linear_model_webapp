"""
Models structure.
"""

from typing import List, Protocol

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

    def equation(self, x_names: List[str], y_name: str) -> str:
        """Get the linear regression equation"""


class ClassificationModel(Model):
    """Abstract representation of a classification model object."""
