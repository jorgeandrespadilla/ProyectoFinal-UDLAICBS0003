from config import EtlDbConfig
from util.sql_helpers import Relationship, SchemaConnection, map_relationships, merge_and_insert, read_table

table_columns = [
    'ID_PREMIO',
    'ID_CLIENTE',
    'DESCRIPCION_PREMIO',
    'VALOR_PREMIO',
    'CANJEADO',
]

def load_premios(schema_con: SchemaConnection, etl_process_id: int) -> None:
    premios_tra = read_table(
        table_name=EtlDbConfig.TransformTable.PREMIOS,
        columns=table_columns,
        con=schema_con.STG,
        with_process_id=etl_process_id
    )
    premios_sor = read_table(
        table_name=EtlDbConfig.SorTable.PREMIOS,
        columns=['ID', *table_columns],
        con=schema_con.SOR
    )
    premios_with_relationships = map_relationships(
        df=premios_tra,
        con=schema_con.SOR,
        relationships=[
            Relationship(
                destination_column='ID_CLIENTE', source_table=EtlDbConfig.SorTable.CLIENTES,
                source_column='ID_CLIENTE',
            ),
        ]
    )
    merge_and_insert(
        source_df=premios_with_relationships,
        target_table=EtlDbConfig.SorTable.PREMIOS,
        target_df=premios_sor,
        key_columns=['ID_PREMIO'],
        db_con=schema_con.SOR
    )
