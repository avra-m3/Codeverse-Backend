from flask import *
from flask_cors import CORS

application = Flask(__name__)
CORS(application)


@application.route('/')
def index():
    return Response('Online', status=200)


if __name__ == '__main__':
    application.debug = True
    application.run()
