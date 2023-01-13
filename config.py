import os
from jproperties import Properties
from constants.entities import total_provincias, total_motivos, total_servicios


def read_config(file_path: str) -> dict:
    """
    Reads a properties file and returns a dictionary with the values.
    """
    data_configs = Properties()
    with open(file_path, 'rb') as config_file:
        data_configs.load(config_file)
    data_dict = {key: str(data_configs.get(key).data) for key in data_configs}
    return data_dict


def get_csv_path(file_name: str) -> str:
    """
    Gets the full path of a CSV file.
    """
    return os.path.join(CSV_PATH, file_name)


source_db_config = read_config('./config/source_db.properties') # Read source DB properties file
etl_db_config = read_config('./config/etl_db.properties')  # Read ETL DB properties file
CSV_PATH = os.path.abspath('./data/csv')  # Path to CSV folder

class DbConnectionConfig:
    NAME = ""
    HOST = ""
    PORT = ""
    USER = ""
    PASSWORD = ""


# Database to extract data from
class SourceDbConfig:
    class Connection(DbConnectionConfig):
        NAME = source_db_config['DB_NAME']
        HOST = source_db_config['DB_HOST']
        PORT = source_db_config['DB_PORT']
        USER = source_db_config['DB_USER']
        PASSWORD = source_db_config['DB_PASSWORD']

    DATABASE_SCHEMA = source_db_config['DB_SCHEMA']

    class Table:
        PROVINCIAS = 'provincias'
        SERVICIOS = 'servicios'
        MOTIVOS = 'motivos'
        CLIENTES = 'clientes'
        ORDENES = 'ordenes'


# Database to load data into
class EtlDbConfig:
    class Connection(DbConnectionConfig):
        NAME = etl_db_config['DB_NAME']
        HOST = etl_db_config['DB_HOST']
        PORT = etl_db_config['DB_PORT']
        USER = etl_db_config['DB_USER']
        PASSWORD = etl_db_config['DB_PASSWORD']

    # Database schemas
    class Schema:
        SOR = etl_db_config['DB_SOR_SCHEMA']
        STG = etl_db_config['DB_STG_SCHEMA']

    # Extraction tables (staging)
    class ExtractTable:
        PROVINCIAS = 'provincias_ext'
        SERVICIOS = 'servicios_ext'
        MOTIVOS = 'motivos_ext'
        CLIENTES = 'clientes_ext'
        ORDENES = 'ordenes_ext'
        PREMIOS = 'premios_ext'

    # Transformation tables (staging)
    class TransformTable:
        PROVINCIAS = 'provincias_tra'
        SERVICIOS = 'servicios_tra'
        MOTIVOS = 'motivos_tra'
        CLIENTES = 'clientes_tra'
        ORDENES = 'ordenes_tra'
        PREMIOS = 'premios_tra'

    # Final tables (SOR)
    class SorTable:
        PROVINCIAS = 'provincias'
        SERVICIOS = 'servicios'
        MOTIVOS = 'motivos'
        CLIENTES = 'clientes'
        ORDENES = 'ordenes'
        PREMIOS = 'premios'

    ETL_PROCESS_TABLE = 'procesos_etl'


# Data generation configuration
class DataConfig:
    # Number of records to generate
    class Records:
        PROVINCIAS = total_provincias
        SERVICIOS = total_servicios
        MOTIVOS = total_motivos
        CLIENTES = 82
        ORDENES = 1000
        PREMIOS = 40

    # CSV files
    class Csv:
        PREMIOS = get_csv_path('premios.csv')
