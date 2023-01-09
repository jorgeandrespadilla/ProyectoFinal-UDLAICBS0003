from sqlalchemy.engine import Engine
from .gen_provincias import generate_provincias
from .gen_servicios import generate_servicios
from .gen_clientes import generate_clientes
from .gen_ordenes import generate_ordenes
from .gen_premios import generate_premios
from .gen_motivos import generate_motivos


def generate_data(db_con: Engine):
    generate_provincias(db_con)
    generate_servicios(db_con)
    generate_motivos(db_con)
    generate_clientes(db_con)
    generate_ordenes(db_con)
    generate_premios(db_con)
