import sys
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
sys.path.append('../../')
from src.main.pi_arm import PiArm

app = Flask(__name__)
api = Api(app)

class Robot(Resource):
    def get(self):
        return {'robot': 'hola como tai ...'}  # Fetches first column that is Employee ID

class Up(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "s u 20"
        piarm.parse_joints(input_primitive_joints)
        return {'robot': 'move'}

class Down(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "s d 20"
        piarm.parse_joints(input_primitive_joints)
        return {}

class Right(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "w r 20"
        piarm.parse_joints(input_primitive_joints)
        return {}

class Left(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "w l 20"
        piarm.parse_joints(input_primitive_joints)
        return {}

api.add_resource(Robot, '/hola')  # Route_1
api.add_resource(Up, '/up')  # Route_1
api.add_resource(Down, '/down')
api.add_resource(Right, '/right')
api.add_resource(Left, '/left')


if __name__ == '__main__':
    app.run(port='5002',host='0.0.0.0')

