# Web Forum

Using Flask to build web forum

Integration with Flask-SQLalchemy

## Installation
Install with pip:

```
$ pip install -r requirements.txt
```

## Database setup
```
$ flask shell
>>> from app.extensions import db
>>> from app.models.post import Post
>>> db.create_all()
```

## Run Flask
```
$ flask run
