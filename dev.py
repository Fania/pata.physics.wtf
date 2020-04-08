#!flask/bin/python
from app import app

# import logging


if __name__ == "__main__":
    app.debug = True
    # use_reloader = False
    # handler = logging.StreamHandler()
    # handler.setLevel(logging.ERROR)
    # app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port=8001)
