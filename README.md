# Flask Todo List

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)


<a name="general-info"></a>
### General Info
***
This is a basic flask web app that serves the purpose of a todo-list. Functionalities include: adding tasks (and displaying by deadline), updating a task status, deleting the a task, and clearing all tasks.
![Todo List App Screenshot](https://github.com/michaelwu1002/flask_todo_list/blob/main/Screen%20Shot%202021-05-19%20at%203.35.14%20PM.png)

<a name="technologies"></a>
### Technologies
***
A list of technologies used within the project:
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
* [Semantic UI](https://semantic-ui.com/)

## Installation
***
A little intro about the installation. 
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```

Have Python3 installed, navigate to the project directory, and create & activate the flask environment. Next, install flask.

On Mac:
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install flask
```
On Windows:
```
> py -3 -m venv venv
> venv/Scripts/activate
> pip install flask
```
Next, to run the Todo app, set the following environment variables.

On Mac:
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```
On Windows:
```
> set FLASK_APP=app.py
> set FLASK_ENV=development
```

And finally, to run the Todo web app, enter either of the following into your terminal:
```
$ flask run
```
or
```
$ python app.py
```
Afterwards, you should see something like this in the terminal:

