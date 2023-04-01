import datetime
import json


# 获取当前时间
def current_time():
    print(datetime.datetime.now())


# 计算日期差值
def delta_time():
    date_1 = datetime.datetime(2023, 1, 1, 12, 0, 0)
    date_2 = datetime.datetime(2023, 1, 2, 18, 0, 0)
    delta = date_2 - date_1
    print(delta.total_seconds())


# 将json string读取为Dict
def load_json():
    json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
    data = json.loads(json_string)
    print(data)
    print(data["name"])


if __name__ == '__main__':
    delta_time()
