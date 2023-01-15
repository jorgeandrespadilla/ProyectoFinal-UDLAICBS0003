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
  - `etl`: directorio que contiene los scripts SQL para la creación de tablas de la base de datos de ETL.
  - `source`: directorio que contiene los scripts SQL para la creación de tablas de la base de datos fuente.
- `util`: directorio que contiene los archivos de utilidades de la aplicación.
- `config.py`: archivo de configuración de la aplicación.
- `data_setup.py`: archivo que genera los datos aleatorios.
- `etl_process.py`: archivo que ejecuta el proceso de ETL.

## Instalación de paquetes

Para instalar los paquetes necesarios usados por Python, se debe ejecutar el comando `pip install -r requirements.txt`.

## Configuración de la base de datos

Modificar los archivos de configuración `etl_db.properties` y `source_db.properties` en el directorio `config` con las configuraciones de conexión a la base de datos correspondientes.

## Ejecución de scripts SQL

Los scripts SQL del proyecto se encuentran ubicados en el directorio `sql`.

Para la base de datos fuente, los script SQL se encuentran en el directorio `sql/source` y se deben ejecutar en el siguiente orden:
1. `1_source-initialization.sql` (inicialización de esquemas de la base de datos fuente)
2. `2_source-tables.sql` (creación de tablas de la base fuente)
  
Para la base de datos de ETL, los script SQL se encuentran en el directorio `sql/etl` y se deben ejecutar en el siguiente orden:
1. `1_etl-initialization.sql` (inicialización de esquemas de la base de datos de ETL)
2. `2_ext-tables.sql` (creación de tablas de extracción)
3. `3_tra-tables.sql` (creación de tablas de transformación)
4. `4_sor-tables.sql` (creación de tablas de la base SOR)

## Generación de datos	

Para generar los datos, se debe ejecutar el comando `python data_setup.py` en la raíz del proyecto. Este comando genera los archivos CSV en el directorio `data/csv`.

## Ejecución de ETL

Para ejecutar el ETL, se debe ejecutar el comando `python etl_process.py` en la raíz del proyecto.