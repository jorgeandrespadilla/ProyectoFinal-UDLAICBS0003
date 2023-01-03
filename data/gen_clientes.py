import pandas as pd
from config import DataConfig
from data.entity_code import cliente_code, provincia_code
from util.data_faker import add_record, generate_csv, generate_fullname, random_choice, normalize_str, fake


def generate_clientes():
    clientes = pd.DataFrame()
    for i in range(DataConfig.Records.CLIENTES):
        tipo = random_choice({
            'NATURAL': 8,
            'EMPRESA': 2
        })
        clientes = add_record(clientes, {
            'codigo_cliente': cliente_code(i+1),
            'codigo_provincia': provincia_code(),
            'nombre_cliente': generate_fullname() if tipo == 'NATURAL' else normalize_str(fake.company()),
            'tipo_cliente': tipo
        })
    generate_csv(clientes, DataConfig.Csv.CLIENTES)
