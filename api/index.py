from flask import Flask, jsonify, request
import joblib
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), 'iris_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/json')
def json_data():
    dummy_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com"
    }
    return jsonify(dummy_data)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]])
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
