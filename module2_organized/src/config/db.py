"""
Configuration settings for the database configuration.

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
from sqlalchemy import create_engine
from loguru import logger


class DbSettings(BaseSettings):
    """
    Database configuration settings.

    Attributes:
    model_config (SettingsConfigDict): Configuration settings for the model.
    db_conn_str (str): The database connection string.
    rent_apart_table_name (str): The name of the rental apartment table in the database.

    Methods:
    None
    """

    model_config = SettingsConfigDict(env_file='config/.env', env_file_encoding='utf-8', extra='ignore',)
    db_conn_str: str
    rent_apart_table_name: str


db_settings = DbSettings()
engine = create_engine(db_settings.db_conn_str)