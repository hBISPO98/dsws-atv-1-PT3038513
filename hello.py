
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

# page 1: hello world
@app.route('/')
def user(name):
    return f'<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

# page 2: hello name
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'