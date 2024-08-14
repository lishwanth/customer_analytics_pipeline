import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, config):
        self.data_path = config['data_path']
    
    def load_data(self):
        data = pd.read_csv(self.data_path)
        X = data[config['input_features']]
        y = data['Churn']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
