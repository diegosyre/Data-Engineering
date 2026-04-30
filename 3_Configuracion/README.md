\# 🛠️ Módulo 03: Configuración y Seguridad de Entorno



Este módulo demuestra la implementación de un sistema de configuración profesional para pipelines de datos, priorizando la \*\*soberanía de los datos\*\* y la \*\*seguridad de la información\*\* mediante el aislamiento de variables sensibles.



\## 🎯 Objetivo

Establecer una capa base de configuración que permita al sistema conectarse a recursos externos (bases de datos, APIs) sin exponer credenciales o rutas críticas en el código fuente.



\## 🚀 Características Técnicas

\*   \*\*Gestión de Variables de Entorno\*\*: Uso de la librería `python-dotenv` para inyectar configuraciones dinámicas desde un archivo `.env`.

\*   \*\*Monitoreo Robusto (Logging)\*\*: Implementación de un sistema de trazabilidad que registra eventos en tiempo real tanto en consola como en un archivo físico (`pipeline.log`).

\*   \*\*Aislamiento de Datos\*\*: Configuración estratégica de `.gitignore` para prevenir la fuga de información sensible hacia repositorios públicos.

\*   \*\*Arquitectura Modular\*\*: Código diseñado para ser escalable y fácilmente integrable con futuros módulos de extracción (APIs) y transformación.



\## 📂 Estructura del Módulo

```text

3\_Configuracion/

├── main.py          # Motor lógico del sistema de configuración.

├── .env             # Bóveda de seguridad (protegido por .gitignore).

└── pipeline.log     # Historial de monitoreo generado en ejecución.



\## 🛠️ Instalación y Uso

Instalar dependencias:



pip install python-dotenv



Configurar el entorno:

Crea un archivo .env en esta carpeta con la siguiente estructura:



DB\_NAME=nombre\_de\_tu\_base.db

Ejecutar:

python main.py

