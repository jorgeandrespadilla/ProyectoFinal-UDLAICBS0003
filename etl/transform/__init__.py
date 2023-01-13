from sqlalchemy.engine import Engine

from .tra_clientes import transform_clientes
from .tra_motivos import transform_motivos
from .tra_ordenes import transform_ordenes
from .tra_premios import transform_premios
from .tra_provincias import transform_provincias
from .tra_servicios import transform_servicios


def transform(db_con: Engine, etl_process_id: int):
    transform_provincias(db_con, etl_process_id)
    transform_servicios(db_con, etl_process_id)
    transform_motivos(db_con, etl_process_id)
    transform_clientes(db_con, etl_process_id)
    transform_ordenes(db_con, etl_process_id)
    transform_premios(db_con, etl_process_id)
