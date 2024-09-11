"""
Module for building and evaluating a machine learning model.

This module orchestrates the entire machine learning pipeline, including data preparation,
model training, hyperparameter tuning, model evaluation, and saving the model.
"""

# Base Python Libraries
import pandas as pd
import pickle as pk

# Open Source Libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

# Imports from other modules
from config import model_settings
from loguru import logger
from model.pipeline.preparation import prepare_data


def build_model():
    """
    Orchestrates the entire machine learning pipeline.
    """
    logger.info('starting up model building pipeline')
    # 1. load preprocessed dataset
    df = prepare_data()
    feature_names = ['area', 'constraction_year', 'bedrooms', 'garden',
                     'balcony_yes', 'parking_yes', 'furnished_yes',
                     'garage_yes', 'storage_yes']
    # 2. identify X and y
    X, y = _get_x_y(df, col_x=feature_names)
    # 3. split the dataset
    X_train, X_test, y_train, y_test = _split_train_test(X, y)
    # 4. train the model
    rf = _train_model(X_train, y_train)
    # 5. evaluate the model
    score = _evaluate_model(rf, X_test, y_test)
    # print(score)
    # 6. tune hyperparameters
    # 7. save the model in a configuration file
    _save_model(rf)


def _get_x_y(data: pd.DataFrame, col_x: list, col_y: str = 'rent') -> tuple:
    """
    Defines the X and y variables for the machine learning model.

    Args:
        data (pd.DataFrame): The input data.
        col_x (list): The names of the columns to use as features.
        col_y (str): The name of the column to use as the target variable.

    Returns:
        tuple: A tuple containing the X and y variables.
    """
    logger.info(f"defining X and Y variables. \n X vars: {col_x}\n y var: {col_y}")
    return data[col_x], data[col_y]


def _split_train_test(X: pd.DataFrame, y: pd.Series) -> tuple:
    """
    Splits the dataset into training and testing sets.

    Args:
        X (pd.DataFrame): The features.
        y (pd.Series): The target variable.

    Returns:
        tuple: A tuple containing the training and testing sets.
    """
    logger.info("splitting into train and test")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test


def _train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestRegressor:
    """
    Trains a machine learning model using the training data.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training target variable.

    Returns:
        sklearn.ensemble.RandomForestRegressor: The trained model.
    """
    logger.info("training a model with hyperparameters")
    grid_space = {'n_estimators': [100, 200, 300], 'max_depth': [3, 6, 9, 12]}
    logger.debug(f"grid space={grid_space}")
    grid = GridSearchCV(RandomForestRegressor(), param_grid=grid_space, cv=5, scoring='r2')
    model_grid = grid.fit(X_train, y_train)
    return model_grid.best_estimator_


def _evaluate_model(model: RandomForestRegressor, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    """
    Evaluates the performance of the machine learning model using the testing data.

    Args:
        model (sklearn.ensemble.RandomForestRegressor): The trained model.
        X_test (pd.DataFrame): The testing features.
        y_test (pd.Series): The testing target variable.

    Returns:
        float: The model's score.
    """
    logger.info(f"evaluating model performance. Score = {model.score(X_test, y_test)}")
    return model.score(X_test, y_test)


def _save_model(model: RandomForestRegressor):
    """
    Saves the trained model to a file.

    Args:
        model (sklearn.ensemble.RandomForestRegressor): The trained model.
    """

    model_path=f'{model_settings.model_path}/{model_settings.model_name}'
    logger.info(f"saving a model to a directory: {model_path}")
    with open(model_path, 'wb') as model_file:
        pk.dump(model, model_file)


build_model()