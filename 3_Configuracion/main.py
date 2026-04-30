import sqlite3
import os
from dotenv import load_dotenv
import logging as log

log.basicConfig(
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        log.FileHandler('pipeline.log'), # Guardamos el archivo 
        log.StreamHandler()  # Mostramos en consola los logs
    ]
)

logger = log.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_log = os.path.join(BASE_DIR, 'pipeline.log')



load_dotenv()
nombre_db = os.getenv('DB_NAME')
target_db = os.path.join(BASE_DIR, nombre_db) if nombre_db else None


def iniciar_conexion(nombre_db):
    # Intentamos inicializar conexion con la base de datos
    try:
        conexion = sqlite3.connect(nombre_db)
        log.info(f"Se ha establecido correctamente la conexion con la base: {nombre_db}") # Creamos un log para el monitoreo 
        conexion.close()
    except Exception as e:
        log.error(f"Error: La conexión no se ha podido establecer... Detalle: {e}") # Creacion de otro log para deteccion de errores 

if __name__ == '__main__':
    if target_db:
        iniciar_conexion(target_db)
    else:
        log.warning(f"No se ha encontrado la variable de entorno dentro de .env")
    
    
