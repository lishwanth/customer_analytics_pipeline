
from utils.logger import Logger
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class ModelEvaluation:
    def __init__(self, config):
        self.logger = Logger(config)
    
    def evaluate(self, model, X_test, y_test):
        self.logger.log("Starting model evaluation...")
        y_pred = model.predict(X_test)
        y_pred = (y_pred > 0.5).astype(int)
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        self.logger.log(f"Accuracy: {accuracy}")
        self.logger.log(f"Precision: {precision}")
        self.logger.log(f"Recall: {recall}")
        self.logger.log(f"F1 Score: {f1}")
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
