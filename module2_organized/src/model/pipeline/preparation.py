"""
Data preparation module for the machine learning project.

This module contains functions for preparing the rental apartment data.
The data is loaded from the database, categorical variables are encoded,
and the garden column is parsed.

Attributes:
None

Functions:
prepare_data: Prepares the rental apartment data.
encode_cat_cols: Encodes categorical variables in the data.
parse_garden_col: Parses the garden column in the data.

Classes:
None
"""

# Base Python Libraries
import re
import warnings

# Open Source Libraries
import pandas as pd
from loguru import logger

# Imports from other modules
from model.pipeline.collection import load_data_from_db

warnings.filterwarnings('ignore')


def prepare_data() -> pd.DataFrame:
    """
    Prepares the rental apartment data.

    Args:
    None

    Returns:
    pd.DataFrame: The prepared data as a pandas DataFrame.
    """
    logger.info('Starting preprocessing pipeline')
    # Load the dataset
    data = load_data_from_db()
    # Encode categorical columns
    data_encoded = _encode_cat_cols(data)
    # Parse the garden column
    df = _parse_garden_col(data_encoded)

    return df


def _encode_cat_cols(data: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes categorical variables in the data.

    Args:
    data (pd.DataFrame): The input data as a pandas DataFrame.

    Returns:
    pd.DataFrame: The data with encoded categorical variables.
    """
    cols = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(f'Encoding categorical variables: {cols}')
    return pd.get_dummies(data, columns=cols, drop_first=True)


def _parse_garden_col(data: pd.DataFrame) -> pd.DataFrame:
    """
    Parses the garden column in the data.

    Args:
    data (pd.DataFrame): The input data as a pandas DataFrame.

    Returns:
    pd.DataFrame: The data with parsed garden column.
    """
    logger.info('Parsing garden columns')
    for i in range(len(data)):
        if data.garden[i] == 'Not present':
            data.garden[i] = 0
        else:
            data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
    return data