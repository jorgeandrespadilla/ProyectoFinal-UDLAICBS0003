from .gen_provincias import generate_provincias
from .gen_servicios import generate_servicios
from .gen_clientes import generate_clientes
from .gen_ordenes import generate_ordenes
from .gen_motivos import generate_motivos


def generate_data():
    generate_provincias()
    generate_servicios()
    generate_motivos()
    generate_clientes()
    generate_ordenes()
