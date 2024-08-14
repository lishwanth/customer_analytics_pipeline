import unittest
from data_ingestion.ingestion import DataIngestion
from data_ingestion.config import config

class TestDataIngestion(unittest.TestCase):
    def test_ingestion(self):
        ingestion = DataIngestion(config)
        result = ingestion.start_ingestion()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
