# Number
def number_example():
    number_1 = 1
    number_2 = 1.5
    number_3 = number_2 - number_1

    print(type(number_1))
    print(type(number_2))
    print(type(number_3))


# Number计算
def number_calc():
    # 除法
    number_div_1 = 2 / 4
    # 整除
    number_div_2 = 2 // 4

    print(number_div_1)
    print(number_div_2)

    # 取余
    number_mod_1 = 16 % 3
    print(number_mod_1)

    # n次方
    number_square = 2
    print(number_square ** 2)


# String
def string_example():
    str = 'STRING'

    # []索引左闭右开
    print(str[1::2])
    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(str[0])  # 输出字符串第一个字符
    print(str[-1])  # 输出字符串最后一个字符
    print(str[2:5])  # 输出从第三个开始到第五个的字符
    print(str[2:])  # 输出从第三个开始的后的所有字符
    print(str * 2)  # 输出字符串两次
    print(str + "-ANOTHERSTRING")  # 连接字符串


def bool_example():
    # 直接比较变量
    print(2 > 3)

    # 逻辑运算符
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not a)


def list_example():
    list_demo = [1, "string", True, 2, 2]
    # 截取List可以限定步长
    print(list_demo[1::2])

    # list 可以被更新
    # list 单个元素更新
    list_demo[1] = "new string"
    print(list_demo)

    # list 新增内容
    list_demo.append("New content")
    print(list_demo)

    # list 删除单个元素
    del list_demo[1]
    print(list_demo)

    # list移除第一个匹配的值
    list_demo.remove(2)
    print(list_demo)

    # list移除多个匹配值
    list_demo = [item for item in list_demo if item not in ("New Content", 2)]
    print(list_demo)

    # list 倒序
    list_demo.reverse()
    print(list_demo)


def reverseString(original: str):
    original_list = list(original)
    print(original_list)
    # 步长为-1代表倒序
    new_list = original_list[-1::-1]
    new_list = ''.join(new_list)
    print(new_list)


def dict_example():
    dict_demo = {
        "firstname": "Layne",
        "lastname": "Wang"
    }

    # 通过key输出value
    print(dict_demo["firstname"])

    # 检查Key是否存在
    if "Layne" in dict_demo:
        print("OK")

    # 获取所有Key
    print(list(dict_demo.keys()))

    # 获取所有Value
    print(list(dict_demo.values()))

    # 遍历获取key， value
    for k, v in dict_demo.items():
        print("{}, {}".format(k, v))


def tuple_example():
    new_tuple = (1, 2, 3, 4)
    print(new_tuple)


def set_example():
    new_set = {1, 2, 3, 4, 4, "5"}
    new_set_2 = {3, 4, 5, "6"}
    print(type(new_set))

    # Set中元素不会重复
    print(new_set)

    # 集合运算
    # ∪
    print(new_set | new_set_2)

    # ∩
    print(new_set & new_set_2)

    # 不同时包含在两个集合中的元素
    print(new_set ^ new_set_2)
    print((new_set - (new_set & new_set_2)) | (new_set_2 - (new_set & new_set_2)))


if __name__ == '__main__':
    set_example()
