import time
import sys
sys.path.insert(0, r'D:\workspace\learn-fastapi\练习')
import write_into_sql_server.main as main
import pandas as pd

df = pd.read_excel(r'C:\Users\precision3630\Desktop\数据\离线测试\旋流器数据\2025-7-8.xlsx', parse_dates=[0], usecols="A,F,K")
# print(df)

def try_create_data():
    for _,(time, yl_200, yl_80) in df.iterrows():
        # print(_, time, value)
        main.create_data(yl_200=yl_200, yl_80=yl_80, d_time=time)


def test_try_create_data():
    start_time = time.perf_counter()
    result = try_create_data()
    total = time.perf_counter() - start_time
    print()
    print(f'共插入{result}条数据, 操作耗时:{total :.3f}s')
    print()


# test_try_create_data()

def way1():
    dict_list = [item.model_dump(exclude_unset=True) for item in datas]
    print(dict_list)

def way2():
    datas_df = pd.DataFrame(data = datas)
    print(datas_df)
    
def way3():
    from collections import namedtuple
    YL_200_Tuple = namedtuple("YL_200", "id time value")
    tuple_list = [
        YL_200_Tuple(
            id = item.id,
            time = item.d_time,
            value = item.value
        ) for item in datas
    ]
    print(tuple_list)

# way3()
# print(datas)

# from pprint import pprint


def draw():
    datas = main.try_query_data()
    from operator import attrgetter
    get_time = attrgetter('d_time')
    # pprint(list(map(get_time, datas)))
    time_list = list(map(attrgetter('d_time'), datas))
    yl_200_list = list(map(attrgetter('yl_200'), datas))
    yl_80_list = list(map(attrgetter('yl_80'), datas))
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(time_list, yl_200_list, label="溢流200目粒度")
    plt.plot(time_list, yl_80_list, label="溢流80目粒度")
    plt.legend()
    plt.show()


# print(type(datas[0]))
# main.drop_table()

if __name__ == '__main__':
    # try_create_data()
    draw()