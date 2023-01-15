import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, SourceDbConfig
from constants.entities import provincias_data
from data.entity_id import provincia_id, records_exist
from util.data_faker import add_record


def generate_provincias(db_con: Engine):
    provincias = pd.DataFrame()
    if records_exist(provincia_id(db_con)):
        print("Provincias already available")
        return
    for i in range(DataConfig.Records.PROVINCIAS):
        provincias = add_record(provincias, {
            'nombre_provincia': provincias_data[i].name,
        })
    provincias.to_sql(SourceDbConfig.Table.PROVINCIAS, db_con, if_exists='append', index=False)
