from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # avoid Cross-Origin Resource Sharing (CORS) errors

# Declare routes by following the examples below
@app.route('/')
def index():
    return "<h1>Hello, world!</h1>" # return this data to the client

@app.route('/api/v1.0/hello', methods=['GET'])
def get_tasks():
    return jsonify({'name': "Hello, client!"})

if __name__ == '__main__':
    app.run(debug=True)