from src.mlproject.logger  import logging
from src.mlproject.exception import CustomException
import sys
# import the data ingestion for using the funtion written in it 
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_ingestion import DataIngestion




if __name__=="__main__":
    logging.info("The Execution is started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
    