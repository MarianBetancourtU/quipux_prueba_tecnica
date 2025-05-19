# Predicción de la Calidad del Aire Basado en los Niveles de Material Particulado 2.5
## Descripción
Este proyecto tiene como objetivo predecir los niveles de contaminación del aire (PM2.5) utilizando datos temporales. El enfoque principal es clasificar los niveles de contaminación en categorías de riesgo: buena, moderada, insalubre para sensibles, insalubre, muy insalubre, y peligroso; propuesta por la Agencia de Protección Ambiental de los Estados Unidos (EPA), facilitando la toma de decisiones en salud pública.

## Estructura del Proyecto
El proyecto está organizado en los siguientes archivos y carpetas:
- `README.md`: Archivo que contiene la descripción del proyecto, las instrucciones de instalación y uso.
- `data.txt`: Archivo con los datos utilizados para el entrenamiento del modelo. Contiene información sobre el nivel de contaminación PM2.5, variables temporales (año, mes, día, hora) y otras variables meteorológicas.
- `dict_data.txt`: Archivo con información descriptiva sobre las columnas del archivo de datos (data.txt). Incluye detalles sobre cada variable y su significado.
- `eda.ipynb`: Notebook en Jupyter que realiza el análisis exploratorio de datos (EDA), el entrenamiento del modelo y la generación del archivo .pkl. Incluye gráficos, estadísticas y los pasos detallados para la creación del modelo. Permite visualizar cómo se entrenó el modelo y cuál fue su rendimiento.
- `mini_app`: Carpeta que contine lo siguientes archivos, para realizar el despliegue locar de una mini aplicación que utiliza el modelo.
  - `templates` : Carpeta que contiene el siguiente archivo index:
    - `index.html`: Página principal de la aplicación web. Permite al usuario ingresar los valores temporales y obtener una predicción del nivel de contaminación. Contiene un formulario simple y la visualización del resultado.
  - `app.py`: Script principal de la aplicación Flask. Utiliza el modelo entrenado para predecir el nivel de contaminación PM2.5 según variables temporales (año, mes, día y hora).
  - `requirements.txt`: Archivo que contiene la lista de dependencias necesarias para ejecutar la aplicación. Incluye librerías como Flask, pandas, scikit-learn, entre otras. Se utiliza para instalar rápidamente todos los paquetes requeridos mediante el comando: `pip install -r requirements.txt`

## Decisiones de Diseño del Modelo

### Elección del Tipo de Modelo: 
Aunque el valor de PM2.5 es continuo, decidí utilizar modelos de clasificación en lugar de regresión por varias razones:
- Un modelo de clasificación genera información mas consisa y clara al público, por el contrario, un valor numérico exacto de PM2.5 puede ser difícil de interpretar sin un contexto adicional
- Los resultados de clasificación son más practicos para la toma de decisiones, ya que las entidades de salud y el público necesitan alertas  (por ejemplo, "No saludable" o "Peligroso"), no números específicos que necesiten más análisis.
- Las métricas de clasificación como F1 ponderado, accuracy, y recall son más útiles para evaluar si el modelo identifica correctamente el nivel de riesgo.
  
### Elección de Variables para el Modelo
La selección de variables se basó en un análisis exploratorio de datos . Durante este proceso, realicé análisis de correlación y visualización de las relaciones entre las variables meteorológicas, temporales y el nivel de contaminación (PM2.5).
Seleccioné solo las variables temporales para predecir la contaminación por las siguientes razones:
- Al analizar las gráficas de niveles de pm2.5 en el tiempo , se observa un pateon ciclcico, con valores de pm2.5 que aumentan o disminuyen de acuerdo al tiempo.
- Los valores de factores ambientales como temperatura, punto de rocio etc, tambien muestran un patron ciclico a lo largo del tiempo, que a su vez están directamente influenciados por la epoca del año, por que no necesatiamente podrian aportar mayor información al modelo en cuanto a contaminación. Esto no se puede asegurar, pero al realizar el mapa de correlación no se observa mayor correlacion entre la variable de interés y las otras variables.
- Al realizar en eltrenamiento de los modelos , las variables meteorologicas no aumentan el rendimiento del modelo.
- El enfoque de usar solo variables temporales garantiza simplicidad en la predicción y evita el uso de datos meteorológicos que pueden no estar disponibles en tiempo real, al momento de utilizar el modelo.

### Modelos de Clasificación Seleccionados
Elegí y probé algunos modelos de clasificiacion como Logistic Regression, Support Vector Classifier, K-Nearest Neighbors (KNN), pero al final seleccioné Random Forest debido a que presento el mayor renfimiento en términos de F1 ponderado (0.73) y precisión en el conjunto de prueba (0.76) (0.72 con validación cruzada).

## Instrucciones de de Despliegue y Uso de la mini app
### 1. Clonar el repositorio
### 2. Crear el Entorno Virtual dentro de la carpeta mini_app
Para asegurar que el entorno esté configurado correctamente, sigue estos pasos: 
`python -m venv env` (en Windows)
### 3. Activar el Entorno Virtual
Una vez creado el entorno, debes activarlo: `.\env\Scripts\Activate` (en Windows (PowerShell))
### 4. Instalar las Dependencias
Instala las librerías necesarias directamente desde el archivo requirements.txt: `pip install -r requirements.txt`
### 5. Generar el Modelo
Generar el archivo  `modelo_polucion.pkl`
- Abre el notebook con el siguiente comando: `jupyter notebook eda.ipynb`
- Dentro del notebook, busca la celda que contiene el código para entrenar el modelo.
- Ejecuta la celda para generar el archivo .pkl.
- Verifica que el archivo modelo_polucion.pkl se encuentre en la carpeta mini_app
### 6. Ejecutar la Mini App de Predicción
Con el entorno activado, ejecuta la aplicación Flask: `python app.py`
### 7.Acceder a la Aplicación Web
Abre el navegador y dirígete a: `http://127.0.0.1:5000/`

