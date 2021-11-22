"""
Models structure.
"""

from typing import List

from sklearn.linear_model import LinearRegression


class LinearRegressionExpanded(LinearRegression):
    """Linear regression model from sklearn expanded."""

    def equation(self, x_names: List[str], y_name: str) -> str:
        """Get the regression equation."""
        if not len(x_names) == len(self.coef_) - 1:
            raise ValueError("Lenght of x_names and coefficients doest not match")
        betas = [f"{coef} x {name}" for coef, name in zip(self.coef_[1:], x_names)]
        return f"{y_name} = {self.coef_[0]} + {' + '.join(betas)}"
