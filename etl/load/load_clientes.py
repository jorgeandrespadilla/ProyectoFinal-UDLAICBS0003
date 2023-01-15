from config import EtlDbConfig
from util.sql_helpers import Relationship, SchemaConnection, map_relationships, merge_and_insert, read_table

table_columns = [
    'ID_CLIENTE',
    'ID_PROVINCIA',
    'NOMBRE_CLIENTE',
    'TIPO_CLIENTE',
]


def load_clientes(schema_con: SchemaConnection, etl_process_id: int) -> None:
    clientes_tra = read_table(
        table_name=EtlDbConfig.TransformTable.CLIENTES,
        columns=table_columns,
        con=schema_con.STG,
        with_process_id=etl_process_id
    )
    clientes_sor = read_table(
        table_name=EtlDbConfig.SorTable.CLIENTES,
        columns=['ID', *table_columns],
        con=schema_con.SOR
    )
    clientes_with_relationships = map_relationships(
        df=clientes_tra,
        con=schema_con.SOR,
        relationships=[
            Relationship(
                destination_column='ID_PROVINCIA', source_table=EtlDbConfig.SorTable.PROVINCIAS,
                source_column='ID_PROVINCIA',
            ),
        ]
    )
    merge_and_insert(
        source_df=clientes_with_relationships,
        target_table=EtlDbConfig.SorTable.CLIENTES,
        target_df=clientes_sor,
        key_columns=['ID_CLIENTE'],
        db_con=schema_con.SOR
    )
