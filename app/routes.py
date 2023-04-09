from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    nome = 'Kika'
    dados = {'profissão': 'Professora', 'canal': 'Profa. Alba Lopes'}
    return render_template('index.html', nome= nome, dados= dados)


@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    return 'Usuário: {} e senha {}'.format(usuario, senha)
