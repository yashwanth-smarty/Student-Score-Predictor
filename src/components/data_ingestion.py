import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data: str=os.path.join('artifact',"train.csv")
    test_data: str=os.path.join('artifact',"test.csv")
    raw_data: str=os.path.join('artifact',"data.csv")

class DataIngestion:
    def __init__(self):
        self.init_data_ingestion=DataIngestionConfig()

    def InitIngestion(self):
        logging.info("Initialized Data ingestion")
        try:
            data=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset')

            os.makedirs(os.path.dirname(self.init_data_ingestion.train_data),exist_ok=True)

            data.to_csv(self.init_data_ingestion.raw_data,index=False,header=True)
            logging.info('Train test split initialized')
            train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)

            train_set.to_csv(self.init_data_ingestion.train_data,index=False,header=True)
            test_set.to_csv(self.init_data_ingestion.test_data,index=False,header=True)

            logging.info('Ingestion completed')
            
            return(
                self.init_data_ingestion.train_data,
                self.init_data_ingestion.test_data
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.InitIngestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer=ModelTrainer()
    print(model_trainer.model_training(train_arr,test_arr))