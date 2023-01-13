from config import EtlDbConfig, SourceDbConfig
from util.sql_helpers import read_table, SchemaConnection

# source_col_name: db_col_name
columns_map = {
    'ID_MOTIVO': 'id_motivo',
    'DESCRIPCION_MOTIVO': 'descripcion_motivo',
}
source_columns = list(columns_map.keys())


def extract_motivos(schema_con: SchemaConnection):
    # Read source table
    motivos_source = read_table(
        table_name=SourceDbConfig.Table.MOTIVOS,
        columns=source_columns,
        con=schema_con.SOURCE,
    ).astype(str)
    if not motivos_source.empty:
        # Assign database column names
        motivos_df = motivos_source.rename(columns=columns_map)
        # Write to database
        schema_con.STG.connect().execute(f'TRUNCATE TABLE {EtlDbConfig.ExtractTable.MOTIVOS}')
        motivos_df.to_sql(EtlDbConfig.ExtractTable.MOTIVOS, schema_con.STG, if_exists='append', index=False)
