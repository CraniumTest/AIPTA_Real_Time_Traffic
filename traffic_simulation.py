import random
import numpy as np

def simulate_traffic_data(num_samples=1000):
    # Simulate traffic data with random time (0-23 for hours) and weather conditions
    time = np.random.randint(0, 24, num_samples)
    weather = np.random.choice(['sunny', 'rainy', 'cloudy'], num_samples)
    congestion = np.array([random.uniform(0.5, 2) if w == 'sunny' else random.uniform(1, 3) for w in weather])
    
    # Construct a dataset
    X = list(zip(time, weather))
    y = congestion
    
    return X, y
