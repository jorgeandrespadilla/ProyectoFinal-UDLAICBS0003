import os
from jproperties import Properties
from data.entity_constants import total_provincias, total_motivos, total_servicios


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


db_config = read_config('./db.properties')  # Read DB properties file
CSV_PATH = os.path.abspath('./data/csv')  # Path to CSV folder


class DbConfig:
    HOST = db_config['DB_HOST']
    PORT = db_config['DB_PORT']
    USER = db_config['DB_USER']
    PASSWORD = db_config['DB_PASSWORD']

    # Database schemas
    class Schema:
        SOR = db_config['DB_SOR_SCHEMA']
        STG = db_config['DB_STG_SCHEMA']

    # Extraction tables (staging)
    class ExtractTable:
        PROVINCIAS = 'provincias_ext'
        SERVICIOS = 'servicios_ext'
        MOTIVOS = 'motivos_ext'
        CLIENTES = 'clientes_ext'
        ORDENES = 'ordenes_ext'

    # Transformation tables (staging)
    class TransformTable:
        PROVINCIAS = 'provincias_tra'
        SERVICIOS = 'servicios_tra'
        MOTIVOS = 'motivos_tra'
        CLIENTES = 'clientes_tra'
        ORDENES = 'ordenes_tra'

    # Final tables (SOR)
    class SorTable:
        PROVINCIAS = 'provincias'
        SERVICIOS = 'servicios'
        MOTIVOS = 'motivos'
        CLIENTES = 'clientes'
        ORDENES = 'ordenes'


class DataConfig:
    # Number of records to generate
    class Records:
        PROVINCIAS = total_provincias
        SERVICIOS = total_servicios
        MOTIVOS = total_motivos
        CLIENTES = 82
        ORDENES = 1000

    # CSV files
    class Csv:
        PROVINCIAS = get_csv_path('provincias.csv')
        SERVICIOS = get_csv_path('servicios.csv')
        MOTIVOS = get_csv_path('motivos.csv')
        CLIENTES = get_csv_path('clientes.csv')
        ORDENES = get_csv_path('ordenes.csv')
