from config import EtlDbConfig, SourceDbConfig
from util.sql_helpers import SchemaConnection, read_table

# source_col_name: db_col_name
columns_map = {
    'ID_ORDEN': 'id_orden',
    'ID_CLIENTE': 'id_cliente',
    'ID_SERVICIO': 'id_servicio',
    'ID_PROVINCIA': 'id_provincia',
    'ID_MOTIVO': 'id_motivo',
    'ESTADO_ORDEN': 'estado_orden',
    'FECHA_ADQUISICION': 'fecha_adquisicion',
}
source_columns = list(columns_map.keys())


def extract_ordenes(schema_con: SchemaConnection):
    # Read source table
    ordenes_source = read_table(
        table_name=SourceDbConfig.Table.ORDENES,
        columns=source_columns,
        con=schema_con.SOURCE,
    ).astype(str)
    if not ordenes_source.empty:
        # Assign database column names
        ordenes_df = ordenes_source.rename(columns=columns_map)
        # Write to database
        schema_con.STG.connect().execute(f'TRUNCATE TABLE {EtlDbConfig.ExtractTable.ORDENES}')
        ordenes_df.to_sql(EtlDbConfig.ExtractTable.ORDENES, schema_con.STG, if_exists='append', index=False)
