from datetime import datetime, timezone
from .model import YL
from .db import create_db_and_tables, engine
from .db import create_data, get_all_data, drop_table

create_db_and_tables()

def try_write_data(value, d_time):
    try:
        create_data(value=value, d_time=d_time)
        print('write successful!')
    except:
        print('ops, writing failed.')

def try_query_data():
    return get_all_data()
