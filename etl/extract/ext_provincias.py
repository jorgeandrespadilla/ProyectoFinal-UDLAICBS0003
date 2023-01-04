import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, DbConfig

# csv_col_name: db_col_name
columns_map = {
    'codigo_provincia': 'codigo_provincia',
    'nombre_provincia': 'nombre_provincia',
}


def extract_provincias(db_con: Engine):
    # Read CSV
    provincias_csv = pd.read_csv(DataConfig.Csv.PROVINCIAS, dtype=str)
    if not provincias_csv.empty:
        # Assign database column names
        provincias_df = provincias_csv.rename(columns=columns_map)
        # Write to database
        db_con.connect().execute(
            f'TRUNCATE TABLE {DbConfig.ExtractTable.PROVINCIAS}')
        provincias_df.to_sql(DbConfig.ExtractTable.PROVINCIAS,
                             db_con, if_exists='append', index=False)
