import json
import os
from pptx_handler import fuente_direccion
ruta_json = fuente_direccion('config.json')
FILE = ruta_json

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
