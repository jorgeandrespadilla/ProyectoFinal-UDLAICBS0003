# Proyecto Final - Visualización de Datos (ICBS0003)

## Integrantes

- Jorge Padilla
- Daniel Bustos
- Alain Ruales

## Descripción

Este repositorio contiene el código fuente usado para el proyecto final de Visualización de Datos. Para ello, se utilizó Python 3.10 y MySQL 8.0 para el almacenamiento de datos.

## Estructura del proyecto

El proyecto está estructurado de la siguiente manera:
- `config`: directorio que contiene los archivos de configuración de la aplicación.
  - `etl_db.properties`: archivo de configuración de la base de datos de ETL.
  - `source_db.properties`: archivo de configuración de la base de datos fuente.
- `constants`: directorio que contiene los archivos de constantes de la aplicación.
- `data`: directorio que contiene los archivos para la generación de datos aleatorios.
  - `csv`: directorio que contiene los archivos CSV con los datos generados.
- `etl`: directorio que contiene los scripts de ETL.
  - `extract`: directorio que contiene los scripts de extracción de datos.
  - `transform`: directorio que contiene los scripts de transformación de datos.
  - `load`: directorio que contiene los scripts de carga de datos.
- `sql`: directorio que contiene los scripts SQL para la creación de tablas de la base de datos.
- `util`: directorio que contiene los archivos de utilidades de la aplicación.

## Instalación de paquetes

Para instalar los paquetes necesarios usados por Python, se debe ejecutar el comando `pip install -r requirements.txt`

## Configuración de la base de datos

Modificar los archivos de configuración `etl_db.properties` y `source_db.properties` en el directorio `config` con las configuraciones de conexión a la base de datos correspondientes.

## Ejecución de scripts SQL

Los scripts SQL se encuentran ubicados en el directorio `sql`, y se deben ejecutar en una base de datos MySQL en el siguiente orden:
1. `source-initialization.sql` (inicialización de esquemas de la base de datos fuente)
2. `source-tables.sql` (creación de tablas de la base fuente)
3. `etl-initialization.sql` (inicialización de esquemas de la base de datos de ETL)
4. `ext-tables.sql` (creación de tablas de extracción)
5. `tra-tables.sql` (creación de tablas de transformación)
6. `sor-tables.sql` (creación de tablas de la base SOR)

## Generación de datos	

Para generar los datos, se debe ejecutar el comando `python data_setup.py` en la raíz del proyecto. Este comando genera los archivos CSV en el directorio `data/csv`.

## Ejecución de ETL

Para ejecutar el ETL, se debe ejecutar el comando `python etl_process.py` en la raíz del proyecto.