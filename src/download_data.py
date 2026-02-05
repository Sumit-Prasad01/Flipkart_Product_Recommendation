import os
import requests
from dotenv import load_dotenv

from utils.logger import get_logger
from utils.custom_exception import CustomException
from config.download_data_config import *

logger = get_logger(__name__)
load_dotenv()


class DatasetDownloader:
    def __init__(self, url, folder_name: str, file_name: str):
        self.url = self.convert_to_raw_url(url)
        self.folder_name = folder_name
        self.file_name = file_name
        self.file_path = os.path.join(self.folder_name, self.file_name)

    def convert_to_raw_url(self, url: str) -> str:
        """
        Converts GitHub blob URL to raw URL if needed.
        """
        if "github.com" in url and "/blob/" in url:
            url = url.replace("github.com", "raw.githubusercontent.com")
            url = url.replace("/blob/", "/")
        return url

    def create_folder(self):
        os.makedirs(self.folder_name, exist_ok=True)

    def is_html(self, text: str) -> bool:
        text = text.strip().lower()
        return text.startswith("<!doctype html") or "<html" in text

    def download_file(self):
        try:
            logger.info(f"Downloading dataset from: {self.url}")

            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(self.url, headers=headers)

            if response.status_code != 200:
                logger.error(f"Failed to download file. Status code: {response.status_code}")
                raise Exception(f"Download failed with status code {response.status_code}")

            # check if file is actually html
            preview = response.text[:200]
            if self.is_html(preview):
                logger.error("Downloaded content is HTML, not CSV. Wrong URL detected.")
                raise Exception("Downloaded content is HTML instead of CSV. Check dataset URL.")

            with open(self.file_path, "wb") as file:
                file.write(response.content)

            logger.info(f"Download complete! Saved at: {self.file_path}")

        except Exception as e:
            logger.error("Failed to download file.")
            raise CustomException("Error while downloading dataset.", e)

    def run(self):
        self.create_folder()
        self.download_file()


if __name__ == "__main__":
    url = os.getenv("DATASET_URL")

    if not url:
        raise ValueError("DATASET_URL not found in .env file")

    downloader = DatasetDownloader(url, FOLDER_NAME, FILE_NAME)
    downloader.run()
