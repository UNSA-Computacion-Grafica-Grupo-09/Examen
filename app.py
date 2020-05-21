import os
#from convertirGrey  import  imagen_gray
#from procesamientoImagen import operador_logaritmico
from procesamientoImagen import histogram_equalization
from flask import Flask ,render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/img"


@app.route('/')
def upload_file():
    return render_template('formulario.html')

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(full_filename)
        #PRUEBAS
        imagen_resultado = histogram_equalization(app.config['UPLOAD_FOLDER'], filename)
        #imagen_resultado = operador_logaritmico(app.config['UPLOAD_FOLDER'], filename)
        #imagen_resultado = imagen_gray(app.config['UPLOAD_FOLDER'], filename)

        return  render_template('result.html', imagen=imagen_resultado)

if __name__ == '__main__':
    app.run(debug=True)
