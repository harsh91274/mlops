"""
Configuration settings for the machine learning project.

This module contains the configuration settings for the machine learning project,
such as paths, model names, database connection strings, and logging settings.

Attributes:
None

Functions:
None

Classes:
Settings: A class for managing configuration settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath

class ModelSettings(BaseSettings):
    """
    ML model configuration settings for the application.

    Attributes:
    model_config (SettingsConfigDict): Configuration settings for the model.
    model_path (str): The path to the folder containing model config files.
    model_name (str): The name of the model to be used.
    """

    model_config = SettingsConfigDict(env_file='config/.env', env_file_encoding='utf-8',  extra='ignore',)
    model_path: str
    model_name: str


model_settings = ModelSettings()
