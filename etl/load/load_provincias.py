from config import EtlDbConfig
from util.sql_helpers import SchemaConnection, merge_and_insert, read_table

table_columns = [
    'ID_PROVINCIA',
    'NOMBRE_PROVINCIA',
]


def load_provincias(schema_con: SchemaConnection, etl_process_id: int) -> None:
    provincias_tra = read_table(
        table_name=EtlDbConfig.TransformTable.PROVINCIAS,
        columns=table_columns,
        con=schema_con.STG,
        with_process_id=etl_process_id
    )
    provincias_sor = read_table(
        table_name=EtlDbConfig.SorTable.PROVINCIAS,
        columns=['ID', *table_columns],
        con=schema_con.SOR
    )
    merge_and_insert(
        source_df=provincias_tra,
        target_table=EtlDbConfig.SorTable.PROVINCIAS,
        target_df=provincias_sor,
        key_columns=['ID_PROVINCIA'],
        db_con=schema_con.SOR
    )
