from sqlalchemy.engine import Engine
from config import EtlDbConfig
from util.sql_helpers import read_table
from .transformations import parse_date

table_columns = [
    'ID_ORDEN',
    'ID_CLIENTE',
    'ID_SERVICIO',
    'ID_PROVINCIA',
    'ID_MOTIVO',
    'ESTADO_ORDEN',
    'FECHA_ADQUISICION',
]


def transform_ordenes(db_con: Engine, etl_process_id: int) -> None:
    # Read from extract table
    ordenes_ext = read_table(
        table_name=EtlDbConfig.ExtractTable.ORDENES,
        columns=table_columns,
        con=db_con
    )

    ordenes_df = ordenes_ext.copy(deep=True)
    if not ordenes_ext.empty:
        # Tranform columns
        ordenes_df['FECHA_ADQUISICION'] = ordenes_df['FECHA_ADQUISICION'].apply(parse_date)
        # Add ETL process ID
        ordenes_df[EtlDbConfig.ETL_PROCESS_COL] = etl_process_id
        # Write to transform table
        ordenes_df.to_sql(EtlDbConfig.TransformTable.ORDENES, con=db_con, if_exists='append', index=False)
