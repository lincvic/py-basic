

# 推导式基础
def basic_comp():
    list_demo = [1, 2, 3, 4, 5]
    new_list = [item for item in list_demo if item < 4]
    print(new_list)


def basic_comp_with_else_statement():
    list_demo = ["python", "go", "java"]
    new_list = [item.upper() if item.startswith("p") else item for item in list_demo]
    print(new_list)


if __name__ == '__main__':
    basic_comp_with_else_statement()
