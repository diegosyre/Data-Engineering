# 🏗️ Mi Primer Pipeline ETL: User Data Processor

Este repositorio contiene la implementación de mi primer flujo de trabajo **ETL (Extract, Transform, Load)** desarrollado en Python. El proyecto demuestra la capacidad de integrar bibliotecas de procesamiento de datos con motores de bases de datos relacionales.

---

### 🛠️ Tecnologías y Librerías

Para replicar este entorno, instala las dependencias necesarias con el siguiente comando:

```bash
pip install pandas sqlalchemy
```

*   **Pandas:** Motor principal para la manipulación y limpieza de estructuras de datos (DataFrames).
*   **SQLAlchemy:** ORM y Toolkit de SQL para una conexión robusta y profesional con la base de datos.
*   **SQLite:** Base de datos ligera para persistencia local.

---

### 📐 Arquitectura del Pipeline

El proceso se divide en tres fases críticas para asegurar la integridad de la información:

1.  **Extraction (Extracción):** 
    *   Carga de datos desde fuentes estructuradas (DataFrame simulado con capacidad de escala para ingesta de **APIs** o archivos **CSV**).
2.  **Transformation (Transformación):** 
    *   **Data Cleaning:** Normalización de *strings* (limpieza de espacios y capitalización).
    *   **Type Casting:** Aseguramiento de tipos de datos correctos para columnas financieras y de usuario.
    *   **Handling Nulls:** Tratamiento estratégico de valores nulos en el campo de ventas para evitar sesgos en el análisis.
3.  **Loading (Carga):** 
    *   Persistencia de datos curados en una base de datos relacional utilizando **SQLAlchemy**, garantizando que el esquema sea consistente y consultable vía SQL.

---

### 🚀 Cómo Ejecutarlo

1.  Clona el repositorio.
2.  Asegúrate de tener instalado **Python 3.12+**.
3.  Instala las librerías mencionadas arriba.
4.  Ejecuta el script principal:
    ```bash
    python main.py
    ```

---

### 📈 Aprendizajes Clave
- Manejo de **ciclos de vida del dato**.
- Introducción al **mapeo objeto-relacional (ORM)**.
- Implementación de lógica de limpieza para mejorar la **calidad de los datos (Data Quality)**.

---
**Ingeniería en Sistemas Computacionales** | *Enfocado en construir bases de datos íntegras y escalables.*