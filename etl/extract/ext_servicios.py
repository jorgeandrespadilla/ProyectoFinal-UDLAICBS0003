import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, DbConfig

# csv_col_name: db_col_name
columns_map = {
    'codigo_servicio': 'codigo_servicio',
    'descripcion_servicio': 'descripcion_servicio',
    'valor_servicio': 'valor_servicio',
    'tiempo_subscripcion': 'tiempo_subscripcion',
    'beneficios_servicio': 'beneficios_servicio',
}


def extract_servicios(db_con: Engine):
    # Read CSV
    servicios_csv = pd.read_csv(DataConfig.Csv.SERVICIOS, dtype=str)
    if not servicios_csv.empty:
        # Assign database column names
        servicios_df = servicios_csv.rename(columns=columns_map)
        # Write to database
        db_con.connect().execute(
            f'TRUNCATE TABLE {DbConfig.ExtractTable.SERVICIOS}')
        servicios_df.to_sql(DbConfig.ExtractTable.SERVICIOS,
                            db_con, if_exists='append', index=False)
