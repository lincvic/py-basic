# 函数的基本结构
def func_example(name: str) -> str:
    print(name)
    return name.upper()


# 关键字参数
def keywords_param(name: str, age: int):
    print("The name is {}, and the age is {}".format(name, age))


# 默认参数
def default_param(name: str, age: int = 25):
    print("The name is {}, and the age is {}".format(name, age))


# 不定长参数1， *代表多个参数以Tuple形式传入
def unlimited_param_tuple(name: str, *args):
    print("The name is {}, and the age is {}".format(name, args))


# 不定长参数2, **代表多个参数以Dict形式传入
def unlimited_param(**kwargs):
    print("The name is {}, and the age is {}".format(kwargs["name"], kwargs["age"]))


# 返回值
def function_return_example(num_a: int, num_b: int) -> int:
    return num_a+num_b

if __name__ == '__main__':
    function_return_example("3", "3")
