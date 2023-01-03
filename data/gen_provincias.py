import pandas as pd
from config import DataConfig
from data.entity_constants import provincias_name
from data.entity_code import provincia_code
from util.data_faker import add_record, generate_csv


def generate_provincias():
    provincias = pd.DataFrame()
    for i in range(DataConfig.Records.PROVINCIAS):
        provincias = add_record(provincias, {
            'codigo_provincia': provincia_code(i+1),
            'nombre_provincia': provincias_name[i],
        })
    generate_csv(provincias, DataConfig.Csv.PROVINCIAS)
