from flask import Flask, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
