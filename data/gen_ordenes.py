import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, SourceDbConfig
from data.entity_id import cliente_id, motivo_id, provincia_id, rand_cliente, rand_motivo, rand_provincia, rand_servicio, servicio_id
from util.data_faker import add_record, generate_date, random_choice


def generate_ordenes(db_con: Engine):
    ordenes = pd.DataFrame()
    max_cliente_id = cliente_id(db_con)
    max_servicio_id = servicio_id(db_con)
    max_provincia_id = provincia_id(db_con)
    max_motivo_id = motivo_id(db_con)
    for _ in range(DataConfig.Records.ORDENES):
        estado = random_choice({
            'EXITOSO': 9,
            'FALLIDO': 1
        })
        codigo_motivo_by_estado = {
            'EXITOSO': 1,
            'FALLIDO': rand_motivo(2, max_motivo_id)
        }
        ordenes = add_record(ordenes, {
            'id_cliente': rand_cliente(max_cliente_id),
            'id_servicio': rand_servicio(max_servicio_id),
            'id_provincia': rand_provincia(max_provincia_id),
            'id_motivo': codigo_motivo_by_estado[estado],
            'estado_orden': estado,
            'fecha_adquisicion': generate_date('2021-01-01', '2022-11-30')
        })
    ordenes.to_sql(SourceDbConfig.Table.ORDENES, db_con, if_exists='append', index=False)
