from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "segredo"

API_URL = "http://127.0.0.1:8000/clientes"


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    dados = {
        "nome": request.form.get("nome"),
        "email": request.form.get("email"),
        "telefone": request.form.get("telefone"),
        "cidade": request.form.get("cidade"),
    }

    try:
        response = requests.post(API_URL, json=dados)

        if response.status_code == 200:
            flash("Cliente cadastrado com sucesso!", "success")
        else:
            flash(f"Erro ao cadastrar: {response.text}", "error")

    except Exception as e:
        flash(f"Erro de conexão com API: {str(e)}", "error")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
