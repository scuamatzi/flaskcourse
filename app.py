from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

import os
from flask_sqlalchemy import SQLAlchemy

DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "notes.sqlite")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}"


@app.route("/")
def hello():
    # return "Hello World from Flask!"
    role = "admin"
    notes = ["nota 1", "nota 2", "nota 3"]
    return render_template("home.html", role=role, notes=notes)
    # return "Hello World"


@app.route("/acerca-de")
def about():
    return "Esto es una app de notas"


@app.route("/contacto", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente.", 201
    return "Página de contacto"


@app.route("/api/info")
def api_info():
    data = {"nombre": "Notes App", "version": "1.1.1"}
    return jsonify(data), 200
    # return jsonify(data)


@app.route("/confirmacion")
def confirmation():
    return "Recibido"


@app.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        note = request.form.get("note", "No encontrada")
        # print(note)
        return redirect(url_for("confirmation", note=note))
    return render_template("note_form.html")


# if __name__ == "__main__":
#    app.run(debug=True)
