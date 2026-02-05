import pandas as pd
from config.paths_config import *
from utils.custom_exception import CustomException
from utils.logger import get_logger
from langchain_core.documents import Document

logger = get_logger(__name__)

class DataConverter:
    def __init__(self, file_path : str):
        self.file_path = file_path

    def convert(self):
        try:

            logger.info("Loading CSV Data......")
            logger.info("Converting raw cvs into documents.")

            df = pd.read_csv(self.file_path)[["product_title", "review"]]
            docs = [

                Document(page_content = row['review'], metadata = {"product_name" : row["product_title"]})
                for _, row in df.iterrows()

            ]

            logger.info("Data conversion converted successfully.")

            return docs
    
        except Exception as e:
            logger.error(f"Failed to convert data : {e}")
            raise CustomException("Error while converting data.", e)