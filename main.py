from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Olá, Mundo!</h1><h2>Seja bem-vindo</h2>'

@app.route('/pokemon/<name>/<type>')
def teste(name, type):
  return f'O nome do pokemon é {name}, seu tipo é {type}'

@app.route('/soma/<num1>/<num2>')
def soma(num1, num2):
  soma = int(num1) + int(num2)
  return f'A soma é {soma}'

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/pokemon/<name>')
def pokemon(name):
  return render_template(
    'pokemon.html', 
    name=name
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0')