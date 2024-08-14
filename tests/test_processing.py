import unittest
import pandas as pd
from data_processing.preprocessing import Preprocessing
from data_processing.config import config

class TestPreprocessing(unittest.TestCase):
    def test_clean_data(self):
        preprocessing = Preprocessing(config)
        data = pd.DataFrame({'col1': [1, 2, None], 'col2': [3, None, 4]})
        cleaned_data = preprocessing.clean_data(data)
        self.assertFalse(cleaned_data.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
