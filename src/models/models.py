"""
Models structure.
"""

import numpy as np
from numpy.typing import ArrayLike
from sklearn.linear_model import LinearRegression


class LinearRegressionExpanded(LinearRegression):
    """Linear regression from sklearn expanded."""

    def resid(self, X: ArrayLike, y: ArrayLike) -> np.ndarray:
        """Get the residuals from a linear regression."""
        return np.array(y - self.predict(X))
