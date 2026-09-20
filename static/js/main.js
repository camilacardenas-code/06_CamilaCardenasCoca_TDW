document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const nombre = document.getElementById('nombre');
    const imagen = document.getElementById('imagen');

    const errorNombre = document.getElementById('errorNombre');
    const errorImagen = document.getElementById('errorImagen');

    // Validaciones al enviar el formulario
    if (form) {
        form.addEventListener('submit', function(event) {
            let isValid = true;

            // Limpiar errores previos
            errorNombre.textContent = '';
            errorImagen.textContent = '';

            // Validación 1: Campo de texto no vacío
            if (nombre.value.trim() === '') {
                errorNombre.textContent = 'Por favor, ingresa tu nombre.';
                isValid = false;
            }

            // Validación 2: Verificar selección de imagen
            if (imagen.files.length === 0) {
                errorImagen.textContent = 'Por favor, selecciona una imagen.';
                isValid = false;
            } else {
                const archivo = imagen.files[0];
                const tiposPermitidos = ['image/jpeg', 'image/png', 'image/jpg'];
                if (!tiposPermitidos.includes(archivo.type)) {
                    errorImagen.textContent = 'Solo se permiten archivos de imagen válidos (JPEG, PNG).';
                    isValid = false;
                }
            }

            // Detener envío si hay errores
            if (!isValid) {
                event.preventDefault();
            }
        });
    }

    // Mostrar el nombre del archivo seleccionado junto al botón
    if (imagen) {
        imagen.addEventListener('change', function(e) {
            var fileName = e.target.files[0] ? e.target.files[0].name : 'Ningún archivo seleccionado';
            var nombreArchivoSpan = document.getElementById('nombre-archivo');
            if (nombreArchivoSpan) {
                nombreArchivoSpan.textContent = fileName;
            }
        });
    }
});