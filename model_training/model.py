import tensorflow as tf
from utils.logger import Logger

class ChurnModel:
    def __init__(self, config):
        self.logger = Logger(config)
        self.model = self.build_model()
    
    def build_model(self):
        self.logger.log("Building churn prediction model...")
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(len(config['input_features']),)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model
    
    def train(self, X_train, y_train):
        self.logger.log("Starting model training...")
        self.model.fit(X_train, y_train, epochs=10, batch_size=32)
        self.logger.log("Model training completed.")
    
    def evaluate(self, X_test, y_test):
        self.logger.log("Evaluating the model...")
        return self.model.evaluate(X_test, y_test)
