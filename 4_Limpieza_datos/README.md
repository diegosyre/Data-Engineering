
# 🚀 ETL Pipeline: Limpieza y Estandarización de Datos Financieros

## 📄 Descripción
Este proyecto implementa un flujo **ETL (Extract, Transform, Load)** automatizado desarrollado en Python. Está diseñado para procesar transacciones financieras desde fuentes de datos crudos (CSV), aplicando reglas de negocio para garantizar la integridad y calidad de la información antes de su almacenamiento en una base de datos relacional.

El sistema soluciona problemas comunes en la ingeniería de datos como valores nulos, registros duplicados y falta de estandarización en catálogos y formatos de fecha.

## 🎯 Objetivos

*   **Automatización**: Sustituir el procesamiento manual de datos por un script escalable y repetible.
*   **Integridad de Datos**: Implementar lógica de limpieza para eliminar ruido y redundancia en la información.
*   **Estandarización**: Normalizar formatos de moneda, fechas y nombres de sucursales para asegurar reportes precisos.
*   **Persistencia Profesional**: Migrar datos de archivos volátiles (CSV) a una base de datos estructurada (SQL).



## 🛠️ Stack Tecnológico
*   **Lenguaje:** Python 3.12+


*   **Librerías principales:**
    *   `Pandas`: Manipulación avanzada de datos y limpieza de DataFrames.
    *   `SQLAlchemy`: Creación del motor (Engine) y gestión de la conexión SQL.
    *   `Python-dotenv`: Manejo seguro de configuraciones y variables de entorno.
    *   `Logging`: Registro de eventos, errores y el comportamiento del pipeline en tiempo real, creando una bitácora secuencial
*   **Base de Datos:** SQLite (local) para desarrollo ágil.
## 📂 Estructura del Proyecto
```text
4_Limpieza_Datos/
├── .env                # Configuración de variables (DB_NAME, rutas)
├── .gitignore          # Exclusión de archivos de datos y binarios
├── Limpieza.py         # Script principal con la lógica del pipeline
├── Limpieza.log        # Registro detallado de la ejecución del proceso
├── Consulta_finanzas.sql # Consultas SQL para validación de resultados
└── Finanzas_limpias.db # Base de datos final (generada automáticamente)
```


## ✅ Funcionalidades Implementadas

El pipeline realiza una transformación profunda de los datos crudos siguiendo estas etapas:

*   **Carga de Datos Segura**: Gestión de rutas relativas mediante la librería `os` para asegurar la portabilidad del proyecto entre diferentes entornos.
*   **Limpieza de Montos**: Conversión de tipos de datos de `String` a `Float`, eliminando caracteres especiales y comas para permitir cálculos matemáticos.
*   **Tratamiento de Nulos y Duplicados**: Eliminación de filas redundantes y gestión lógica de valores faltantes para evitar sesgos en el análisis.
*   **Estandarización de Catálogos (Mapeo)**: Uso de diccionarios de "verdad" para corregir errores ortográficos y variaciones en columnas como `sucursal` y `tipo_pago`.
*   **Normalización de Fechas**: Conversión de diversos formatos a estándar ISO y validación de fechas inconsistentes.
*   **Persistencia SQL**: Carga automatizada a través de un `engine` de SQLAlchemy que gestiona la creación y actualización de tablas en SQLite.

## 🚀 Instrucciones de Uso

Para replicar este proyecto en tu entorno local, sigue estos pasos:

1.  **Preparación del Entorno**:
    *   Clona el repositorio.
    *   Crea un entorno virtual: `python -m venv venv`.
    *   Instala las dependencias: `pip install pandas sqlalchemy python-dotenv`.

2.  **Configuración**:
    *   Crea un archivo `.env` en la carpeta `4_Limpieza_Datos/`.
    *   Define la variable: `DB_NAME=tu_base_de_datos.db`.

3.  **Ejecución**:
    *   Coloca tu archivo de origen `Chunk_Finanzas.csv` en la carpeta del proyecto.
    *   Ejecuta el script principal:
        ```bash
        python Limpieza.py
        ```

4.  **Validación**:
    *   Abre el archivo `.db` generado con el **SQLite Explorer** de VS Code para verificar la tabla `transacciones_limpias`.


## 📈 Próximos Pasos (Roadmap)

Como parte de mi formación en **Data Engineering** y **Project Management**, tengo planeado integrar las siguientes mejoras:

- [ ] **Unit Testing**: Implementar pruebas con `pytest` para validar cada función de limpieza de forma aislada.
- [ ] **Dockerización**: Crear un contenedor para asegurar que el pipeline corra idéntico en cualquier servidor.
- [ ] **Visualización**: Conectar la base de datos a un dashboard en **Streamlit** para mostrar KPIs de ventas en tiempo real.






*Proyecto desarrollado como parte del portafolio profesional de Ingeniería en Sistemas Computacionales.*

