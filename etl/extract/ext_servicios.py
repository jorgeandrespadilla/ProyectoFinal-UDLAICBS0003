from config import EtlDbConfig, SourceDbConfig
from util.sql_helpers import SchemaConnection, read_table

# source_col_name: db_col_name
columns_map = {
    'ID_SERVICIO': 'id_servicio',
    'DESCRIPCION_SERVICIO': 'descripcion_servicio',
    'VALOR_SERVICIO': 'valor_servicio',
    'TIEMPO_SUBSCRIPCION': 'tiempo_subscripcion',
    'BENEFICIOS_SERVICIO': 'beneficios_servicio',
}
source_columns = list(columns_map.keys())


def extract_servicios(schema_con: SchemaConnection):
    # Read source table
    servicios_source = read_table(
        table_name=SourceDbConfig.Table.SERVICIOS,
        columns=source_columns,
        con=schema_con.SOURCE,
    ).astype(str)
    if not servicios_source.empty:
        # Assign database column names
        servicios_df = servicios_source.rename(columns=columns_map)
        # Write to database
        schema_con.STG.connect().execute(f'TRUNCATE TABLE {EtlDbConfig.ExtractTable.SERVICIOS}')
        servicios_df.to_sql(EtlDbConfig.ExtractTable.SERVICIOS, schema_con.STG, if_exists='append', index=False)
