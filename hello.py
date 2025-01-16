from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disciplinas')
def disciplinas():
    disciplinas = [
        {'nome': 'DSWA5', 'semestre': '5° semestre'},
        {'nome': 'PTBDSWS', 'semestre': '4° semestre'},
        {'nome': 'GPSA5', 'semestre': '5° semestre'},
    ]
    return render_template('disciplinas.html', disciplinas=disciplinas)

@app.route('/professores')
def professores():
    return render_template('blank.html')

@app.route('/alunos')
def alunos():
    return render_template('blank.html')

@app.route('/cursos')
def cursos():
    return render_template('blank.html')

@app.route('/ocorrencias')
def ocorrencias():
    return render_template('blank.html')

if __name__ == '__main__':
    app.run(debug=True)
