import pandas as pd
from config import DataConfig
from data.entity_constants import motivos_description
from data.entity_code import motivo_code
from util.data_faker import add_record, generate_csv


def generate_motivos():
    motivos = pd.DataFrame()
    for i in range(DataConfig.Records.MOTIVOS):
        motivos = add_record(motivos, {
            'codigo_motivo': motivo_code(i+1),
            'descripcion_motivo': motivos_description[i],
        })
    generate_csv(motivos, DataConfig.Csv.MOTIVOS)
