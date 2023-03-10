from sqlalchemy.engine import Engine
from config import EtlDbConfig
from util.sql_helpers import read_table

table_columns = [
    'ID_MOTIVO',
    'DESCRIPCION_MOTIVO',
]


def transform_motivos(db_con: Engine, etl_process_id: int) -> None:
    # Read from extract table
    motivos_ext = read_table(
        table_name=EtlDbConfig.ExtractTable.MOTIVOS,
        columns=table_columns,
        con=db_con
    )

    motivos_df = motivos_ext.copy(deep=True)
    if not motivos_ext.empty:
        # Add ETL process ID
        motivos_df[EtlDbConfig.ETL_PROCESS_COL] = etl_process_id
        # Write to transform table
        motivos_df.to_sql(EtlDbConfig.TransformTable.MOTIVOS, con=db_con, if_exists='append', index=False)
