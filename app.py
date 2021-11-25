"""
App
"""

from app.pages.page import MultiPage, SideBar
from app.pages.pages import DiagnosticPage, MetricPage, OverallPage
from src.metrics.metrics import RegressionMetrics
from src.models.models import LinearRegressionExpanded
from src.settings.settings import AppConfig


def main():
    """Main function."""

    parameters = AppConfig()

    sidebar = SideBar(parameters.APP_NAME)
    sidebar.render()

    if sidebar.data:
        model = LinearRegressionExpanded()
        model.fit(sidebar.data.X, sidebar.data.y)

        metrics = RegressionMetrics(model, sidebar.data.X, sidebar.data.y)

        page_overall = OverallPage(parameters)
        page_metric = MetricPage(parameters, metrics)
        page_diagnostic = DiagnosticPage(parameters)

        page = MultiPage()

        page.add_page(page_overall)
        page.add_page(page_metric)
        page.add_page(page_diagnostic)

        page.run()


if __name__ == "__main__":
    main()
