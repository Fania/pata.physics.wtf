# Web Collider

Fania Raczinski + De Montfort University + 2015


![screenshot](https://raw.githubusercontent.com/fania/pata.physics.wtf/master/screenshot.png)

## OVH VPS SETUP

IP: 92.222.73.21

Test for errors:

```nginx -t```
```service nginx reload```

Run on Ubuntu:

```screen```
```. venv/bin/activate```
```gunicorn -c guni.py live:app```
```ctrl+a+d```


---

git log --graph --full-history --all --date=format:"%a %d %b %Y" --pretty=format:"%h%x20%x20%ad%x09%d%x20%s" > prettyprint.txt

## HOW TO AT HOME

- Activate venv ```workon newpatav``` (if virtualenvwrapper is installed)
- Win activate: ```venv\scripts\activate```
- unix activate: ```. venv/bin/activate```
- Start dev project ```python dev.py```
- Start live project ```python live.py``` (if avalailable)
- Stop project ```Ctrl + c```
- Deactivate ```deactivate```


## IMPORTANT
```python run.py``` starts the local dev SERVER
```gunicorn wsgi:app```  starts gunicorn server
wsgi is the wsgi script in the main folder.
app is the name of the folder that contains the __init__.py and all the views.
```gunicorn -c guni.py wsgi:app```


## IOCT SERVER
- ```ssh fraczinski@mnemosyne.ioct.dmu.ac.uk```
- mnemosyne.ioct.dmu.ac.uk
- username fraczinski
- password Green+99
- config: /etc/apache2/sites/pata.conf

http://mnemosyne.ioct.dmu.ac.uk/
/Library/WebServer/share/pata/pata3


## SCREEN
start screen: ```screen```
reconnect: ```screen -R```
detach:	```ctrl+a d```
list screens: ```screen -list```
kill screen: ```exit```


### IOCT setup

1. ```ssh fraczinski@mnemosyne.ioct.dmu.ac.uk```
2. ```Green+99```
3. cd root /Library/WebServer/share/pata/pata3
4. ```screen```
5. ```. venv/bin/activate```
6. ```python run.py```
7. ```ctrl+a d```
8. ```exit```


## REQUIREMENTS

- Python 2.7.10
- Get requirements ```pip freeze > requirements.txt```
- Install from reqs ```pip install -r requirements.txt```

### Location of Python 2.7 (python2)
/usr/local/Cellar/python/2.7.10_2/bin/python2

virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>