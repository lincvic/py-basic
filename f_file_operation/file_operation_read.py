# 读取整个文件
def read_file_all():
    file = open("data.txt", "r")
    print(file.read())
    file.close()


# 逐行读取文件
def read_file_by_single_line():
    file = open("data.txt", "r")
    line = file.readline()
    line_2 = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
    file.close()


# 将所有行读取到list中
def read_file_by_multi_line():
    file = open("data.txt", "r")

    for item in file.readlines():
        print(item.strip())

    file.close()


# 使用with语句
def read_file_by_multi_line_safe():
    with open("data.txt", "r") as f:
        for item in f.readlines():
            print(item.strip())


if __name__ == '__main__':
    read_file_by_multi_line_safe()
