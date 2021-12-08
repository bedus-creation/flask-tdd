# Installation
Before get started be sure you have all the requirements installed in your environments.
* Python
* pipenv

#### Create new virtual environment using pipenv.
```
pipenv shell
```

#### Install Flask 
```
pipenv install flask
```

### Application Run
Export flask app as:
```
export FLASK_APP=run.py
```
Further run app as:
```
flask run
```

### Testing
```
python -m pytest
```
