"""
Pages.
"""

import pandas as pd
import streamlit as st
from app.pages.page import Page
from src.settings.settings import AppConfig


class OverallPage(Page):
    """Overall page."""

    def __init__(self, params: AppConfig, title="Overall"):
        self.params = params
        self.title = title

    def render(self) -> None:
        """Render the page."""

        st.header(self.title)

    def __str__(self) -> str:
        return self.title

    def __eq__(self, other):
        if isinstance(other, OverallPage):
            return self.title == other.title

        return False


class MetricPage(Page):
    """Metric page."""

    def __init__(self, params: AppConfig, title="Metrics"):
        self.params = params
        self.title = title

    def render(self) -> None:
        """Render the page."""
        st.header(self.title)

    def __str__(self) -> str:
        return self.title

    def __eq__(self, other):
        if isinstance(other, MetricPage):
            return self.title == other.title

        return False


class DiagnosticPage(Page):
    """Diagnostic page."""

    def __init__(self, params: AppConfig, title="Diagnostic"):
        self.params = params
        self.title = title

    def render(self) -> None:
        """Render the page."""
        st.header(self.title)

    def __str__(self) -> str:
        return self.title

    def __eq__(self, other):
        if isinstance(other, DiagnosticPage):
            return self.title == other.title


class HomePage(Page):
    """Home page."""

    def __init__(self, params: AppConfig, title="Home"):
        self.params = params
        self.title = title
        self.dataframe = None

    def render(self) -> None:
        """Render the page."""
        loaded_file = st.file_uploader("Upload CSV file", type="csv")
        data = pd.read_csv(loaded_file)

        st.header(self.title)
        st.selectbox("Select dependent variable", data.columns)
        st.multiselect("Select predictors", data.columns)

    def __str__(self) -> str:
        return self.title

    def __eq__(self, other):
        if isinstance(other, HomePage):
            return self.title == other.title
