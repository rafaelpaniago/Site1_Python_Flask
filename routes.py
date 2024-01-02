from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    projeto1 = {"projeto": "1° projeto desenvolvido utilizando Flask"}
    detalhes = {"paginas": "Duas páginas criadas (home, contato)", "objetivo": "Criar primeiro site"}
    return render_template('index.html', projeto1=projeto1, detalhes=detalhes)

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Aqui, basicamente estamos definindo as rotas da nossa aplicação.
