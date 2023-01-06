from sqlalchemy.engine import Engine
from config import DbConfig
from util.sql_helpers import read_table

table_columns = [
    'CODIGO_PROVINCIA',
    'NOMBRE_PROVINCIA',
]


def transform_provincias(db_con: Engine, etl_process_id: int) -> None:
    # Read from extract table
    provincias_ext = read_table(
        table_name=DbConfig.ExtractTable.PROVINCIAS,
        columns=table_columns,
        con=db_con
    )

    provincias_df = provincias_ext.copy(deep=True)
    if not provincias_ext.empty:
        # Add ETL process ID
        provincias_df['ETL_PROC_ID'] = etl_process_id
        # Write to transform table
        provincias_df.to_sql(DbConfig.TransformTable.PROVINCIAS, con=db_con, if_exists='append', index=False)
