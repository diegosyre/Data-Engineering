# 🛠️ Módulo 03: Configuración y Seguridad de Entorno

Este módulo implementa un sistema de configuración profesional para pipelines de datos, priorizando la **soberanía de los datos** y la **seguridad de la información** mediante el aislamiento de variables sensibles.

---

### 🎯 Objetivo de Ingeniería
Establecer una capa base de configuración que permita al sistema conectarse a recursos externos (Bases de Datos, APIs) sin exponer credenciales o rutas críticas en el código fuente, garantizando que el pipeline sea **portable** entre diferentes entornos.

---

### 📝 Implementación Técnica (Control de Entorno)

El siguiente fragmento de código demuestra el uso de **rutas dinámicas**, carga de variables de entorno y manejo de errores preventivo:

```python
import sqlite3
import os
from dotenv import load_dotenv
import logging as log

# Configuración de trazabilidad dual
log.basicConfig(
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        log.FileHandler('pipeline.log'),
        log.StreamHandler()
    ]
)

# Gestión dinámica de rutas y variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv()

nombre_db = os.getenv('DB_NAME')
target_db = os.path.join(BASE_DIR, nombre_db) if nombre_db else None

def iniciar_conexion(db_path):
    try:
        conexion = sqlite3.connect(db_path)
        log.info(f"Conexión establecida con éxito: {db_path}")
        conexion.close()
    except Exception as e:
        log.error(f"Error crítico en la conexión: {e}")
```

### 🚀 Características Clave
*   **Dynamic Path Handling:** Uso de `os.path.abspath` para asegurar que el pipeline funcione independientemente de desde dónde se ejecute el script.
*   **Seguridad por Aislamiento:** Implementación de `python-dotenv` para mantener nombres de archivos y credenciales fuera del repositorio (vía `.env`).
*   **Validación de Entorno:** Lógica que detecta la ausencia de variables críticas antes de intentar operaciones de I/O, evitando el colapso del sistema.

---

### 📂 Estructura del Módulo
```text
3_Configuracion/
├── main.py          # Lógica de inicialización y conexión.
├── .env             # Bóveda de seguridad (protegido por .gitignore).
├── mi_proyecto.db   # Base de datos (protegido por .gitignore).
└── pipeline.log     # Bitácora de ejecución dinámica.
```

---

### 🛠️ Guía de Ejecución
1. **Instalar dependencias:** `pip install python-dotenv`
2. **Preparar .env:** Crea el archivo con `DB_NAME=tu_base.db`.
3. **Lanzar:** `python main.py`

---
**Ingeniería en Sistemas Computacionales** | *Implementando estándares de seguridad y robustez en arquitecturas de datos.*
