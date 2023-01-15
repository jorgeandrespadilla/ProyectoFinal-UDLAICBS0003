from config import EtlDbConfig
from util.sql_helpers import SchemaConnection, merge_and_insert, read_table

table_columns = [
    'ID_SERVICIO',
    'DESCRIPCION_SERVICIO',
    'VALOR_SERVICIO',
    'TIEMPO_SUBSCRIPCION',
    'BENEFICIOS_SERVICIO',
]


def load_servicios(schema_con: SchemaConnection, etl_process_id: int) -> None:
    servicios_tra = read_table(
        table_name=EtlDbConfig.TransformTable.SERVICIOS,
        columns=table_columns,
        con=schema_con.STG,
        with_process_id=etl_process_id
    )
    servicios_sor = read_table(
        table_name=EtlDbConfig.SorTable.SERVICIOS,
        columns=['ID', *table_columns],
        con=schema_con.SOR
    )
    merge_and_insert(
        source_df=servicios_tra,
        target_table=EtlDbConfig.SorTable.SERVICIOS,
        target_df=servicios_sor,
        key_columns=['ID_SERVICIO'],
        db_con=schema_con.SOR
    )
