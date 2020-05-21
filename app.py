import os
from procesamientoImagen import operador_raiz, operador_exponencial, operador_logaritmico, histogram_equalization
from flask import Flask ,render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/img"

@app.route('/')
def home():
    return render_template('formulario.html') # en vez fomulario pon el index.html

@app.route('/formulario')
def upload_file():
    return render_template('formulario.html')

@app.route("/raiz", methods=['POST'])
def endPointRaiz():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(full_filename)
        imagen_resultado = operador_raiz(app.config['UPLOAD_FOLDER'], filename)

        return  render_template('result.html', imagen=imagen_resultado)

@app.route("/logritmico", methods=['POST'])
def endPointLogaritmico():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(full_filename)
        imagen_resultado = operador_logaritmico(app.config['UPLOAD_FOLDER'], filename)

        return  render_template('result.html', imagen=imagen_resultado)

@app.route("/exponencial", methods=['POST'])
def endPointExponencial():
    if request.method == 'POST':
        f = request.files['archivo']
        C = int(request.form['C'])

        filename = secure_filename(f.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(full_filename)
        imagen_resultado = operador_exponencial(app.config['UPLOAD_FOLDER'], filename, C)

        return  render_template('result.html', imagen=imagen_resultado)

@app.route("/histEquali", methods=['POST'])
def endPointHistEqua():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(full_filename)
        imagen_resultado = histogram_equalization(app.config['UPLOAD_FOLDER'], filename)

        return  render_template('result.html', imagen=imagen_resultado)

if __name__ == '__main__':
    app.run(debug=True)
