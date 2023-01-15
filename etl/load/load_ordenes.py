from config import EtlDbConfig
from util.sql_helpers import Relationship, SchemaConnection, map_relationships, merge_and_insert, read_table

table_columns = [
    'ID_ORDEN',
    'ID_CLIENTE',
    'ID_SERVICIO',
    'ID_PROVINCIA',
    'ID_MOTIVO',
    'ESTADO_ORDEN',
    'FECHA_ADQUISICION',
]


def load_ordenes(schema_con: SchemaConnection, etl_process_id: int) -> None:
    ordenes_tra = read_table(
        table_name=EtlDbConfig.TransformTable.ORDENES,
        columns=table_columns,
        con=schema_con.STG,
        with_process_id=etl_process_id
    )
    ordenes_sor = read_table(
        table_name=EtlDbConfig.SorTable.ORDENES,
        columns=['ID', *table_columns],
        con=schema_con.SOR
    )
    ordenes_with_relationships = map_relationships(
        df=ordenes_tra,
        con=schema_con.SOR,
        relationships=[
            Relationship(
                destination_column='ID_CLIENTE', source_table=EtlDbConfig.SorTable.CLIENTES,
                source_column='ID_CLIENTE',
            ),
            Relationship(
                destination_column='ID_SERVICIO', source_table=EtlDbConfig.SorTable.SERVICIOS,
                source_column='ID_SERVICIO',
            ),
            Relationship(
                destination_column='ID_PROVINCIA', source_table=EtlDbConfig.SorTable.PROVINCIAS,
                source_column='ID_PROVINCIA',
            ),
            Relationship(
                destination_column='ID_MOTIVO', source_table=EtlDbConfig.SorTable.MOTIVOS,
                source_column='ID_MOTIVO',
            ),
        ]
    )
    merge_and_insert(
        source_df=ordenes_with_relationships,
        target_table=EtlDbConfig.SorTable.ORDENES,
        target_df=ordenes_sor,
        key_columns=['ID_ORDEN'],
        db_con=schema_con.SOR
    )
