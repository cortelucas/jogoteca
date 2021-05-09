from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import Jogo, Usuario
from dao import JogoDao
import mysql.connector

app = Flask(__name__)
app.secret_key = '2d1d056b2b0272e6723dcb6a093b10c6'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="0612AnLu+",
    database="jogoteca",
    auth_plugin='mysql_native_password'
)

jogo_dao = JogoDao(db)


u1 = Usuario('lucas', 'Lucas Corte', '2801')
u2 = Usuario('andressa', 'Andressa Karino', '0709')
u3 = Usuario('leo', 'Leo Corte', '2405')

usuarios = {u1.id: u1, u2.id: u2, u3.id: u3}

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
lista = [jogo1, jogo2]


@app.route('/')
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'), proxima=url_for('novo'))
    return render_template('novo.html', titulo="Novo Jogo")


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
        flash(usuario.nome + " logou com sucesso")
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
