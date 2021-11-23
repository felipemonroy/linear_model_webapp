"""
Page.
"""

from abc import ABC, abstractmethod

import streamlit as st


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
        self.pages = []

    def add_page(self, page: Page) -> None:
        """Class Method to Add pages to the project."""

        self.pages.append(page)

    def run(self) -> None:
        """Render Multipage."""
        page = st.sidebar.selectbox(
            "App Navigation", self.pages, format_func=lambda page: page
        )

        page.render()
