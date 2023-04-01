# 写入文件
def write_to_txt():
    with open("result.txt", "a") as f:
        for num in range(11, 15):
            f.write(str(num)+"\n")


if __name__ == '__main__':
    write_to_txt()