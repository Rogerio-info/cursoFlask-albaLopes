from app import app

@app.route('/')
@app.route('/index')
def index():
    nome = 'Ana Eliza'
    return '''
    <html>
        <head><title>Página Inicial</title></head>
        <body>
            <h2>Hello ''' +nome+ ''', bem vindo ao flask.</h2>
        </body>
    </html>
    '''


