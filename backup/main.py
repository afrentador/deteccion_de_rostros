import cv2   # Para leer y procesar la imagen
import os  
import tkinter as tk    
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # El "puente" que traduce la imagen entre OpenCV y Tkinter.
from ultralytics import YOLO 


ANCHO_MAXIMO = 600
ALTO_MAXIMO = 500


modelo = None
try:
    modelo = YOLO("yolov8n.pt")
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo 'yolov8n.pt'")
except Exception as e:
    print(f"❌ Error al cargar el modelo: {type(e).__name__}: {e}")

def seleccionar_y_procesar():
    if modelo is None:
        messagebox.showerror("Error", "El modelo no está cargado. Revisa la consola.")
        return
    
    ruta_imagen = filedialog.askopenfilename(
        initialdir = ".",
        title = "Selecciona una Imagen",
        filetypes = (("Archivos JPG", "*.jpg"), ("Archivos PNG", "*.png"), ("Todos los archivos", "*.*"))
    )

    if not ruta_imagen:
        return
    
    # Valida que el archivo existe
    if not os.path.isfile(ruta_imagen):
        messagebox.showerror("Error", f"El archivo no existe: {ruta_imagen}")
        return
    
    # Lee la imagen del archivo
    photo_cv = cv2.imread(ruta_imagen)
    if photo_cv is None:
        messagebox.showerror("Error", "No se pudo cargar el archivo seleccionado. Verifica que sea una imagen válida.")
        return
    
    # Extraemos la imagen que dibujadas por la IA
    resultados = modelo(photo_cv) 
    photo_cv_detectada = resultados[0].plot() 
    photo_rgb = cv2.cvtColor(photo_cv_detectada, cv2.COLOR_BGR2RGB)   

    
    # Convertimos a imagen de Pillow
    imagen_pillow = Image.fromarray(photo_rgb)
    imagen_pillow.thumbnail((ANCHO_MAXIMO, ALTO_MAXIMO))

    # Convertimos esa imagen de Pillow en un formato final Tkinter
    imagen_final_tk = ImageTk.PhotoImage(image = imagen_pillow)
    lbl_imagen.config(image = imagen_final_tk)
    lbl_imagen.image = imagen_final_tk


root = tk.Tk()
root.title("Mi visor de Imágenes en WSL")
root.geometry("700x650")


lbl_titulo = tk.Label(root, text="Analizador de Imágenes Inteligente", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=10)

btn_cargar = tk.Button(
    root,
    text= "Seleccionar Nueva Imagen",
    command = seleccionar_y_procesar,
    bg ="#2196F3", 
    fg ="white", 
    font =("Arial", 11, "bold"),
    padx =10,
    pady =5
)
btn_cargar.pack(pady=10)

lbl_estado = tk.Label(root, text= "Por favor, selecciona una imagen para comenzar...", font=("Arial", 10, "italic"))
lbl_estado.pack(pady=5)

lbl_imagen = tk.Label(root, bg="#2A2A2A", width=800, height=450)
lbl_imagen.pack(padx=20, pady=20, expand=True)


root.mainloop()

