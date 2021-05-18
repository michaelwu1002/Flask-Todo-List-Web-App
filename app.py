from flask import Flask, render_template
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
    # show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

if __name__ == "__main__":
    db.create_all()

    curr_date = date.today().strftime("%m/%d/%Y")
    new_todo_deadline = Todo(title="todo 1", complete=False, deadline=curr_date)
    db.session.add(new_todo_deadline)
    db.session.commit()

    app.run(debug=True)