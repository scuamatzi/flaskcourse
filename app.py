from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask!"
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


# if __name__ == "__main__":
#    app.run(debug=True)
