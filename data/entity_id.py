import random
from config import SourceDbConfig
from sqlalchemy.engine import Engine
from util.sql_helpers import get_current_identity


def records_exist(entity_id: int):
    return entity_id != 0

def cliente_id(con: Engine):
    return get_current_identity(SourceDbConfig.Table.CLIENTES, con, id_column='ID_CLIENTE')

def motivo_id(con: Engine):
    return get_current_identity(SourceDbConfig.Table.MOTIVOS, con, id_column='ID_MOTIVO')

def orden_id(con: Engine):
    return get_current_identity(SourceDbConfig.Table.ORDENES, con, id_column='ID_ORDEN')

def provincia_id(con: Engine):
    return get_current_identity(SourceDbConfig.Table.PROVINCIAS, con, id_column='ID_PROVINCIA')

def servicio_id(con: Engine):
    return get_current_identity(SourceDbConfig.Table.SERVICIOS, con, id_column='ID_SERVICIO')


# Generate a random ID for a given entity

def rand_provincia(end: int):
    return random.randint(1, end)

def rand_motivo(start: int = 1, end: int = 1):
    return random.randint(start, end)

def rand_servicio(end: int):
    return random.randint(1, end)

def rand_cliente(end: int):
    return random.randint(1, end)