from flask import Flask, jsonify, request
from traffic_simulation import simulate_traffic_data
from model import TrafficModel

app = Flask(__name__)
traffic_model = TrafficModel()

# Train the model with simulated data
X, y = simulate_traffic_data()
traffic_model.train(X, y)

@app.route('/optimize_route', methods=['POST'])
def optimize_route():
    data = request.json
    current_time = data.get('time')
    current_weather = data.get('weather')
    
    traffic_congestion = traffic_model.predict_congestion(current_time, current_weather)
    route_suggestion = "Take the highway" if traffic_congestion < 1.5 else "Avoid the highway"
    return jsonify({
        'suggested_route': route_suggestion,
        'congestion_level': traffic_congestion
    })

if __name__ == '__main__':
    app.run(debug=True)
