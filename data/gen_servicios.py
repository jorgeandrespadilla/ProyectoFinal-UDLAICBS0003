import pandas as pd
from config import DataConfig
from data.entity_constants import servicios_data
from data.entity_code import servicio_code
from util.data_faker import add_record, generate_csv


def generate_servicios():
    servicios = pd.DataFrame()
    for i in range(DataConfig.Records.SERVICIOS):
        data = servicios_data[i]
        servicios = add_record(servicios, {
            'codigo_servicio': servicio_code(i+1),
            'descripcion_servicio': data.description,
            'valor_servicio': data.cost,
            'tiempo_subscripcion': data.time,
            'beneficios_servicio': data.benefits,
        })
    generate_csv(servicios, DataConfig.Csv.SERVICIOS)
