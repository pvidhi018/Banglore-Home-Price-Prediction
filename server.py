from flask import Flask, request, jsonify
import util
import logging

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

logging.basicConfig(level=logging.DEBUG)
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    received_data = request.get_data(as_text=True)
    app.logger.info("Received data: %s", received_data)

    data = request.get_json()
    app.logger.info("Parsed JSON data: %s", data)

    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    print("Starting Flask Server For Home Price Prediction...")
    app.run()
