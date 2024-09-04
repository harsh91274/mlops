#1. pick up model
# 1.1 if config file exists, load the trained model
# 1.2 if config file does not exist, train the model to get it

#2. make predictions 
from pathlib import Path
import pickle as pk
from config.config import settings
from model.pipeline.model import build_model
from loguru import logger

class ModelService:
    def __init__ (self):
        self.model = None
        
    def load_model(self, model_name='rf_v1'):
        logger.info(f"checking existince of model config file at {settings.model_path}/{settings.model_name}")
        model_path=Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning (f"model at {settings.model_path}/{settings.model_name} was not found -> building {settings.model_name}")
            build_model()
        
        logger.info(f"model {settings.model_name} exists -> loading model configuration file ")
        self.model=pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))
    
    def predict(self, input_parameters):
        logger.info("making predictions")
        return self.model.predict([input_parameters])
    
#test the code
# ml_svc=ModelService()
# ml_svc.load_model('rf_v1')
# pred= ml_svc.predict([85, 2015, 2, 20, 1, 1, 0, 0 , 1])
# print(pred)
    
    