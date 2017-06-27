# run.py

import os

from app import flaskapp

config_name = os.getenv('FLASK_CONFIG')

if __name__ == '__main__':
    flaskapp.run('0.0.0.0', 5008, debug=True, threaded=True)