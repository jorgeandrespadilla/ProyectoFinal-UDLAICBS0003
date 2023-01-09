import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, SourceDbConfig
from constants.entities import servicios_data
from data.entity_id import servicio_id, records_exist
from util.data_faker import add_record


def generate_servicios(db_con: Engine):
    servicios = pd.DataFrame()
    if records_exist(servicio_id(db_con)):
        print("Servicios already available")
        return
    for i in range(DataConfig.Records.SERVICIOS):
        data = servicios_data[i]
        servicios = add_record(servicios, {
            'descripcion_servicio': data.description,
            'valor_servicio': data.cost,
            'tiempo_subscripcion': data.time,
            'beneficios_servicio': data.benefits,
        })
    servicios.to_sql(SourceDbConfig.Table.SERVICIOS, db_con, if_exists='append', index=False)
