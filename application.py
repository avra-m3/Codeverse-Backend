#!/usr/bin/python3
import os
import time
from functools import wraps

from flask import *
from flask_cors import CORS
from flask_restful import Api, Resource

import model
import sphere_integration as sph
from model.Challenges import Challenges as db_Challenges
from model.Problems import Problems as db_Problems
from model.Users import Users as db_Users

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
            result = challenges.listChallenges('Waiting')
            return jsonify(result)
        ch = model.Challenges().getChallenge(challenge_id)
        if ch is None:
            abort(400)
        return jsonify(ch)

    @validate_request('problem_id')
    def put(self, challenge_id=None):
        if challenge_id is not None:
            abort(400)
        req = request.json
        problem_id = req["problem_id"]
        challenges = db_Challenges()
        challenge_id = challenges.createChallenge(problem_id, "Waiting")
        return jsonify(challenges.getChallenge(challenge_id))

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
    def put(self, challenge_id, user_id):
        if user_id is None:
            abort(400)
        db = model.Collaborators()
        challenge_db = model.Challenges()
        challenge = challenge_db.getChallenge(challenge_id)
        if challenge is None:
            abort(400)
        if challenge["Status"] != "Waiting":
            print(challenge)
            abort(412)
        data = request.json
        result = db.createCollaborator(challenge_id=challenge_id, user_id=user_id, playbackStream=data["stream"])
        return jsonify(result)

    @validate_request()
    def post(self, challenge_id, user_id=None):
        pass
        if user_id is None:
            abort(400)
        data = request.json()
        if "code" in data:
            code = data["code"]
            challenge = model.Challenges().getChallenge(challenge_id)
            if challenge is None:
                abort(400)
            test_cases = model.TestCases().listTestCases(challenge["problem_id"])
            if test_cases is None or len(test_cases) < 1:
                abort(400)
            case = test_cases[0]
            code = case["Precode"] + code + case["Postcode"]
            id = sph.submit(code)
            db = model.Collaborators()
            colab = db.getCollaborator(challenge_id, user_id)
            if colab is None:
                abort(400)
            return jsonify(
                db.updateCollaborator(challenge_id, user_id, colab["PlaybackStream"], "running", time.time(), None,
                                      id))
        db = model.Collaborators()
        colab = db.getCollaborator(challenge_id, user_id)
        if colab is None:
            abort(400)
        if colab["Status"] != "running":
            return jsonify(colab)
        result, status = sph.poll(colab["SubmissionID"])
        if status:
            db.updateCollaborator(challenge_id, user_id, colab["PlaybackStream"], result, colab["submittedAt"],
                                  result["time"], colab["SubmissionID"])


class Users(Resource):
    def get(self, user_id=None):
        if user_id is None:
            abort(501)
        db = db_Users()
        return jsonify(db.getUser(user_id))

    @validate_request('firstname', 'lastname')
    def put(self, user_id=None):
        if user_id is not None:
            abort(400)
        data = request.json()
        firstname = data['firstname']
        lastname = data['lastname']
        db = db_Users()
        return jsonify(db.createUser(firstname, lastname))


class TestCode(Resource):
    def get(self, id):
        return sph.poll(id)

    @validate_request('source')
    def post(self):
        return sph.submit(source=request.json["source"])


api.add_resource(Problems, '/problems/<string:problem_id>', '/problems', '/problems/')
api.add_resource(Users, '/users/<string:user_id>', '/users', '/users/')
api.add_resource(Challenges, '/challenges/<string:challenge_id>', '/challenges/', '/challenges')
api.add_resource(Collaborators, '/challenges/<string:challenge_id>/collaborators/<string:user_id>',
                 '/challenges/<string:challenge_id>/collaborators/', '/challenges/<string:challenge_id>/collaborators')
api.add_resource(TestCode, '/testing/<string:id>', '/testing/')
if __name__ == '__main__':
    if os.getenv("PRODUCTION"):
        app.run(host='0.0.0.0', port=80)
    else:
        api.run()
