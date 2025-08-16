from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola! Este es mi primer sitio web con Flask.</h1>"

@app.route('/about')
def about():
    return "<h2>Sobre mí</h2><p>Esta es una página de información.</p>"

if __name__ == '__main__':
    app.run(debug=True)