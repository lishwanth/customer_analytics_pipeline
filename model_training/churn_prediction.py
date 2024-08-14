from model_training.model import ChurnModel
from utils.data_loader import DataLoader

class ChurnPrediction:
    def __init__(self, config):
        self.data_loader = DataLoader(config)
        self.model = ChurnModel(config)
    
    def execute(self):
        X_train, X_test, y_train, y_test = self.data_loader.load_data()
        self.model.train(X_train, y_train)
        evaluation = self.model.evaluate(X_test, y_test)
        print(f"Model Evaluation: {evaluation}")
