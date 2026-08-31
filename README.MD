# Sistema de Detección de Rostros con YOLOv8-Pose y Tkinter en WSL

Este proyecto implementa un flujo de trabajo avanzado para Inteligencia Artificial utilizando el modelo oficial **YOLOv8-Pose** de Ultralytics. Este sistema extrae los *keypoints* faciales esenciales (ojos y nariz) y aplica proporciones anatómicas basadas en la distancia interocular para enmarcar rostros de lo más exacta posible.

Permite cargar imágenes desde una carpeta local, procesarlas con un modelo YOLOv8-Pose y mostrar los resultados dentro de una interfaz gráfica creada con Tkinter.

La aplicación recorre automáticamente las imágenes de una carpeta, muestra cada una y permite avanzar o retroceder entre ellas con botones.

## ¿Qué hace?

- Lee imágenes desde una carpeta llamada `imagenes`
- Detecta rostros y puntos clave faciales con YOLOv8-Pose
- Dibuja un recuadro alrededor del rostro detectado
- Muestra la imagen resultante en una ventana Tkinter
- Permite navegar entre varias imágenes con botones

## Tecnologías utilizadas

- Python
- OpenCV
- Pillow
- Tkinter
- Ultralytics YOLOv8

## 🚀 Desafíos Técnicos Resueltos (Aprendizaje)

1. **Gestión de Entornos Virtuales:** Configuración y aislamiento de un entorno dedicado en **Miniconda** con Python 3.11, garantizando compatibilidad total con librerías de IA.
2. **Depuración de Infraestructura Linux:** Corrección de bloqueos en el gestor de paquetes (`apt`) en WSL eliminando repositorios obsoletos (`404 Not Found`) e instalando librerías gráficas esenciales (`libGL`).
3. **Escala y Proporción Dinámica:** Implementación del Teorema de Pitágoras para calcular la distancia euclidiana entre los ojos. Esto permite que los rectángulos se expandan o encojan proporcionalmente según la distancia de la persona a la cámara, capturando de forma exacta desde la frente hasta la barbilla.
4. **Interfaz Fluida Híbrida:** Diseño de un navegador de imágenes integrado con **Tkinter** y **Pillow (PIL)**, que permite iterar fotos mediante botones nativos sin interrumpir la experiencia con ventanas emergentes.


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

