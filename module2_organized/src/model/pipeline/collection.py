"""
Data collection and preprocessing module for the machine learning project.

This module contains functions for loading data from a CSV file and a database.
The data is then preprocessed and returned as a pandas DataFrame.

Attributes:
None

Functions:
load_data: Loads data from a CSV file.
load_data_from_db: Loads data from the database.

Classes:
None
"""

# Import necessary libraries
from loguru import logger
import pandas as pd
from sqlalchemy import select

from config import engine
from db.db_model import RentApartments

def load_data_from_db() -> pd.DataFrame:
    """
    Loads data from the database.

    Args:
    None

    Returns:
    pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    logger.info("Extracting table from database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)


# Test
# Uncomment the following line to test the load_data function
# df = load_data()
# print(df)