#### Database ORM with SQLAlchemy
Install SQLAlchemy as:
```
pipenv install SQLAlchemy --skip-lock
```

#### Database Migrations
**alembic** is database migration tools for **sqlalchemy**. Install it using follwoing commands.
```
pipenv install alembic --skip-lock
```

###### Init alembic
```
alembic init database
```

###### Create a migration
```
alembic revision -m "create users table"
```

###### Run Migration
```
alembic upgrade
```

#### Model
Model is a python class that maps to a database table in DBMS, and object maps to a row of database table.

Consider a `Thread` model to create. At first thread model is created under the folder
`app/domain/artefact/Thread.py` as

```python
from bootstrap.app import TableName
from bootstrap.app import db


class Thread(db.Model):
    __tablename__ = TableName.USER

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.text)
```
