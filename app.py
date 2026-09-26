from flask import Flask, render_template, request, redirect, url_for
from controllers.classificacao_controller import ClassificacaoController

app = Flask(__name__)
controller = ClassificacaoController()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/classificar", methods=["POST"])
def classificar():
    texto = request.form.get("texto", "")
    resultado = controller.processar_solicitacao(texto)
    return render_template("index.html", resultado=resultado)

@app.route("/historico", methods=["GET"])
def historico():
    registros = controller.obter_historico()
    return render_template("index.html", historico=registros)

if __name__ == "__main__":
    app.run(debug=True)