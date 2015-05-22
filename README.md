
# Web Collider

Fania Raczinski + De Montfort University + 2014

## HOW TO

- Activate ```workon newpatav```
- Start project ```python run.py```
- Stop project ```Ctrl + c```
- Deactivate ```deactivate```


## IOCT SERVER
- ```ssh fraczinski@mnemosyne.ioct.dmu.ac.uk```
- mnemosyne.ioct.dmu.ac.uk
- username fraczinski
- password Green+99
- config: /etc/apache2/sites/0003_146.227.57.110_80_mnemosyne.ioct.dmu.ac.uk.conf

http://mnemosyne.ioct.dmu.ac.uk/fania/
(from root)
/Library/WebServer/share/pata/fania/index.html

http://mnemosyne.ioct.dmu.ac.uk/
/Library/WebServer/share/pata/

start screen: ```screen```
reconnect: ```screen -R```
detach:	```ctrl+a d```
list screens: ```screen -list```
kill screen: ```exit```

### IOCT setup

1. ```ssh fraczinski@mnemosyne.ioct.dmu.ac.uk```
2. ```Green+99```
3. cd root /Library/WebServer/share/pata/
4. ```screen```
5. ```. venv/bin/activate```
6. ```python run.py```
7. ```ctrl+a d```
8. ```exit```


## REQUIREMENTS

- Get requirements ```pip freeze > requirements.txt```
- Install from reqs ```pip install -r requirements.txt```

### WINDOWS

- Flask==0.10.1
- Jinja2==2.7.3
- MarkupSafe==0.23
- PyYAML==3.11
- Werkzeug==0.9.6
- flickrapi==1.4.4
- gdata==2.0.18
- itsdangerous==0.24
- microsofttranslator==0.6
- nltk==3.0.0b1
- requests==2.3.0

### MAC

- Flask==0.10.1
- Jinja2==2.7.3
- MarkupSafe==0.23
- Werkzeug==0.9.6
- flickrapi==1.4.4
- gdata==2.0.18
- itsdangerous==0.24
- microsofttranslator==0.6
- nltk==3.0.0b1
- requests==2.3.0
- wsgiref==0.1.2

## HEROKU

heroku toolbelt 3.9.6
```heroku update````
