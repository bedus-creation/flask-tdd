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