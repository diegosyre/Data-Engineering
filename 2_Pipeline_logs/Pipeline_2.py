
import pandas as pd 
import sqlalchemy as sql
import os
import logging as lg

# configuramos el logger

lg.basicConfig(
    level=lg.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        lg.FileHandler('pipeline.log'), # Guardamos el archivo 
        lg.StreamHandler()  # Mostramos en consola los logs
    ]
)

logger = lg.getLogger(__name__)




def extraer_datos():
    lg.info("Iniciando extracción de datos...") # Iniciamos el primer log que ha iniciado la estraccion de datos

    try:
        data = {
            'id': [1, 2, 3, 4],
            'nombre': ['  juan perez  ', 'MARIA Lopez', 'pedro gomez ', 'ana SOTO'],
            'ventas': ['100.50', '200', 'no_disponible', '150.75'],
            'fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']
        }
        df = pd.DataFrame(data)
        lg.info("Extracción completada...") # Colocamos el log que informa en base a lo que esta sucediendo
        return df
    except Exception as e:
        lg.error(f"Error en la extracción de datos: {e}") # Si se han ingresado valores informamos del error ocurrido 
        raise





def transformar_datos(df):
    lg.info("Iniciando transformación de datos...")

    

    #Limpieza de datos eliminando espacios y normalizando los nombres
    df['nombre'] = df['nombre'].str.strip().str.title()

    #Manejo de tipos, coerce transforma todo aquello que no se puede convertir como un NaN Not a Number
    df['ventas'] = pd.to_numeric(df['ventas'], errors='coerce')

    # Creamos un conteo de errores 
    errores_encontrados = df['ventas'].isna().sum() 

    if errores_encontrados > 0:
        lg.warning(f"Se detectaron {errores_encontrados} errores en la columna 'ventas'. Se procede a imputar con valor 0")

    # Tratamos los nullos usando fill
    df['ventas'] = df['ventas'].fillna(0)

    #Formateamos las fechas 
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

    # Colocamos un log que informe que ha terminado el proceso de transformación de manera exitosa
    lg.info("Transformación completada...")
    return df


def cargar_datos(df):

    lg.info("Iniciando carga de datos...")

    try:
        tabla = 'Usuarios procesados'

        # Extraemos la ruta actual donde se creara la bd local
        ruta_base = os.path.dirname(os.path.abspath(__file__))
        # Unimos nuestra ruta extrauda y el nombre de la bbdd
        ruta_db = os.path.join(ruta_base, 'mi_proyecto.db')
        # Creamos el motor donde almacenar nuestros datos
        engine = sql.create_engine(f'sqlite:///{ruta_db}')

        # Creamos la tabla de usuarios procesados (datos limpios) del data frame 
        df.to_sql(tabla, engine, if_exists='replace', index=False)
        # Creamos un log especifico para el guardado de datos 
        lg.info(f"Carga de datos hecha en: {tabla}, en la ruta: {ruta_db}, actualizada con {len(df)} registros.")
    except Exception as e:
        lg.error(f"Error en la carga de datos: {e}")
        raise




if __name__ == '__main__':
    datos_crudos = extraer_datos()
    datos_limpios = transformar_datos(datos_crudos)
    cargar_datos(datos_limpios)

    print("Proceso completado...")
    print(datos_limpios)
    


    
    

