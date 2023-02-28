from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/name', methods=['GET'])
def name():
    if (request.method == 'GET'):
        data = {"data": "Vinod here!!"}
        return jsonify(data)
    
@app.route('/', methods=['GET'])
def index():
    if (request.method == 'GET'):
        data = {"data": "Hello World!"}
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
