from util.sql_helpers import SchemaConnection
from .load_clientes import load_clientes
from .load_motivos import load_motivos
from .load_ordenes import load_ordenes
from .load_premios import load_premios
from .load_provincias import load_provincias
from .load_servicios import load_servicios


def load(schema_con: SchemaConnection, etl_process_id: int):
    load_provincias(schema_con, etl_process_id)
    load_servicios(schema_con, etl_process_id)
    load_motivos(schema_con, etl_process_id)
    load_clientes(schema_con, etl_process_id)
    load_ordenes(schema_con, etl_process_id)
    load_premios(schema_con, etl_process_id)
