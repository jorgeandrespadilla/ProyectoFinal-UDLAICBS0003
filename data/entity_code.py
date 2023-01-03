import random
from util.data_faker import generate_code
from config import DataConfig

# Generate a code for a given entity. If value is None, a random value is generated.


def cliente_code(value: int = None):
    if not value:
        value = random.randint(1, DataConfig.Records.CLIENTES)
    return generate_code('CL', value, 5)


def motivo_code(value: int = None):
    if not value:
        value = random.randint(1, DataConfig.Records.MOTIVOS)
    return generate_code('M', value, 3)


def orden_code(value: int = None):
    if not value:
        value = random.randint(1, DataConfig.Records.ORDENES)
    return generate_code('TR', value, 6)


def provincia_code(value: int = None):
    if not value:
        value = random.randint(1, DataConfig.Records.PROVINCIAS)
    return generate_code('EC', value, 2)


def servicio_code(value: int = None):
    if not value:
        value = random.randint(1, DataConfig.Records.SERVICIOS)
    return generate_code('S', value, 3)
