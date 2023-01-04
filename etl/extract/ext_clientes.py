import pandas as pd
from sqlalchemy.engine import Engine
from config import DataConfig, DbConfig

# csv_col_name: db_col_name
columns_map = {
    'codigo_cliente': 'codigo_cliente',
    'codigo_provincia': 'codigo_provincia',
    'nombre_cliente': 'nombre_cliente',
    'tipo_cliente': 'tipo_cliente',
}


def extract_clientes(db_con: Engine):
    # Read CSV
    clientes_csv = pd.read_csv(DataConfig.Csv.CLIENTES, dtype=str)
    if not clientes_csv.empty:
        # Assign database column names
        clientes_df = clientes_csv.rename(columns=columns_map)
        # Write to database
        db_con.connect().execute(
            f'TRUNCATE TABLE {DbConfig.ExtractTable.CLIENTES}')
        clientes_df.to_sql(DbConfig.ExtractTable.CLIENTES,
                           db_con, if_exists='append', index=False)
