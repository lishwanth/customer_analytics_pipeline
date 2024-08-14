import logging

class Logger:
    def __init__(self, config):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(config.get('logger_name', 'customer_analytics'))
    
    def log(self, message):
        self.logger.info(message)
