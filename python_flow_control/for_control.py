#  for循环

# 基础循环
def basic_for_list():
    demo_list = [1, 2, 3]
    for item in demo_list:
        print(item, end=",")

    print("\n")
    demo_string = "String"
    for char in demo_string:
        print(char, end=" ")


# 遍历范围
def for_range_example():
    for i in range(1, 11):
        print(i, end=" ")


# 遍历嵌套
def multiply_list():
    for i in range(1, 10):
        for j in range(1, 10):
            print("{} x {} = {}".format(i, j, i * j))


def multiply_list_with_structure():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{} x {} = {}".format(j, i, i * j), end="\t")
        print()


# 循环条件控制
def break_else_example():
    students = {"A": 85, "B": 70, "C": 58, "D": 92, "E": 78}
    for name, score in students.items():
        if score < 60:
            print("{}的分数为{}，不及格，结束评分".format(name, score))
            break
        # format的另一种方式
        print(f"{name}的分数为{score}")
    else:
        print("所有学生评分结束")


if __name__ == '__main__':
    break_else_example()
