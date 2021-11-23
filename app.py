"""
App
"""

from app.canvas import Canvas
from src.settings.settings import AppConfig


def main():
    """Main function."""

    parameters = AppConfig()

    app = Canvas(parameters)
    app.build()


if __name__ == "__main__":
    main()
