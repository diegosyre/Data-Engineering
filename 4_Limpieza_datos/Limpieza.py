
import pandas as pd
import logging as log
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Inicializamos las variables para traer las variables dinamicas dentro de .env a nuestro main
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Configuramos el log
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        log.FileHandler(os.path.join(BASE_DIR, 'limpieza.log')),
        log.StreamHandler()
    ]
)

# Asociamos las variables con los datosl archivo .env
archivo_sucio = os.getenv("DATOS")
base_datos = os.getenv("DB_NAME")

# Metodo para el diagnostico de datos antes de su limpieza
def diagnostico_de_datos(df):
    log.info("Iniciando el diagnostico de datos...")
    print(f"Conteo de valores nulos: {df.isnull().sum()}")
    print(f"Tipos de columnas de datos: {df.dtypes}")


# Metodo en el cual podemos eliminar nulos dentro de nuestro df
def eliminado_nulos(df):
    log.info("Iniciando tratado de nulos...")
    df = df.dropna(subset=['id_transaccion', 'cliente'])

    df['monto'] = df['monto'].fillna(0.0)
    return df


# Metodo para eliminar duplicados dentro de nuestro df
def eliminar_duplicados(df):
    log.info("Inicializando con el elimiado de datos...") # Log especifico para la incializacion de la eliminación
    antes = len(df)
    df = df.drop_duplicates(subset =['id_transaccion'], keep = 'first') # Eliminacion de los ultimos duplicados conservando el original 
    despues = len(df)

    log.info(f"Se eliminaron {antes - despues} filas duplicadas.") # Conformamos cuantas filas se han eliminado bajo los cirterios ya prestablecidos
    return df

def estaraizar_fechas(df):
    log.info("Estandarizando fechas...")
    df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True, errors='coerce')
    nulos_fecha = df['fecha'].isnull().sum()

    if nulos_fecha > 0:
        log.warning(f"Se encontraron {nulos_fecha} valores nulos en la columna 'fecha'.")
        df = df.dropna(subset=['fecha'])
    else:
        log.info("No se encontraron valores nulos en la columna 'fecha'.")

    return df

def estandarizar_catalogos(df):
    log.info("Estandarizando catalogos...")
    mapa_pagos = {
        'Efctivo': 'Efectivo',
        'Efecitvo': 'Efectivo',
        'Tranferencia': 'Transferencia',
        'Tarjeta de credito': 'Tarjeta',
        'Tarjeta de debito': 'Tarjeta',
        'Tarjera': 'Tarjeta'
    }

    mapa_estados = {
        'En ruta': 'Pendiente',
        'Proceso': 'Pendiente',
        'Fallida': 'Error',
    }

    columnas_a_limpiar = ['tipo_pago', 'estado', 'sucursal']
    for col in columnas_a_limpiar:
        df[col] = df[col].astype(str).str.strip().str.capitalize()

    df['tipo_pago'] = df['tipo_pago'].replace(mapa_pagos)
    df['estado'] = df['estado'].replace(mapa_estados)

    df.loc[df['tipo_pago'].isin(['?', 'Nan', 'None']), 'tipo_pago'] = 'No definido'

    return df


def carga_bd(df, base_datos):
    try:
        engine = create_engine(f'sqlite:///{base_datos}')
        df.to_sql('transacciones_limpias', con=engine, if_exists='replace', index=False)
        log.info(f"Proceso de carga completado. Se cargargaron {len(df)} limpios de datos a la base de datos {base_datos}.")
    except Exception as e:
        log.error(f"Error al cargar los datos a la base de datos: {e}")




# Ejecucon de nuestro main
if __name__ == "__main__":
    ruta_csv = os.path.join(BASE_DIR, archivo_sucio)
    
    if os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv, index_col=False)
        log.info(f"Archivo {archivo_sucio} cargado correctamente.")

        
        if 'id_transaccion' not in df.columns:
            log.info("Rescatando 'id_transaccion' desde el índice...")
            df = df.reset_index()
        
        
        df.columns = [col.strip().lower() for col in df.columns]
        
        if 'index' in df.columns:
            df.rename(columns={'index': 'id_transaccion'}, inplace=True)

       
        diagnostico_de_datos(df)

        
        df.to_csv(ruta_csv, index=False)

        df = eliminar_duplicados(df)
        df = eliminado_nulos(df)
        df = estaraizar_fechas(df)
        df = estandarizar_catalogos(df)
        
        # El gran final
        base_datos_ruta = os.path.join(BASE_DIR, base_datos)
        carga_bd(df, base_datos_ruta)

        
    else:
        log.error(f"El archivo {archivo_sucio} no existe en la ruta: {ruta_csv}")
