def calc():
    while True:
        try:
            # 获取用户输入的计算式
            expression = input("请输入一个计算式：")

            # 计算结果
            result = eval(expression)
            print("计算结果为：", result)
        except SyntaxError:
            print("计算式语法错误，请重新输入。")
        except NameError:
            print("计算式包含未定义的变量，请重新输入。")
        except ZeroDivisionError:
            print("除数不能为0，请重新输入。")

        # 询问用户是否继续计算
        choice = input("是否继续计算？输入'y'继续，任意键退出：")
        if choice.lower() != 'y':
            break


if __name__ == "__main__":
    calc()