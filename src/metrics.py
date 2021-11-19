"""
Models performance metrics.
"""

from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt

from .models import Model


class Metrics(ABC):
    """Abstract representation of the model metrics."""

    @property
    @abstractmethod
    def r_2(self) -> float:
        """Computes the coefficient of determination R^2"""
        ...

    @property
    @abstractmethod
    def mape(self) -> float:
        """Computes the MAPE"""
        ...


class LinearModelMetrics(Metrics):
    """Representation of a linear model metrics"""

    def __init__(
        self, model: Model, predictors: npt.ArrayLike, response: npt.ArrayLike
    ):
        self.model = model
        self.predictors = np.array(predictors)
        self.response = np.array(response)

    @property
    def r_2(self) -> float:
        """Computes the coefficient of determination R^2"""
        ssr = np.sum((self.model.predict(self.predictors) - self.response.mean()) ** 2)
        sst = np.sum((self.response - self.response.mean()) ** 2)
        return ssr / sst

    @property
    def mape(self) -> float:
        """Computes the MAPE"""
        return np.sum(
            np.absolute((self.response - self.model.predict(self.predictors)))
            / self.response
        )
