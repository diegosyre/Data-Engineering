# Data Engineering Roadmap 🚀

Repositorio especializado en la documentación, diseño y ejecución de procesos **ETL**, arquitectura de datos y estrategias de **observabilidad**. Este espacio sirve como bitácora técnica de mi evolución como Ingeniero de Datos.

---

## 🛠️ Stack Tecnológico
[![My Skills](https://skillicons.dev/icons?i=git,github,py,sqlite,vscode)](https://skillicons.dev)

---

## 📂 Estructura del Proyecto

Cada módulo representa un hito en la construcción de pipelines de datos robustos:


| Módulo | Título | Descripción Técnica |
| :--- | :--- | :--- |
| **01** | `Inicio_Pipeline` | Fundamentos de flujos **ETL**. Extracción de fuentes planas y carga en entornos relacionales (SQLite). |
| **02** | `Pipeline_Logs` | Implementación de **Logging & Observabilidad**. Auditoría de procesos y manejo avanzado de excepciones. |
| **03** | `Configuracion` | Gestión de variables de entorno mediante archivos `.env` para asegurar la seguridad y portabilidad del código. |
| **04** | `Limpieza_datos` | Procesamiento de *chunks* financieros masivos: limpieza, normalización y persistencia en base de datos. |

## 🚀 Detalle de Módulos Recientes

### 🏗️ 03. Configuración y Seguridad (`.env`)
En esta fase se profesionalizó el manejo de credenciales y rutas. 
- Implementación de `python-dotenv` para desacoplar la configuración del código fuente.
- Protección de datos sensibles y fácil migración entre entornos (Desarrollo/Producción).

### 🧹 04. Limpieza de Datos Financieros (Batch Processing)
Se trabajó con un **dataset financiero sucio** (datos de transacciones), aplicando técnicas de ingeniería de datos para asegurar la calidad de la información:
- **Carga por Chunks:** Procesamiento eficiente de archivos de gran tamaño para optimizar el uso de memoria.
- **Data Wrangling:** 
  - Eliminación de registros nulos y duplicados.
  - Normalización de formatos (fechas, monedas y tipos de cambio).
  - Estandarización de nombres de columnas bajo convención *snake_case*.
- **Persistencia:** Exportación de los datos curados a una base de datos estructurada para análisis posterior.

---

> **Ingeniería en Sistemas Computacionales** | *En constante aprendizaje sobre arquitecturas escalables y gobierno de datos.*