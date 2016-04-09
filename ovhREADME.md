# OVH VPS

Debian Jessie

[Guide 1](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04) (Skip Upstart part)
[Guide 2](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04)

## Minimal Working Example

1. ```apt-get update```
2. ```apt-get install python-pip python-dev nginx```
3. ```pip install virtualenv```
4. ```virtualenv venv```
5. ```. venv/bin/activate```
6. ```pip install gunicorn flask nltk microsofttranslator flickrapi```
7. ```nano hello.py```
```from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
```
8. ```nano wsgi.py```
```
from myproject import application

if __name__ == "__main__":
    application.run()
```
9. ```gunicorn --bind 0.0.0.0:8000 wsgi```
10. ```nano /etc/nginx/sites-available/hello```
```
server {
    listen 80;
    server_name hello.itu24.com;

    root /path/to/hello;

    access_log /path/to/hello/logs/access.log;
    error_log /path/to/hello/logs/error.log;

    location / {
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        if (!-f $request_filename) {
            proxy_pass http://127.0.0.1:8000;
            break;
        }
    }
}
```
11. ```ln -s /etc/nginx/sites-available/hello /etc/nginx/sites-enabled/```
12. ```nginx -t```
13. ```service nginx reload```
14. Check if it works in browser.


## Venv nltk data
1. ```nano /home/pata/venv/lib/python2.7/site-packages/nltk/data.py```
2. find path for unix
3. add ```str('/home/pata/nltk_data'),```
