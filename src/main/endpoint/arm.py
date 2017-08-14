import sys
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify

sys.path.append('../../')
from src.main.pi_arm import PiArm

app = Flask(__name__)
api = Api(app)


class HealtCheck(Resource):
    def get(self):
        return {'robot': 'hola como tai ...'}


class Move(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "s u 20"
        piarm.parse_joints(input_primitive_joints)
        return {'robot': 'move'}





api.add_resource(HealtCheck, '/healtCheck')
api.add_resource(Move, 'move')


if __name__ == '__main__':
    app.run(port='5002', host='0.0.0.0')