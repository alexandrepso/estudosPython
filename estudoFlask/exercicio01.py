# implementar uma solução em python com flask que faça:

# 1 - exiba uma mensagem "pagina principal" no endereço raiz de uma pagina web.
# 2 - exiba uma mensagem "Olá mundo" no endereço "/Olá/" de uma página web.
# 3 - exiba uma mensagem " Olá usuário!" no endereço "/Olá/nome_do_usuário" de uma pafina web.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Página principal."

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return "Olá,"+ nome + "!"

if __name__=='__main__':
    app.run()
    
