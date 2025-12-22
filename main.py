from flask import Flask,request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

    # def to_dict(self):
    #     return {"id": self.id, "title": self.title}


@app.get("/")
def index():
    return {"status": "ok:)"}


@app.get("/todos/list")
def todos_list():
    todos = Todo.query.order_by(Todo.id.desc()).all()
    return render_template("list.html", todos=todos)


@app.post("/todos/create")
def todos_create():
    title = (request.form.get("title") or "").strip()
    if not title:
        return redirect(url_for("todos_list"))

    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("todos_list"))


@app.post("/todos/delete/<int:todo_id>")
def todos_delete(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("todos_list"))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)