

# 捕获一个异常
def catch_single_exception():
    try:
        # 需要捕获异常的代码
        num = 1/0
    except ZeroDivisionError as e:
        # 有异常出现的情况
        print("Error, {}".format(e))
    else:
        # 没有异常出现的情况
        print("No Errors")
    finally:
        # 执行必要的清理操作
        print("Process Try Except Complete")


if __name__ == '__main__':
    catch_single_exception()