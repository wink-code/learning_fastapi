from datetime import datetime, timezone
from .model import YL_200
from .db import create_db_and_tables, engine
from .db import create_data, get_all_data, drop_table

create_db_and_tables()

def try_write_data():
    try:
        create_data(value=60.1, d_time=datetime.now(timezone.utc))
        print('write successful!')
    except:
        print('ops, writing failed.')

def try_query_data():
    get_all_data()
