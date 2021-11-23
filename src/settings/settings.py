"""
Config.
"""

from driconfig import DriConfig
from pydantic import BaseModel
from src import __version__


class FormatPlot(BaseModel):
    """Model for plots configuration."""

    AXIS_FONT_SIZE: int
    TICK_FONT_SIZE: int
    TEMPLATE: str

    class Config:
        """Configuring BaseModel"""

        allow_mutation = False


class AppConfig(DriConfig):
    """Interface for the settings.yml file."""

    class Config:
        """Configure the YML file location."""

        config_folder = "./config"
        config_file_name = "parameters.yml"
        allow_mutation = False

    VERSION: str = __version__
    APP_NAME: str
    FORMAT_PLOTS: FormatPlot
