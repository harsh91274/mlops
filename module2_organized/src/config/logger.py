"""
Configuration settings for the logger.

Attributes:
None

Functions:
None

Classes:
Settings: A class for managing configuration settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger


class LoggerSettings(BaseSettings):
    """
    A class for managing logger configuration settings.

    Attributes:
    model_config (SettingsConfigDict): Configuration settings for the model.
    log_level (str): The log level for logging.

    Methods:
    None
    """

    model_config = SettingsConfigDict(env_file='config/.env', env_file_encoding='utf-8', extra='ignore',)
    log_level: str


def configure_logging(log_level: str) -> None:
    """
    Configures the logging settings for the machine learning project.

    Args:
    log_level (str): The log level for logging. It should be one of the following:
        'trace', 'debug', 'info', 'success', 'warning', 'error', 'critical'.

    Returns: None
    """
    logger.remove()
    logger.add("logs/app.log", rotation='1 day', retention='2days', compression='zip', level=log_level)

#Initializing settings and configure logging
configure_logging(log_level=LoggerSettings().log_level)