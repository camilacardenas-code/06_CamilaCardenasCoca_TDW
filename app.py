import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image  # Librería para procesar imágenes con Python (pip install Pillow)

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Carpeta donde se guardarán las imágenes subidas
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Extensiones permitidas para las imágenes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Validar si el archivo de imagen viene en la petición
        if 'imagen' not in request.files:
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)
        
        file = request.files['imagen']
        
        if file.filename == '':
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # --- PROCESAMIENTO DE LA IMAGEN CON PYTHON (Ejemplo: escala de grises) ---
            try:
                img = Image.open(filepath)
                img_procesada = img
                processed_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + filename)
                img_procesada.save(processed_path)
            except Exception as e:
                flash(f'Error al procesar la imagen: {e}')
                return redirect(request.url)
            
            flash('¡Imagen cargada y procesada con éxito!')
            return render_template('index.html', imagen_original=filename, imagen_procesada='processed_' + filename)
        else:
            flash('Formato de archivo no permitido')
            return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)