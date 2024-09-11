"""
This script is responsible for running the main prediction process.
"""

# Base Python Libraries
import logging

# Open Source Libraries
from loguru import logger

# Local Modules
from model.model_service import ModelService

@logger.catch
def _main() -> None:
    """
    Main function to load the model, make predictions, and log the results.
    """
    logger.info("running the application")
    ml_svc = ModelService()
    ml_svc.load_model()

    feature_values={
        'area':85, 
        'construction_year':2015,
        'bedrooms': 2,
        'garden_area':20,
        'balcony_present':1, 
        'parking_present':1,
        'furnished':0,
        'garage_present':0,
        'storage_present':1,
    }

    pred = ml_svc.predict(list(feature_values.values()))
    logger.info(f'prediction={pred}')
    print(pred)


if __name__ == '__main__':
    _main()
