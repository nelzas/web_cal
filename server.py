import os
import pathlib

from bottle import route, run, static_file

PORT = int(os.environ.get("PORT", 5000))
BASE_PATH = pathlib.Path(__file__).parent


@route('/')
def home():
    return 'Hello world! <img src="static/python.png"/>'


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=str(BASE_PATH / 'static'))


run(host='0.0.0.0', port=PORT)
