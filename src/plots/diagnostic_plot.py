"""
Plot
"""

from abc import ABC, abstractmethod

from matplotlib.figure import Figure


class PlotlyPlot(ABC):
    """Abstract representation of a Plotter class."""

    @property
    @abstractmethod
    def fig(self) -> Figure:
        """Plot data on a figure."""
        ...
