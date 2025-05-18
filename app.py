from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

# Configuración de la aplicación Flask
app = Flask(__name__, static_folder='statics')

# Obtener la ruta del directorio actual del script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Ruta directa al modelo en la raíz
model_path = os.path.join(base_dir, "modelo_polucion.pkl")

# Cargar el modelo entrenado
try:
    with open(model_path, "rb") as file:
        modelo = pickle.load(file)
    print(f"Modelo de polución cargado exitosamente desde: {model_path}")
except FileNotFoundError:
    print(f"El modelo no se pudo cargar desde: {model_path}. Verifique la ruta y el nombre del archivo.")

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            year = int(request.form.get('year'))
            month = int(request.form.get('month'))
            day = int(request.form.get('day'))
            hour = int(request.form.get('hour'))

            # Crear un DataFrame con los datos ingresados
            nuevos_datos = pd.DataFrame([[year, month, day, hour]], columns=['year', 'month', 'day', 'hour'])

            # Realizar la predicción
            prediccion = modelo.predict(nuevos_datos)
            clase_predicha = prediccion[0]  # Obtener la clase directamente
            resultado = f"Clasificación de PM2.5: {clase_predicha}"
            print(f"Predicción realizada con éxito: {resultado}")

        except Exception as e:
            print(f"Error al realizar la predicción: {str(e)}")
            resultado = f"Error: {str(e)}"

    return render_template('index.html', prediccion=resultado)

if __name__ == '__main__':
    print("Iniciando la aplicación Flask")
    app.run(debug=True)
