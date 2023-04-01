import os


# 列出当前目录下所有文件
def list_all_files():
    directory = os.getcwd()
    files = os.listdir(directory)
    print(files)


# 创建新目录
def new_dic():
    os.mkdir("new_folder")


# 删除文件
def remove_file():
    os.remove("newfile.1txt")


if __name__ == '__main__':
    remove_file()

    x = "global x"

    def outer_function():
        x = "enclosing x"

        def inner_function():
            x = "local x"
            print(x)

        inner_function()


    outer_function()  # 输出: "local x"
