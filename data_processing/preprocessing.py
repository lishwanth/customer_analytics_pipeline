from utils.logger import Logger

class Preprocessing:
    def __init__(self, config):
        self.logger = Logger(config)
    
    def clean_data(self, data):
        self.logger.log("Starting data cleaning...")
        # Example cleaning process
        cleaned_data = data.dropna()
        self.logger.log("Data cleaning completed.")
        return cleaned_data

    def encode_features(self, data):
        self.logger.log("Starting feature encoding...")
        # Example encoding process
        encoded_data = pd.get_dummies(data)
        self.logger.log("Feature encoding completed.")
        return encoded_data
