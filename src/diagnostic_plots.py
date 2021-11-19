"""
Models diagnostic plots.
"""

from typing import Protocol

import plotly.graph_objects as go
from plotly.graph_objects import Figure
from statsmodels.graphics.gofplots import qqplot

# qqplot_data = qqplot(gauss_data, line="s").gca().lines


class Plotter(Protocol):
    """Protocol that represents a Plotter class."""

    def plot(self) -> None:
        """Plot data on Plotly figure."""
        ...

    def update_xaxis(self) -> None:
        """Update the xaxis."""
        ...

    def update_yaxis(self) -> None:
        """Update the yaxis."""
        ...

    @property
    def fig(self) -> Figure:
        """Get the figure object."""
        ...


# class QQPlot
