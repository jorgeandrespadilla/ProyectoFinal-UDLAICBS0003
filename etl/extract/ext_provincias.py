from config import EtlDbConfig, SourceDbConfig
from util.sql_helpers import SchemaConnection, read_table

# source_col_name: db_col_name
columns_map = {
    'ID_PROVINCIA': 'id_provincia',
    'NOMBRE_PROVINCIA': 'nombre_provincia',
}
source_columns = list(columns_map.keys())


def extract_provincias(schema_con: SchemaConnection):
    # Read source table
    provincias_source = read_table(
        table_name=SourceDbConfig.Table.PROVINCIAS,
        columns=source_columns,
        con=schema_con.SOURCE,
    ).astype(str)
    if not provincias_source.empty:
        # Assign database column names
        provincias_df = provincias_source.rename(columns=columns_map)
        # Write to database
        schema_con.STG.connect().execute(f'TRUNCATE TABLE {EtlDbConfig.ExtractTable.PROVINCIAS}')
        provincias_df.to_sql(EtlDbConfig.ExtractTable.PROVINCIAS, schema_con.STG, if_exists='append', index=False)
