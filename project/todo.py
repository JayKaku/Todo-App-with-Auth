from flask import Flask, redirect, render_template, request, abort
from flask import Blueprint
from . import db
from jinja2 import TemplateNotFound
from project.models import Todo
from flask_login import login_required, current_user

todo = Blueprint('todo', __name__)


# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     desc = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     # __repr__ is used to repeat a class's objects as a string
#     def __repr__(self):
#         return f"{self.sno} - {self.title}"

# create  routes


@todo.route('/', methods=['GET', 'POST'])
@login_required
def hello_world():
    # return 'Hello, World!'
    if request.method == 'POST':
        # print(f"POST request with title {request.form['title']}")
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    # allTodo is the var name throught which data that is passed down to the template
    return render_template('index.html', allTodo=allTodo, name=current_user.name)


@todo.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@todo.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')

        todo = Todo.query.filter_by(sno=sno).first()

        todo.title = title
        todo.desc = desc

        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


# if __name__ == '__main__':
#     todo.run(debug=True)  # port=8000
