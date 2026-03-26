import json
import os

FILE = "config.json"

def cargar_info():
    if not os.path.exists(FILE):
        return []
        
    with open(FILE, "r") as f:
        return json.load(f)
    
def guardar_info(datos):
    with open(FILE,"w") as f:
        json.dump(datos, f, indent=4)
        
def agregar_archivo(nombre, ruta):
    datos = cargar_info()
    datos.append({
        "nombre": nombre,
        "ruta": ruta
    })
    guardar_info(datos)
