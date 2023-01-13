from config import EtlDbConfig, SourceDbConfig
from util.sql_helpers import SchemaConnection, read_table

# source_col_name: db_col_name
columns_map = {
    'ID_CLIENTE': 'id_cliente',
    'ID_PROVINCIA': 'id_provincia',
    'NOMBRE_CLIENTE': 'nombre_cliente',
    'TIPO_CLIENTE': 'tipo_cliente',
}
source_columns = list(columns_map.keys())


def extract_clientes(schema_con: SchemaConnection):
    # Read source table
    clientes_source = read_table(
        table_name=SourceDbConfig.Table.CLIENTES,
        columns=source_columns,
        con=schema_con.SOURCE,
    ).astype(str)
    if not clientes_source.empty:
        # Assign database column names
        clientes_df = clientes_source.rename(columns=columns_map)
        # Write to database
        schema_con.STG.connect().execute(f'TRUNCATE TABLE {EtlDbConfig.ExtractTable.CLIENTES}')
        clientes_df.to_sql(EtlDbConfig.ExtractTable.CLIENTES, schema_con.STG, if_exists='append', index=False)
