# implementar uma solução em python flask que faça:
# 1 - exiba a mensagem "olá programadores" no endereço raiz de uma página
# web  e apareça o link "/User/Usuario"
# 2 - exiba a mensagem "olá usuário" no endereço "/User/ e exiba a mensagem "Altere o endereço do browser e recarregue a pagina"
# 3 - exiba a mensagem : "olá usuario!" no endereço "/user/nome_do_usuario" de uma página web.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, Programadores!</h1>'
    link = '<p><a href= "user/Usuário"> Clique aqui!</a></p>'
    return boas_vindas + link

@app.route('/User/')
@app.route('/User/<nome>')
def user(nome=Usuário):
    personalizar = f'<h1> Olá, {nome}!</h1>'
    insrtucao = '<p>Altere o nome no <em> endereço do browser</em> \ e recarregue a página. </p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run(debug=true)