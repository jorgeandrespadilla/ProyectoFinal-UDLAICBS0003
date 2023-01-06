from sqlalchemy.engine import Engine
from config import DbConfig
from util.sql_helpers import read_table
from transform.transformations import parse_date

table_columns = [
    'CODIGO_ORDEN',
    'CODIGO_CLIENTE',
    'CODIGO_SERVICIO',
    'CODIGO_PROVINCIA',
    'CODIGO_MOTIVO',
    'ESTADO_ORDEN',
    'FECHA_ADQUISICION',
]


def transform_ordenes(db_con: Engine, etl_process_id: int) -> None:
    # Read from extract table
    ordenes_ext = read_table(
        table_name=DbConfig.ExtractTable.ORDENES,
        columns=table_columns,
        con=db_con
    )

    ordenes_df = ordenes_ext.copy(deep=True)
    if not ordenes_ext.empty:
        # Tranform columns
        ordenes_df['FECHA_ADQUISICION'] = ordenes_df['FECHA_ADQUISICION'].apply(parse_date)
        # Add ETL process ID
        ordenes_df['ETL_PROC_ID'] = etl_process_id
        # Write to transform table
        ordenes_df.to_sql(DbConfig.TransformTable.ORDENES, con=db_con, if_exists='append', index=False)
