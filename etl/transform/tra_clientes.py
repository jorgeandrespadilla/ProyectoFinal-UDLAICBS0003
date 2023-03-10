from sqlalchemy.engine import Engine
from config import EtlDbConfig
from util.sql_helpers import read_table

table_columns = [
    'ID_CLIENTE',
    'ID_PROVINCIA',
    'NOMBRE_CLIENTE',
    'TIPO_CLIENTE',
]


def transform_clientes(db_con: Engine, etl_process_id: int) -> None:
    # Read from extract table
    clientes_ext = read_table(
        table_name=EtlDbConfig.ExtractTable.CLIENTES,
        columns=table_columns,
        con=db_con
    )

    clientes_df = clientes_ext.copy(deep=True)
    if not clientes_ext.empty:
        # Add ETL process ID
        clientes_df[EtlDbConfig.ETL_PROCESS_COL] = etl_process_id
        # Write to transform table
        clientes_df.to_sql(EtlDbConfig.TransformTable.CLIENTES, con=db_con, if_exists='append', index=False)
