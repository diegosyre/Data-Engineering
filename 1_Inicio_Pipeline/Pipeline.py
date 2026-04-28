
import pandas as pd 
import sqlalchemy as sql
import os

def extraer_datos():
    data = {
        'id': [1, 2, 3, 4],
        'nombre': ['  juan perez  ', 'MARIA Lopez', 'pedro gomez ', 'ana SOTO'],
        'ventas': ['100.50', '200', 'no_disponible', '150.75'],
        'fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']
    }
    df = pd.DataFrame(data)
    print("Extracción completada...")
    return df

def transformar_datos(df):
    print("Iniciando transformación de datos...")

    #Limpieza de datos eliminando espacios y normalizando los nombres
    df['nombre'] = df['nombre'].str.strip().str.title()

    #Manejo de tipos, coerce transforma todo aquello que no se puede convertir como un NaN Not a Number
    df['ventas'] = pd.to_numeric(df['ventas'], errors='coerce')

    # Tratamos los nullos usando fill
    df['ventas'] = df['ventas'].fillna(0)

    #Formateamos las fechas 
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

    print("Transformación completada...")
    return df

def cargar_datos(df):

    # Extraemos la ruta actual donde se creara la bd local
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    # Unimos nuestra ruta extrauda y el nombre de la bbdd
    ruta_db = os.path.join(ruta_base, 'mi_proyecto.db')
    # Creamos el motor donde almacenar nuestros datos
    engine = sql.create_engine(f'sqlite:///{ruta_db}')

    # Creamos la tabla de usuarios procesados (datos limpios) del data frame 
    df.to_sql('Usuarios procesados', engine, if_exists='replace', index=False)

    print("Carga completada     ...")



if __name__ == '__main__':
    datos_crudos = extraer_datos()
    datos_limpios = transformar_datos(datos_crudos)
    cargar_datos(datos_limpios)

    print("Proceso completado...")
    print(datos_limpios)
    


    
    