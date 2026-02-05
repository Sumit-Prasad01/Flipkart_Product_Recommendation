from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from src.data_converter import DataConverter
from config.config import Config
from config.paths_config import *
from utils.custom_exception import CustomException
from utils.logger import get_logger

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self):

        self.embedding = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vstore = AstraDBVectorStore(

            embedding = self.embedding,
            collection_name = Config.COLLECTION_NAME,
            api_endpoint = Config.ASTRA_DB_API_ENDPOINT,
            token = Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace = Config.ASTRA_DB_KEYSPACE

        )
    
    def ingest(self, load_existing : bool = True):
        try:

            logger.info("Ingesting data to vector store.")

            if load_existing == True:
                return self.vstore
            
            docs = DataConverter(CSV_DATA_PATH).convert()

            self.vstore.add_documents(docs)

            logger.info("Data ingested to vector store successfully.")

            return self.vstore

        except Exception as e:
            logger.error(f"Failed to ingest data into vector store : {e}")
            raise CustomException("Error while ingesting data into vector store.",  e)
        
    