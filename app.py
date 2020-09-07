# Standard library imports
from flask import Flask, Response, request
from json import dumps, loads
from flask_cors import CORS

SECRET_MESSAGE = 'Mensaje Secreta'
API_PORT = '5000'
API_VERSION = '1.0'

base_route = '/api/' + API_VERSION + '/'

app = Flask(__name__)
CORS(app, resources={r'/api/*': {'origins': '*', 'expose_headers': 'Access-Token'}})

@app.route('/', methods=['GET'])
def root():
    resp = { 'Root': 'root'}
    return Response(dumps(resp), mimetype='application/json', status='200')

@app.route(base_route, methods=['GET'])
def welcome():
    resp = { 'msg': 'Hello World'}
    return Response(dumps(resp), mimetype='application/json', status='200')

@app.route( base_route + '<string:coin>', methods=['GET'])
def api_coin(coin: str):
    print('string = ' + coin)
    resp = { 'msg': 'Your coin is: ' + coin }
    return Response(dumps(resp), mimetype='application/json', status='200')
    
@app.route(base_route + 'security/user/login/email', methods=['POST'])
def get_secret_message():
    data = loads(request.data)
    print('email: ' + data['email'])
    print('password: ' + data['password'])
    resp = {'message': SECRET_MESSAGE}
    return Response(dumps(resp), mimetype='application/json', status='401')

if __name__=='__main__':
    app.run(port=API_PORT, debug=True)
