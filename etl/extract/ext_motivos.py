import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, DbConfig

# csv_col_name: db_col_name
columns_map = {
    'codigo_motivo': 'codigo_motivo',
    'descripcion_motivo': 'descripcion_motivo',
}


def extract_motivos(db_con: Engine):
    # Read CSV
    motivos_csv = pd.read_csv(DataConfig.Csv.MOTIVOS, dtype=str)
    if not motivos_csv.empty:
        # Assign database column names
        motivos_df = motivos_csv.rename(columns=columns_map)
        # Write to database
        db_con.connect().execute(
            f'TRUNCATE TABLE {DbConfig.ExtractTable.MOTIVOS}')
        motivos_df.to_sql(DbConfig.ExtractTable.MOTIVOS,
                           db_con, if_exists='append', index=False)
