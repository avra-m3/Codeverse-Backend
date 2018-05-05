from functools import wraps

from flask import *
from flask_cors import CORS

application = Flask(__name__)
CORS(application)


@application.route('/')
def index():
    return Response('Online', status=200)


def validate_request(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.json

            print(expected_args)

            if json_object is None:
                abort(400)
            for arg in expected_args:
                if arg not in json_object:
                    abort(412)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@application.route('/register', methods=['POST', 'PUT'])
@validate_request('user_id', 'firstname', 'lastname')
def register():
    data = request.json


if __name__ == '__main__':
    application.run()
