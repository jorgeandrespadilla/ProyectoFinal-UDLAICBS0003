from config import EtlDbConfig
from util.sql_helpers import SchemaConnection, merge_and_insert, read_table

table_columns = [
    'ID_MOTIVO',
    'DESCRIPCION_MOTIVO',
]


def load_motivos(schema_con: SchemaConnection, etl_process_id: int) -> None:
    motivos_tra = read_table(
        table_name=EtlDbConfig.TransformTable.MOTIVOS,
        columns=table_columns,
        con=schema_con.STG,
        with_process_id=etl_process_id
    )
    motivos_sor = read_table(
        table_name=EtlDbConfig.SorTable.MOTIVOS,
        columns=['ID', *table_columns],
        con=schema_con.SOR
    )
    merge_and_insert(
        source_df=motivos_tra,
        target_table=EtlDbConfig.SorTable.MOTIVOS,
        target_df=motivos_sor,
        key_columns=['ID_MOTIVO'],
        db_con=schema_con.SOR
    )
