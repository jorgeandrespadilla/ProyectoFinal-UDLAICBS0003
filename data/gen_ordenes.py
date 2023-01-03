import random
import pandas as pd
from config import DataConfig
from data.entity_code import cliente_code, motivo_code, orden_code, provincia_code, servicio_code
from util.data_faker import add_record, generate_csv, generate_date, random_choice


def generate_ordenes():
    ordenes = pd.DataFrame()
    for i in range(DataConfig.Records.ORDENES):
        estado = random_choice({
            'EXITOSO': 9,
            'FALLIDO': 1
        })
        codigo_motivo_by_estado = {
            'EXITOSO': motivo_code(1),
            'FALLIDO': motivo_code(random.randint(2, DataConfig.Records.MOTIVOS))
        }
        ordenes = add_record(ordenes, {
            'codigo_orden': orden_code(i+1),
            'codigo_cliente': cliente_code(),
            'codigo_servicio': servicio_code(),
            'codigo_provincia': provincia_code(),
            'codigo_motivo': codigo_motivo_by_estado[estado],
            'estado_orden': estado,
            'fecha_adquisicion': generate_date('2021-01-01', '2022-11-30')
        })
    generate_csv(ordenes, DataConfig.Csv.ORDENES)
