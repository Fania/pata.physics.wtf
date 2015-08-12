#!flask/bin/python
from app import app

if __name__ == "__main__":
    app.debug = True
    # use_reloader = False
    app.run()
