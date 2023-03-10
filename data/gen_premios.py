import random
import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig
from constants.entities import premios_data
from data.entity_id import cliente_id, rand_cliente
from util.data_faker import random_choice, add_record, generate_csv


def generate_premios(db_con: Engine):
    premios = pd.DataFrame()
    max_cliente_id = cliente_id(db_con)
    existing_clientes = [None] # Already existing id_cliente
    for i in range(DataConfig.Records.PREMIOS):
        # Choose random list element
        data = random.choice(premios_data)
        cl_id = None
        while cl_id in existing_clientes: 
            cl_id = rand_cliente(max_cliente_id)
        existing_clientes.append(cl_id)

        canjeado = random_choice({
            'S': 1,
            'N': 1
        })
        premios = add_record(premios, {
            'ID_PREMIO': i + 1,
            'ID_CLIENTE': cl_id,
            'DESCRIPCION_PREMIO': data.description,
            'VALOR_PREMIO': data.cost,
            'CANJEADO': canjeado
        })
    generate_csv(premios, DataConfig.Csv.PREMIOS)
