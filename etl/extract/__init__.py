from .ext_clientes import extract_clientes
from .ext_motivos import extract_motivos
from .ext_ordenes import extract_ordenes
from .ext_premios import extract_premios
from .ext_provincias import extract_provincias
from .ext_servicios import extract_servicios
from util.sql_helpers import SchemaConnection


def extract(schema_con: SchemaConnection):
    extract_provincias(schema_con)
    extract_servicios(schema_con)
    extract_motivos(schema_con)
    extract_clientes(schema_con)
    extract_ordenes(schema_con)
    extract_premios(schema_con)
