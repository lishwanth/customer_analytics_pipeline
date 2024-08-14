from utils.logger import Logger

class FeatureEngineering:
    def __init__(self, config):
        self.logger = Logger(config)
    
    def create_features(self, data):
        self.logger.log("Starting feature engineering...")
        # Example feature engineering process
        data['tenure_years'] = data['tenure'] / 12
        self.logger.log("Feature engineering completed.")
        return data
