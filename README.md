
# Web Collider

Fania Raczinski + De Montfort University + 2015


## OVH VPS SETUP
Test for errors:

```nginx -t```

```service nginx reload```




## HOW TO AT HOME

- Activate venv ```workon newpatav``` (if virtualenvwrapper is installed)
- Win activate: ```venv\scripts\activate```
- unix activate: ```. venv/bin/activate```
- Start dev project ```python dev.py```
- Start live project ```python live.py``` (if avalailable)
- Stop project ```Ctrl + c```
- Deactivate ```deactivate```



## IMPORTANT
```python dev.py``` starts the local dev SERVER
```gunicorn live:app```  starts gunicorn server
live is the wsgi script in the main folder.
app is the name of the folder that contains the __init__.py and all the views.
```gunicorn -c guni.py live:app```


TO RUN IOCT SERVER 2016:
- screen
- . venv/bin/activate
- gunicorn -c guni.py wsgi:app

CHECK ERROR LOGS

any changes to the server IP port stuff:
restart apache using: ```apachectl graceful``` or ```apachectl restart```

if probs check ```apachectl configtest```
FIX ERRORS
RESTART APACHE



## IOCT SERVER
- ```ssh fraczinski@mnemosyne.ioct.dmu.ac.uk```
- mnemosyne.ioct.dmu.ac.uk
- username fraczinski
- password Green+99
- config: /etc/apache2/sites/pata.conf

http://mnemosyne.ioct.dmu.ac.uk/
- start server from: /Library/WebServer/share/pata/pata3


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
6. ```python dev.py``` python run.py
7. ```ctrl+a d```
8. ```exit```


## REQUIREMENTS

- Python 2.7.10
- Get requirements ```pip freeze > requirements.txt```
- Install from reqs ```pip install -r requirements.txt```

### Location of Python 2.7 (python2)
/usr/local/Cellar/python/2.7.10_2/bin/python2

virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>

http://www.bing.com/developers/s/APIBasics.html

## OLD PROTOTYPES

to check which python installation is used:
```python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"```

You can find out all the versions of python if you type python and then press TAB.

change path to local venv python if needed...
~/projectpath/venv/bin/python
!/usr/bin/python in manage.py


# TODO: Add to Solutions Log

# INSTALLING FROM SCRATCH
- install python 2.7.X
- install pip and virtualenv
- create venv and activate it
- install requirements
