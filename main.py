from flask import Flask, render_template, request, jsonify
from aria import Aria

app = Flask(__name__)
ia = Aria()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mensaje", methods=["POST"])
def mensaje():
    datos = request.get_json()
    entrada = datos.get("mensaje", "")
    lang = datos.get("idioma", "es")
    ia.set_language(lang)
    respuesta = ia.procesar_entrada(entrada)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
