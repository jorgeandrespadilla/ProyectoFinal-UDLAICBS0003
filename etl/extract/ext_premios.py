import pandas as pd
from config import DataConfig, EtlDbConfig
from util.sql_helpers import SchemaConnection

# csv_col_name: db_col_name
columns_map = {
    'ID_PREMIO': 'id_premio',
    'ID_CLIENTE': 'id_cliente',
    'DESCRIPCION_PREMIO': 'descripcion_premio',
    'VALOR_PREMIO': 'valor_premio',
    'CANJEADO': 'canjeado',
}


def extract_premios(schema_con: SchemaConnection):
    # Read CSV
    premios_csv = pd.read_csv(DataConfig.Csv.PREMIOS, dtype=str)
    if not premios_csv.empty:
        # Assign database column names
        premios_df = premios_csv.rename(columns=columns_map)
        # Write to database
        schema_con.STG.connect().execute(f'TRUNCATE TABLE {EtlDbConfig.ExtractTable.PREMIOS}')
        premios_df.to_sql(EtlDbConfig.ExtractTable.PREMIOS, schema_con.STG, if_exists='append', index=False)
