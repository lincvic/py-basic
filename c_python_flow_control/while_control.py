# while 使用方法
def while_sample():
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1


# 寻找list中的第一个偶数
def even_finder_first():
    numbers = [1, 3, 5, 6, 7, 9, 10]
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print("Even number found, {}".format(numbers[index]))
            break
        index += 1


def even_finder_all():
    numbers = [1, 3, 5, 6, 7, 9, 10]
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print("Even number found, {}".format(numbers[index]))
        index += 1
    else:
        print("All even numbers has been found")


if __name__ == "__main__":
    even_finder_all()
