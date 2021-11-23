"""
Canvas.
"""

from src.settings.settings import AppConfig

from app.pages.page import MultiPage
from app.pages.pages import DiagnosticPage, MetricPage, OverallPage


class Canvas:
    """Class defining the structure of the application."""

    def __init__(self, params: AppConfig):
        self._title = params.APP_NAME
        self._version = params.VERSION
        self._parameters = params

    def build(self):
        """Render each one of the sections."""
        page = MultiPage()

        page_overall = OverallPage(self._parameters)
        page_metric = MetricPage(self._parameters)
        diagnostic_page = DiagnosticPage(self._parameters)

        page.add_page(page_overall)
        page.add_page(page_metric)
        page.add_page(diagnostic_page)

        page.run()
