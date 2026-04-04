import json
import sys
import os

def obtener_dir(filename):
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir,filename)
FILE = obtener_dir('config.json')

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

def eliminar_json(ruta):
    datos = cargar_info()
    nuevos = [item for item in datos if item["ruta"] != ruta]
    guardar_info(nuevos)