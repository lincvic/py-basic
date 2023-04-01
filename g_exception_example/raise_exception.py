# 自定义异常
class MyError(Exception):
    pass


# 抛出异常
def divide(a, b):
    if b == 0:
        raise MyError("The divisor cannot be zero")
    return a / b


if __name__ == '__main__':
    divide(1, 0)
