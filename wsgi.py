from app import app

from waitress import serve

if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001)  
    serve(app, host='127.0.0.1', port=8001)  