from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = 'Ana Eliza'
    return render_template('index.html')
