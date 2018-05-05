from functools import wraps

from flask import *
from flask_cors import CORS
from flask_restful import Api, Resource

import sphere_integration as sph

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
        pass

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


class Test(Resource):
    def get(self, challenge_id, user_id, test_id):
        result = sph.poll(test_id)
        return result

    @validate_request('source')
    def put(self, challenge_id, user_id, test_id):
        data = request.json()
        lang = "language" in data and data["language"] or 4
        return sph.submit(data["source"], lang=lang)


api.add_resource(Problems, '/problems/<string:problem_id>', '/problems', '/problems/')
api.add_resource(Users, '/users/<string:user_id>', '/users', '/users/')
api.add_resource(Challenges, '/challenges/<string:challenge_id>' '/challenges/', '/challenges')
api.add_resource(Collaborators, '/challenges/<string:challenge_id>/collaborators/<string:user_id>',
                 '/challenges/<string:challenge_id>/collaborators/', '/challenges/<string:challenge_id>/collaborators')
api.add_resource(Test, '/challenges/<string:challenge_id>/collaborators/<string:user_id>/compile/<string:test_id>')

if __name__ == '__main__':
    api.run()
