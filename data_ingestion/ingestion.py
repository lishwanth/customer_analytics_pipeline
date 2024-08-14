from utils.logger import Logger
from utils.data_loader import DataLoader

class DataIngestion:
    def __init__(self, config):
        self.logger = Logger(config)
        self.data_loader = DataLoader(config)
    
    def start_ingestion(self):
        self.logger.log("Starting data ingestion...")
        # Implement ingestion logic using NiFi REST API
        # Example:
        # response = requests.post(config['nifi_endpoint'] + '/templates', data=template_data)
        self.logger.log("Data ingestion completed.")
        return True
