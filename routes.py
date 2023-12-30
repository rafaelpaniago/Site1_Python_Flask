from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Rafael"
    dados = {"profissao": "Analista de Dados", "canal": "Ivd"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Aqui, basicamente estamos definindo as rotas da nossa aplicação.
