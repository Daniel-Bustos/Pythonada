from flask import Flask, render_template

app = Flask(__name__)

#ruta para pagina
@app.route('/')
def home():
    return render_template('home.html')

#ruta about
@app.route('/about')
def about():
    return render_template('about.html')

#debug=True = reiniciar
if __name__ == '__main__':
    app.run(debug=True)