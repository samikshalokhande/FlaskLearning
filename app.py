from turtle import title
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo_db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(800), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/")
def hello_world():
    todo = ToDo(title="FirstToDo" , desc="Start Investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    allTodo = ToDo.query.all()
    # return a html from templates
    # we are using jinja2 template and sending a variable to index.html page 
    return render_template('index.html', allTodo=allTodo)
    # return "<p>Hello, World!</p>"

@app.route("/show")
def products():
    allTodo = ToDo.query.all()
    print(allTodo)
    return "<p>Products Page!</p>"

if __name__ == "__main__":
    # we can change host and port here
    app.run(debug=True, port=3080)