# 📈 Pipeline ETL con Observabilidad y Auditoría (v2)

Esta versión representa la evolución técnica de un flujo funcional hacia un **sistema robusto con principios de ingeniería de datos**. El enfoque principal de esta iteración es la **trazabilidad**: garantizar que cada paso del proceso sea auditable y monitoreable.

---

### 🚀 Mejoras de Ingeniería (v2 vs v1)

En esta etapa, el enfoque se desplazó de "mover datos" a "controlar el flujo". Las implementaciones clave incluyen:

*   **Logging Profesional:** Migración de sentencias `print()` al módulo nativo `logging` de Python.
*   **Niveles de Severidad:** Implementación de jerarquías de eventos (`INFO`, `WARNING`, `ERROR`).
*   **Data Profiling & Auditoría:** Identificación de anomalías antes de la fase de transformación.

---

### 📝 Implementación del Sistema de Logs

Para garantizar que el sistema sea auditable, se configuró una trazabilidad dual (archivo y consola) mediante el siguiente bloque de código:

```python
import logging as lg

# Configuración de observabilidad y auditoría
lg.basicConfig(
    level=lg.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        lg.FileHandler('pipeline.log'), # Persistencia para auditoría histórica
        lg.StreamHandler()              # Monitoreo en tiempo real por terminal
    ]
)

logger = lg.getLogger(__name__)
```

**Beneficio Técnico:** Esta configuración permite desacoplar la ejecución del monitoreo. Mientras el `FileHandler` genera una bitácora persistente para análisis forense de errores, el `StreamHandler` facilita la observabilidad inmediata durante el desarrollo.

---

### 🛠️ Arquitectura del Sistema

El pipeline implementa un patrón **ETL** optimizado para la detección de errores:

1.  **Extracción:** Simulación de ingesta de datos con "ruido" técnico (espacios excesivos, tipos inconsistentes).
2.  **Transformación (con Auditoría):**
    *   **Data Cleaning:** Normalización a *Title Case* y casting de tipos.
    *   **Lógica de Auditoría:** Conteo y registro automático de registros defectuosos en el log.
3.  **Carga:** Persistencia relacional en **SQLite** mediante **SQLAlchemy**, garantizando la integridad de las tablas.

---

### 📦 Requisitos e Instalación

Para ejecutar este pipeline, instala las dependencias necesarias:

```bash
pip install pandas sqlalchemy
```

---

### 📖 Guía de Uso

1.  **Ejecución:** Corre el script principal:
    ```bash
    python pipeline_2.py
    ```
2.  **Monitoreo:** Revisa el archivo generado `pipeline.log` para auditar los eventos de la ejecución.
3.  **Verificación:** Consulta la base de datos `mi_proyecto.db` para ver los resultados finales.

---
**Ingeniería en Sistemas Computacionales** | *Construyendo sistemas de datos transparentes y confiables.*
