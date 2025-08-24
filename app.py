from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/informacion')
def informacion():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)