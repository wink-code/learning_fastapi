import os
from sqlmodel import create_engine, Session, select
from dotenv import load_dotenv

from .model import  YL, SQLModel

load_dotenv()

sql_server_url = (
    f"mssql+pyodbc://{os.getenv('SQLSERVER_USER')}:"
    f"{os.getenv('SQLSERVER_PASSWORD')}@"
    f"{os.getenv('SQLSERVER_HOST')}:{os.getenv('SQLSERVER_PORT')}/"
    f"{os.getenv('SQLSERVER_DB')}?"
    f"driver={os.getenv('SQLSERVER_DRIVER').replace(' ','+')}&"
    "TrustServerCertificate=yes&"
    "Encrypt=no"
)
# print(sql_server_url)
engine = create_engine(
    sql_server_url,
    echo=True,
    pool_pre_ping=True
)

# 创建数据表(若表不存在则创建)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# CRUD操作
# 新增数据
from datetime import datetime
def create_data(yl_200: float, yl_80: float, d_time: datetime):
    with Session(engine) as session:
        data = YL(
            yl_200=yl_200,
            yl_80=yl_80,
            d_time=d_time,
        )
        session.add(data)
        session.commit()
        session.refresh(data)
        print(f"新增数据成功:溢流200目:{data.yl_200}, 溢流80目:{data.yl_80}")
        return data

# 查询所有数据
def get_all_data():
    with Session(engine) as session:
        # 构建查询语句: 查询data表所有数据
        statement = select(YL)
        datas = session.exec(statement).all()
        print(f"查询到{len(datas)}个数据")
        for data in datas[:10]:
            print("time: ", data.d_time, ",yl_200: ", data.yl_200, ",yl_80: ", data.yl_80)
    return datas

# 删除表
def drop_table():
    YL.__table__.drop(engine)
    print('删除表成功')
