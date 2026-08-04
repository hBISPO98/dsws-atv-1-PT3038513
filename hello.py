
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, request, make_response, abort

app = Flask(__name__)

# rota 1: hello world
@app.route('/')
def index():
    return f'<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

# rota 2: hello name
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

# rota 3: contexto de requisição
@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Your browser is {user_agent}</p>'

# rota 4: status diferente - 400
@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return '<p>Bad request</p>', 400

# rota 5: objeto resposta
@app.route('/objetoresposta')
def objeto_resposta():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('language','pt-BR')
    return response

# rota 6: redirecionamento para o site IFSP
@app.route('/ifsp')
def redirecionar_ifsp():
    return redirect('https://ptb.ifsp.edu.br/')

# rota 7: cancelamento
@app.route('/cancelar')
def cancelar_requisicao():
    abort(404)