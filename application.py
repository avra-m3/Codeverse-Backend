#!/usr/bin/python3

from functools import wraps
from flask import *
from flask_cors import CORS
from flask_restful import Api, Resource
from model.Users import Users as db_Users
from model.Challenges import Challenges as db_Challenges
from model.Problems import Problems as db_Problems 
from model.TestCases import TestCases as db_TestCases
from model.Collaborators import Collaborators as db_Collaborators
import db_config as cfg

application = Flask(__name__)
CORS(application)
api = Api(application)


@application.route('/')
def index():
    return Response('Online', status=200)

def validate_request(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.json

            if json_object is None:
                print(expected_args)
                abort(400)
                # message="Expected request body to contain JSON, try setting Content-Type to application/json")
            for arg in expected_args:
                if arg not in json_object:
                    print(arg)
                    abort(400)
                    # message="Missing argument '{}', required arguments for this endpoint {} ".format(arg, ",".join(
                    # expected_args)))
            return func(*args, **kwargs)

        return wrapper

    return decorator


class Problems(Resource):
    def get(self, problem_id=None):
        if problem_id is None:
            return "all problems"
        return "get problem" + problem_id


class Challenges(Resource):
    def get(self, challenge_id=None):
        if challenge_id is None:
            chal = db_Challenges()

            r = chal.listChallenges('InProgress')
            print(r)
            print(jsonify(r))
            # for item in result:
            #     print(item, type(item))
            # # print(result)
            return jsonify(r)
        return None

    def put(self, challenge_id=None):
        pass

    def post(self, challenge_id=None):
        pass


class Collaborators(Resource):
    def get(self, challenge_id, user_id=None):
        if user_id is None:
            abort(501)

    def put(self, challenge_id, user_id=None):
        if user_id is None:
            abort(501)

    def post(self, challenge_id, user_id=None):
        pass


class Users(Resource):
    def get(self, user_id=None):
        if user_id is None:

            abort(501)
        pass

    @validate_request('user_id', 'firstname', 'lastname')
    def put(self, user_id=None):
        data = request.json()
        user_id = user_id or data["user_id"]
        firstname = data['firstname']
        lastname = data['lastname']
        pass


api.add_resource(Problems, '/problems/<string:problem_id>', '/problems', '/problems/')
api.add_resource(Users, '/users/<string:user_id>', '/users', '/users/')
api.add_resource(Challenges, '/challenges/<string:challenge_id>' '/challenges/', '/challenges')
api.add_resource(Collaborators, '/challenges/<string:challenge_id>/collaborators/<string:user_id>',
                 '/challenges/<string:challenge_id>/collaborators/', '/challenges/<string:challenge_id>/collaborators')

if __name__ == '__main__':
    api.run()
