def if_example(foo: int):
    if foo > 10:
        print("Foo is greater than 10")
    elif foo < 0:
        print("Foo is less than 0")
    elif foo == 10:
        print("Foo is equal to 10")
    else:
        print("Foo is between 0 to 10")


def if_example_2(text: str) -> bool:

    # return True if text in 'abc' else False
    if text in 'abc':
        return True
    return False


if __name__ == '__main__':
    print(if_example_2("a"))
