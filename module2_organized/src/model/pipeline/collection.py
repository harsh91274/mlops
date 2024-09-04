import pandas as pd
from config.config import engine
from loguru import logger
from db.db_model import RentApartments
from sqlalchemy import select

def load_data(path): 
    logger.info(f"loading csv file at path {path}")
    return pd.read_csv(path)


def load_data_from_db():
    logger.info("extracting table from database")
    query=select(RentApartments)
    return pd.read_sql(query, engine)

#test
#df=load_data()
#print(df)