"""
Models structure.
"""

from abc import abstractmethod
from typing import Protocol, runtime_checkable

import numpy as np
import numpy.typing as npt
from sklearn.linear_model import LinearRegression


@runtime_checkable
class Model(Protocol):
    """Abstract representation of a Model object."""

    @abstractmethod
    def fit(self):
        """Fit the model."""
        ...

    @abstractmethod
    def predict(self, *args, **kwargs) -> np.ndarray:
        """Predict the response variable given predictors."""
        ...

    @abstractmethod
    def resid(self) -> np.ndarray:
        """Get the residuals of the trained model."""
        ...


class LinearRegressionExpanded(LinearRegression):
    """Linear regression from sklearn expanded."""

    def resid(self, predictors: npt.ArrayLike, response: npt.ArrayLike) -> np.ndarray:
        """Get the residuals from a linear regression."""
        return np.array(response - self.predict(predictors))
