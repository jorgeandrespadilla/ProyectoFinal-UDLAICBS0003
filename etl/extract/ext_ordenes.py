import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, DbConfig

# csv_col_name: db_col_name
columns_map = {
    'codigo_orden': 'codigo_orden',
    'codigo_cliente': 'codigo_cliente',
    'codigo_servicio': 'codigo_servicio',
    'codigo_provincia': 'codigo_provincia',
    'codigo_motivo': 'codigo_motivo',
    'estado_orden': 'estado_orden',
    'fecha_adquisicion': 'fecha_adquisicion',
}


def extract_ordenes(db_con: Engine):
    # Read CSV
    ordenes_csv = pd.read_csv(DataConfig.Csv.ORDENES, dtype=str)
    if not ordenes_csv.empty:
        # Assign database column names
        ordenes_df = ordenes_csv.rename(columns=columns_map)
        # Write to database
        db_con.connect().execute(
            f'TRUNCATE TABLE {DbConfig.ExtractTable.ORDENES}')
        ordenes_df.to_sql(DbConfig.ExtractTable.ORDENES,
                          db_con, if_exists='append', index=False)
