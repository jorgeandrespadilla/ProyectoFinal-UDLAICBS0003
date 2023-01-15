import time
import traceback
from etl.extract import extract
from etl.transform import transform
from etl.load import load
from util.sql_helpers import SchemaConnection, connection_handler, create_etl_process

@connection_handler
def main(schema_con: SchemaConnection):
    start = time.time()
    process_id = create_etl_process(schema_con.STG)
    print(f'ETL process N°{process_id}')
    print('Extracting data...')
    extract(schema_con)
    print('Transforming data...')
    transform(schema_con.STG, process_id)
    print('Loading data...')
    load(schema_con, process_id)
    end = time.time()
    print(f'ETL process finished in {end - start:.4f} seconds')

if __name__ == "__main__":
    try:
        main()
    except:
        print("An error occurred while running the ETL process:")
        traceback.print_exc()
