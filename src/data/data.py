"""
Data.
"""

from dataclasses import dataclass

import pandas as pd


@dataclass
class Data:
    """Representation of the data."""

    X: pd.DataFrame
    y: pd.Series

    @property
    def X_names(self):
        """Get the X names."""
        return self.X.columns

    @property
    def y_name(self):
        """Get the y name."""
        return self.y.name
