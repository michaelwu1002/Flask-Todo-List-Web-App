from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    deadline = db.Column(db.String(20))

@app.route('/')
def index():
    # show all todos by deadline order
    todo_list = Todo.query.order_by(Todo.deadline).all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    # add new item to todo list
    title = request.form.get("title")
    deadline = request.form.get("deadline")
    new_todo_deadline = Todo(title=title, complete=False, deadline=deadline)
    db.session.add(new_todo_deadline)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    # update item in todo list
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # delete item in todo list
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/clear', methods=["POST"])
def clear():
    # clear all items from todo list
    Todo.query.delete()
    db.session.commit()
    return redirect(url_for("index"))
    

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)