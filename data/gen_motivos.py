import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, SourceDbConfig
from constants.entities import motivos_data
from util.data_faker import add_record
from .entity_id import motivo_id, records_exist


def generate_motivos(db_con: Engine):
    motivos = pd.DataFrame()
    if records_exist(motivo_id(db_con)):
        print("Motivos already available")
        return
    for i in range(DataConfig.Records.MOTIVOS):
        motivos = add_record(motivos, {
            'descripcion_motivo': motivos_data[i].description,
        })
    motivos.to_sql(SourceDbConfig.Table.MOTIVOS, db_con, if_exists='append', index=False)
