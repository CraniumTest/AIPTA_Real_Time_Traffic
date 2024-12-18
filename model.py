from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import numpy as np

class TrafficModel:
    def __init__(self):
        self.model = LinearRegression()
        self.encoder = OneHotEncoder()
    
    def train(self, X, y):
        # Encode categorical weather data
        time = np.array([x[0] for x in X]).reshape(-1, 1)
        weather = self.encoder.fit_transform([[x[1]] for x in X]).toarray()
        X_transformed = np.hstack((time, weather))
        self.model.fit(X_transformed, y)
        
    def predict_congestion(self, time, weather):
        weather_encoded = self.encoder.transform([[weather]]).toarray()
        X = np.hstack(([time], weather_encoded))
        return self.model.predict([X])[0]
