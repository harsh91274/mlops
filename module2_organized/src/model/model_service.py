"""
ModelService class for managing machine learning models.

Contains the ModelService class, which handles loading and using the pre-trained ML model.
The class offers methods to load a model from a file, building it if it doesn't exist,
and to make predictions using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model

class ModelService:
    """
    ModelService class for managing machine learning models.

    This class is responsible for loading and using pre-trained ML models. It offers
    methods to load a model from a file, building it if it doesn't exist, and to make predictions using the
    loaded model.

    Attributes:
    model (object): The loaded machine learning model.

    Methods:
    load_model(model_name: str) -> None:
        Load a model from a file, build it if it doesn't exist.

    predict(input_parameters: list) -> list:
        Make predictions using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize ModelService class."""
        self.model = None

    def load_model(self, model_name="rf_v1") -> None:
        """Load a model from a file, build it if it doesn't exist."""
        logger.info(
            f'Checking existence of model config file at {model_settings.model_path}/{model_settings.model_name}'
        )
        model_path = Path(f"{model_settings.model_path}/{model_settings.model_name}")

        if not model_path.exists():
            logger.warning(
                f'Model at {model_settings.model_path}/{model_settings.model_name} was not found -> building {model_settings.model_name}'
            )
            build_model()

        logger.info(
            f'Model {model_settings.model_name} exists -> loading model configuration file'
        )
        with open(model_path, 'rb') as file:
            self.model = pk.load(file)

    def predict(self, input_parameters: list) -> list:
        """
        Make predictions using the loaded model.

        Parameters:
        input_parameters (list): A list of input parameters for the model.

        Returns:
        list: A list of predictions made by the model.
        """
        logger.info('Making predictions')
        return self.model.predict([input_parameters])
