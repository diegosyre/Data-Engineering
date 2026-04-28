
Pipeline ETL con Observabilidad y Auditoría (v2)



Este proyecto representa la evolución de mi primer pipeline de datos, pasando de una estructura funcional básica a un sistema robusto con principios de ingeniería de datos.



🚀 Evolución del Proyecto

En esta etapa, el enfoque se desplazó hacia la observabilidad y la trazabilidad. No basta con mover datos; es necesario saber exactamente qué ocurrió durante el proceso.



\### Mejoras Implementadas

* Logging Profesional: Sustitución de `print()` por el módulo `logging` de Python.
* Niveles de Severidad: Uso de `INFO` para flujo normal, `WARNING` para inconsistencias de datos y `ERROR` para fallos críticos.
* Persistencia de Logs: Configuración de un `FileHandler` para almacenar la bitácora en un archivo `.log` externo, facilitando auditorías futuras.
* Tratamiento de Errores: Identificación y registro de valores nulos o inválidos antes de la transformación (Data Profiling básico).



🛠️ Arquitectura del Sistema



El pipeline sigue el patrón clásico ETL (Extract, Transform, Load):



1\.  Extracción: Simulación de ingesta de datos con diversos tipos de errores (strings con espacios, valores no numéricos).

2\.  Transformación: Limpieza y normalización de texto (Title Case).

&#x20;    \* Conversión de tipos de datos.

&#x20;    \* Lógica de Auditoría: Conteo y registro en log de registros defectuosos antes de la imputación.

3\.  Carga: Persistencia en una base de datos \*\*SQLite\*\* mediante \*\*SQLAlchemy\*\*, asegurando que la tabla se actualice correctamente.



📋 Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

\* Python 3.12

\* Pandas (`pip install pandas`)

\* SQLAlchemy (`pip install sqlalchemy`)



📖 Cómo usarlo

1\. Clona el repositorio.

2\. Ejecuta el script principal: `python pipeline\_2.py`.

3\. Revisa el archivo generado `pipeline.log` para ver el historial de la ejecución.

4\. Consulta la base de datos `mi\_proyecto.db` para ver los resultados finales.




