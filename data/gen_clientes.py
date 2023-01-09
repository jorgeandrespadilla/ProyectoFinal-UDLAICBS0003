import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, SourceDbConfig
from .entity_id import provincia_id, rand_provincia
from util.data_faker import add_record, generate_fullname, random_choice, normalize_str, fake



def generate_clientes(db_con: Engine):
    clientes = pd.DataFrame()
    max_provincia_id = provincia_id(db_con)
    for _ in range(DataConfig.Records.CLIENTES):
        tipo = random_choice({
            'NATURAL': 8,
            'EMPRESA': 2
        })
        clientes = add_record(clientes, {
            'id_provincia': rand_provincia(max_provincia_id),
            'nombre_cliente': generate_fullname() if tipo == 'NATURAL' else normalize_str(fake.company()),
            'tipo_cliente': tipo
        })
    clientes.to_sql(SourceDbConfig.Table.CLIENTES, db_con, if_exists='append', index=False)
