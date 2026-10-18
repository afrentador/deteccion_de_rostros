# Sistema de Detección de Rostros con YOLOv8-Pose y Tkinter en WSL

Este proyecto implementa un flujo de trabajo avanzado para Inteligencia Artificial utilizando el modelo oficial **YOLOv8-Pose** de Ultralytics. Este sistema extrae los *keypoints* faciales esenciales (ojos y nariz) y aplica proporciones anatómicas basadas en la distancia interocular para enmarcar rostros con alta precisión, integrando una interfaz gráfica interactiva en Tkinter.

## ¿Qué hace el sistema?
- **Procesamiento de Imágenes:** Recorre automáticamente conjuntos de datos visuales desde un directorio local.
- **Detección y Extracción de Puntos Clave:** Identifica rostros y extrae coordenadas geoespaciales de elementos faciales con YOLOv8-Pose.
- **Cálculo Métrico Dinámico:** Modela el tamaño del encuadre de forma proporcional a la distancia del sujeto.
- **Interfaz de Navegación:** Despliega visualizaciones dinámicas integradas con Tkinter y Pillow para la iteración de datos.

## 🛠️ Tecnologías y Entornos
- **Lenguaje:** Python
- **Librerías de Datos y Visión:** OpenCV, Pillow (PIL), Ultralytics YOLOv8
- **Interfaz Gráfica:** Tkinter
- **Entorno de Desarrollo:** WSL2 (Ubuntu), Miniconda (Python 3.11)

## 🚀 Desafíos Técnicos Resueltos (Aprendizaje)

### 1. Modelado Matemático (Escala y Proporción Dinámica)
Implementé el **Teorema de Pitágoras** para calcular la *distancia euclidiana* entre los vectores de los ojos en tiempo real. Esto permite que el algoritmo normalice el tamaño de los rectángulos de captura, expandiéndose o encogiéndose proporcionalmente según la distancia de la persona a la lente. Demuestra la capacidad de aplicar lógica matemática para resolver problemas de consistencia de datos.

### 2. Infraestructura y Redirección de Hardware en WSL2
Al desarrollar sobre una arquitectura **WSL2**, el sistema presentaba restricciones nativas para acceder a hardware periférico (cámara web de Windows). 
- **Solución:** Reestructuré el flujo de entrada de datos conectando el script a una transmisión de video por IP (URL) emitida desde un dispositivo móvil, logrando que el backend en Linux procesara el stream de datos en tiempo real a través de la red local.
- Adicionalmente, depuré bloqueos en el gestor de paquetes de Ubuntu (`apt`) eliminando repositorios obsoletos e instalando dependencias gráficas críticas (`libGL`).

### 3. Gestión de Entornos Eficientes
Configuración y aislamiento de entornos virtuales dedicados mediante **Miniconda**, garantizando la reproducibilidad del proyecto y la gestión eficiente de dependencias pesadas de Machine Learning.

### 4. Interfaz Fluida Híbrida
Diseño de un navegador de imágenes integrado con **Tkinter** y **Pillow (PIL)**, que permite iterar fotos mediante botones nativos sin interrumpir la experiencia con ventanas emergentes.

## Estructura del proyecto

```text
deteccion_de_rostros/
├── backup/                # Proyecto piloto o versiones anteriores
├── imagenes/              # Carpeta con imágenes de prueba
├── main_mostrar.py        # Script principal
├── README.md
├── requirements.txt
├── .gitignore
└── yolov8m-pose.pt        # Modelo descargado localmente

## 📈 Próximos Pasos (Enfoque Analítico)
- [ ] **Persistencia de Datos:** Integrar una base de datos relacional (SQLite) para registrar variables de cada detección (ID, timestamp, distancia euclidiana calculada y nivel de confianza).
- [ ] **Módulo de Analítica:** Desarrollar un script en **Pandas** y **Matplotlib** para analizar los patrones de asistencia, horas pico de detección y métricas de rendimiento del modelo.
