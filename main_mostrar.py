import cv2
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from ultralytics import YOLO

ANCHO_MAXIMO = 600
ALTO_MAXIMO = 500
CARPETA_FOTOS = Path("imagenes")

indice_actual = 0
lista_imagenes = []

# Cargar el modelo
try:
    modelo = YOLO("yolov8m-pose.pt")
except FileNotFoundError:
    print("❌ No se encontró el archivo yolov8m-pose.pt")
    modelo = None
except Exception as e:
    print(f"❌ Error al cargar el modelo: {e}")
    modelo = None

# Crear la carpeta si no existe
if not CARPETA_FOTOS.exists():
    CARPETA_FOTOS.mkdir(parents=True, exist_ok=True)

# Lista de imágenes
lista_imagenes = sorted(
    [
        archivo
        for archivo in CARPETA_FOTOS.iterdir()
        if archivo.is_file() and archivo.suffix.lower() in {".jpg", ".jpeg", ".png"}
    ],
    key=lambda x: x.name.lower()
)

def mostrar_imagen_actual():
    global indice_actual

    if not lista_imagenes:
        lbl_estado.config(text="La carpeta 'imagenes' está vacía. Agrega fotos ahí.", fg="red")
        return

    ruta_imagen = lista_imagenes[indice_actual]

    imagen_cv = cv2.imread(str(ruta_imagen))
    if imagen_cv is None:
        lbl_estado.config(text="No se pudo leer la imagen.", fg="red")
        return

    resultados = modelo(imagen_cv, conf=0.25)[0]
    imagen_con_rectangulo = imagen_cv.copy()

    if resultados.keypoints is not None:
        for keypoints in resultados.keypoints.xy:
            if len(keypoints) < 3:
                continue

            x_nasal, y_nasal = keypoints[0]
            x_ojo_izq, y_ojo_izq = keypoints[1]
            x_ojo_der, y_ojo_der = keypoints[2]

            if x_nasal <= 0 or x_ojo_izq <= 0 or x_ojo_der <= 0:
                continue

            centro_x = int((x_ojo_izq + x_ojo_der + x_nasal) / 3)
            centro_y = int((y_ojo_izq + y_ojo_der + y_nasal) / 3)

            distancia_ojos = int(
                ((x_ojo_der - x_ojo_izq) ** 2 + (y_ojo_der - y_ojo_izq) ** 2) ** 0.5
            )

            if distancia_ojos == 0:
                distancia_ojos = 15

            radio_x = int(distancia_ojos * 1.2)
            radio_y = int(distancia_ojos * 1.5)

            x1 = max(0, centro_x - radio_x)
            y1 = max(0, centro_y - radio_y)
            x2 = min(imagen_cv.shape[1], centro_x + radio_x)
            y2 = min(imagen_cv.shape[0], centro_y + radio_y)

            cv2.rectangle(imagen_con_rectangulo, (x1, y1), (x2, y2), (0, 255, 0), 3)

    imagen_rgb = cv2.cvtColor(imagen_con_rectangulo, cv2.COLOR_BGR2RGB)
    imagen_pillow = Image.fromarray(imagen_rgb)
    imagen_pillow.thumbnail((ANCHO_MAXIMO, ALTO_MAXIMO))

    imagen_tk = ImageTk.PhotoImage(image=imagen_pillow)
    lbl_imagen.config(image=imagen_tk)
    lbl_imagen.image = imagen_tk

    lbl_estado.config(
        text=f"Foto {indice_actual + 1} de {len(lista_imagenes)}: {ruta_imagen.name}",
        fg="green"
    )


def foto_siguiente():
    global indice_actual
    if not lista_imagenes:
        return
    indice_actual = (indice_actual + 1) % len(lista_imagenes)
    mostrar_imagen_actual()


def foto_anterior():
    global indice_actual
    if not lista_imagenes:
        return
    indice_actual = (indice_actual - 1) % len(lista_imagenes)
    mostrar_imagen_actual()


root = tk.Tk()
root.title("Visor de imágenes con detección")
root.geometry("700x650")

lbl_titulo = tk.Label(root, text="Navegador de detección", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)

btn_anterior = tk.Button(
    frame_botones,
    text="< Anterior",
    command=foto_anterior,
    bg="#FF9800",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)
btn_anterior.pack(side=tk.LEFT, padx=10)

btn_siguiente = tk.Button(
    frame_botones,
    text="Siguiente >",
    command=foto_siguiente,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)
btn_siguiente.pack(side=tk.LEFT, padx=10)

lbl_estado = tk.Label(root, text="Cargando galería...", font=("Arial", 10, "italic"))
lbl_estado.pack(pady=5)

lbl_imagen = tk.Label(root, bg="#2A2A2A", width=800, height=550)
lbl_imagen.pack(padx=20, pady=20, expand=True)

if modelo is not None:
    mostrar_imagen_actual()
else:
    lbl_estado.config(text="El modelo no está disponible.", fg="red")

root.mainloop()