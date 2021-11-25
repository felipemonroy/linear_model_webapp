"""
Page.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

import pandas as pd
import streamlit as st
from src.data.data import Data
from streamlit.elements.file_uploader import SomeUploadedFiles


class Page(ABC):
    """Abstract representtion of a Page."""

    @abstractmethod
    def render(self):
        """Render page."""
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __eq__(self, other):
        ...


class MultiPage:
    """Constructor class to generate a list which will store all
    our applications as an instance variable.
    """

    def __init__(self):
        self.pages: List[Page] = []
        self._loaded_file: SomeUploadedFiles = None

    def add_page(self, page: Page) -> None:
        """Class Method to Add pages to the project."""
        self.pages.append(page)

    def run(self) -> None:
        """Render Multipage."""
        page = st.sidebar.selectbox(
            "App Navigation", self.pages, format_func=lambda page: page
        )

        page.render()


class SideBar:
    def __init__(self, title):
        self.title = title
        self._dataframe: pd.DataFrame = pd.DataFrame()
        self._X_name: List[str] = []
        self._y_name: Optional[str] = None

    def render(self):
        st.sidebar.header(self.title)
        loaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

        if not loaded_file:
            return None

        self._dataframe = pd.read_csv(loaded_file)
        self._y_name = st.sidebar.selectbox(
            "Select dependent variable", self._dataframe.columns
        )
        self._X_names = st.sidebar.multiselect(
            "Select predictors", self._dataframe.columns
        )

    @property
    def data(self) -> Optional[Data]:
        if not self._dataframe.empty and self._X_names and self._y_name:
            return Data(
                self._dataframe.loc[:, self._X_names], self._dataframe[self._y_name]
            )
        return None
