#!/usr/bin/python3

from functools import wraps

from flask import *
from flask_cors import CORS
from flask_restful import Api, Resource

import model
from model.Challenges import Challenges as db_Challenges
from model.Users import Users as db_Users
from model.Problems import Problems as db_Problems

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
        problems = db_Problems()
        if problem_id is None:
            result = problems.listProblems()
        else:
            result = problems.getProblem(problem_id)

        return jsonify(result)


class Challenges(Resource):
    def get(self, challenge_id=None):
        if challenge_id is None:
            challenges = db_Challenges()
            result = challenges.listChallenges('InProgress')
            return jsonify(result)
        return None

    @validate_request('problem_id')
    def put(self, challenge_id=None):
        req = request.json
        problem_id = req["problem_id"]
        challenges = db_Challenges()
        challenge_id = challenges.createChallenge(problem_id, "InProgress")
        return challenge_id, 200

    @validate_request('status')
    def post(self, challenge_id=None):
        if challenge_id is None:
            abort(400)
        req = request.json
        new_status = req["status"]
        challenges = db_Challenges()
        challenges.updateChallengeStatus(challenge_id, new_status)


class Collaborators(Resource):
    def get(self, challenge_id, user_id=None):
        db = model.Collaborators()
        if user_id is None:
            result = db.listCollaborators(challenge_id)
        else:
            result = db.getCollaborator(challenge_id, user_id)
        return jsonify(result)

    @validate_request('stream')
    def put(self, challenge_id, user_id=None):
        if user_id is not None:
            abort(400)
        db = model.Collaborators()
        challenge_db = model.Challenges()
        challenge = challenge_db.getChallenge(challenge_id)
        if challenge is None:
            abort(400)
        if challenge["status"] not in ["created", "waiting"]:
            abort(412)
        data = request.json()
        result = db.createCollaborator(challenge_id, user_id, data["stream"], None, None, None, None)
        if len(challenge_db.listChallenges(challenge_id)) >= 2:
            challenge_db.updateChallengeStatus(challenge_id, "in progress")
        else:
            challenge_db.updateChallengeStatus(challenge_id, "waiting")

    @validate_request('code')
    def post(self, challenge_id, user_id=None):
        if user_id is None:
            abort(400)
        db = model.Collaborators()
        db.updateCollaborator(challenge_id, user_id)


class Users(Resource):
    def get(self, user_id=None):
        if user_id is None:
            abort(501)
        db = db_Users()
        return jsonify(db.getUser(user_id))

    @validate_request('firstname', 'lastname')
    def put(self, user_id=None):
        if user_id is None:
            abort(400)
        data = request.json
        firstname = data['firstname']
        lastname = data['lastname']
        print(firstname, lastname, user_id)
        db = db_Users()
        return jsonify(db.createUser(user_id, firstname, lastname))


api.add_resource(Problems, '/problems/<string:problem_id>', '/problems', '/problems/')
api.add_resource(Users, '/users/<string:user_id>', '/users', '/users/')
api.add_resource(Challenges, '/challenges/<string:challenge_id>', '/challenges/', '/challenges')
api.add_resource(Collaborators, '/challenges/<string:challenge_id>/collaborators/<string:user_id>',
                 '/challenges/<string:challenge_id>/collaborators/', '/challenges/<string:challenge_id>/collaborators')

if __name__ == '__main__':
    api.run()
