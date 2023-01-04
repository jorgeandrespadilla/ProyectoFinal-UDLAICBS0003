from sqlalchemy.engine import Engine
from .ext_clientes import extract_clientes
from .ext_motivos import extract_motivos
from .ext_ordenes import extract_ordenes
from .ext_provincias import extract_provincias
from .ext_servicios import extract_servicios


def extract(db_con: Engine):
    extract_provincias(db_con)
    extract_servicios(db_con)
    extract_motivos(db_con)
    extract_clientes(db_con)
    extract_ordenes(db_con)
