from flask import Flask, render_template, request
from AnalisadorLexico import AnalisadorLexico
Analisador = AnalisadorLexico

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/', methods=['POST'])
def homePOST():
    if request.form['nome'] != '':
        nome = request.form['nome']
    else:
        nome = "default"

    text = request.form['texto']
    Analisador.salvar_codigo(nome,text)
    analizer = Analisador(nome,text)
    dado = analizer.separador()
    codigo = analizer.texto
    return render_template("home.html",dado=dado,codigo=text,nome=nome)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)