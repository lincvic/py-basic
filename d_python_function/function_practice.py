# 编写一个函数is_even，接受一个整数参数num，如果num是偶数则返回True，否则返回False
def is_even(num: int) -> bool:
    return num % 2 == 0


# 编写一个函数find_max，接受任意数量的整数参数，返回其中的最大值, 不使用max()方法
def find_max(*args: int) -> int:
    max_value = 0
    for item in args:
        if item > max_value:
            max_value = item

    return max_value


# 编写一个函数count_vowels，接受一个字符串参数text，返回text中元音字母（a, e, i, o, u）的个数
def count_vowels(text: str) -> int:
    vowels = 'aeiou'
    vowels_count = 0

    for char in text:
        if char in vowels:
            vowels_count += 1

    return vowels_count


# 编写一个函数factorial，接受一个整数参数n，返回n的阶乘
def factorial(n: int) -> int:
    return n if n == 0 or n == 1 else n * factorial(n - 1)


# 编写一个函数sum_of_squares，接受一个整数参数n，返回前n个自然数的平方和
def sum_of_squares(n: int) -> int:
    return sum([item ** 2 for item in range(n + 1)])


if __name__ == '__main__':
    print(sum_of_squares(3))
