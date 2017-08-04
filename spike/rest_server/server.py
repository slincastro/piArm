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
        return {'robot': 'hola como tai ...'}


class Up(Resource):
    def get(self):
        piarm = PiArm(None)
        joint = request.query_string
        print "Joint " + joint
        input_primitive_joints = joint + " u 20"
        piarm.parse_joints(input_primitive_joints)
        return {'robot': 'move'}


class Down(Resource):
    def get(self):
        piarm = PiArm(None)
        joint = request.query_string
        print "Joint " + joint
        input_primitive_joints = joint + " d 20"
        piarm.parse_joints(input_primitive_joints)
        return {}


class Right(Resource):
    def get(self):
        piarm = PiArm(None)
        joint = request.query_string
        print "Joint " + joint
        input_primitive_joints = joint + " r 20"
        piarm.parse_joints(input_primitive_joints)
        return {}


class Left(Resource):
    def get(self):
        piarm = PiArm(None)
        joint = request.query_string
        input_primitive_joints = joint + " l 20"
        piarm.parse_joints(input_primitive_joints)
        return {}


class Open(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "g o 20"
        piarm.parse_joints(input_primitive_joints)
        return {}


class Close(Resource):
    def get(self):
        piarm = PiArm(None)
        input_primitive_joints = "g c 20"
        piarm.parse_joints(input_primitive_joints)
        return {}


api.add_resource(Robot, '/hola', endpoint='bar')  # Route_1
api.add_resource(Up, '/up')  # Route_1
api.add_resource(Down, '/down')
api.add_resource(Right, '/right')
api.add_resource(Left, '/left')
api.add_resource(Open, "/open")
api.add_resource(Close, "/close")

if __name__ == '__main__':
    app.run(port='5002', host='0.0.0.0')
