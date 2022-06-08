pip install virtualenv
virtualenv env
Set-ExecutionPolicy unrestricted  // conditional
.\env\Scripts\activate.bat or ps1
activate

// for db
pip install flask-sqlalchemy

// instead of pip list to check dependencies in virtualenv
python -m pip list

// run cmd; hello could be file name or folder(__init__.py)
set FLASK_APP=project
set FLASK_DEBUG=1
flask run

// create db and app from python cmd
>>> from yourapp import db, create_app
>>> db.create_all(app=create_app())

// create db and app from python package
>>> from project import db, create_app, models   
>>> db.drop_all()
>>> app = create_app()
>>> app.app_context().push()                      
>>> db.create_all(app=create_app())
>>> from project.models import User,Todo
>>> u0 = User(email='user0@todos.com',password_hash='123456',name='user_0')
>>> db.session.add(u0)
>>> db.session.commit()
