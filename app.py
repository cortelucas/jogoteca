from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = '2d1d056b2b0272e6723dcb6a093b10c6'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
lista = [jogo1, jogo2]


@app.route('/')
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo="Novo Jogo")


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + " logou com sucesso")
        return redirect('/')
    else:
        flash('Não logado, tente novamente.')
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
