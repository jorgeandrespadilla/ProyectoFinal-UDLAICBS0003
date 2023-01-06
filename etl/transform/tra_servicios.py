from sqlalchemy.engine import Engine
from config import DbConfig
from util.sql_helpers import read_table

table_columns = [
    'CODIGO_SERVICIO',
    'DESCRIPCION_SERVICIO',
    'VALOR_SERVICIO',
    'TIEMPO_SUBSCRIPCION',
    'BENEFICIOS_SERVICIO',
]


def transform_servicios(db_con: Engine, etl_process_id: int) -> None:
    # Read from extract table
    servicios_ext = read_table(
        table_name=DbConfig.ExtractTable.SERVICIOS,
        columns=table_columns,
        con=db_con
    )

    servicios_df = servicios_ext.copy(deep=True)
    if not servicios_ext.empty:
        # Tranform columns
        servicios_df['VALOR_SERVICIO'] = servicios_df['PROMO_COST'].astype(float)
        servicios_df['TIEMPO_SUBSCRIPCION'] = servicios_df['PROMO_ID'].astype(int)
        # Add ETL process ID
        servicios_df['ETL_PROC_ID'] = etl_process_id
        # Write to transform table
        servicios_df.to_sql(DbConfig.TransformTable.SERVICIOS, con=db_con, if_exists='append', index=False)
