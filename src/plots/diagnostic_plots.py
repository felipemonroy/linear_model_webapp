"""
Models diagnostic plots.
"""

from typing import Tuple

import numpy.typing as npt
import plotly.graph_objects as go
from plotly.graph_objects import Figure
from src.plots.diagnostic_plot import PlotlyPlot
from statsmodels.graphics.gofplots import qqplot


class QQPlot(PlotlyPlot):
    """Object representation of a QQ plot."""

    def __init__(
        self,
        data: npt.ArrayLike,
        title: str = "Quantile-Quantile Plot",
        ylabel: str = "Sample Quantities",
        xlabel: str = "Theoritical Quantities",
        size: Tuple[float, float] = (800, 700),
        marker_color: str = "#19d3f3",
        line_color: str = "#636efa",
    ):
        self._fig = go.Figure()
        self._data = qqplot(data, line="s").gca().lines
        self.title = title
        self.ylabel = ylabel
        self.xlabel = xlabel
        self.size = size
        self.marker_color = marker_color
        self.line_color = line_color

    def _add_markers(self) -> None:
        self._fig.add_trace(
            go.Scatter(
                x=self._data[0].get_xdata(),
                y=self._data[0].get_ydata(),
                mode="markers",
                fillcolor=self.marker_color,
            )
        )

    def _add_line(self) -> None:
        self._fig.add_trace(
            go.Scatter(
                x=self._data[1].get_xdata(),
                y=self._data[1].get_ydata(),
                mode="lines",
                fillcolor=self.line_color,
            )
        )

    def _update_layout(self) -> None:
        self._fig.update_layout(
            {
                "title": self.title,
                "xaxis": {"title": self.xlabel, "zeroline": False},
                "yaxis": {"title": self.ylabel},
                "showlegend": False,
                "width": self.size[0],
                "height": self.size[1],
            }
        )

    @property
    def fig(self) -> Figure:
        self._add_markers()
        self._add_line()
        self._update_layout()

        return self._fig
