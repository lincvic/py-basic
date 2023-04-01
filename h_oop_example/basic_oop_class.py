class Dog:
    # 类属性
    species = "Dog"

    def __init__(self, name: str, age: int):
        # 私有实例属性
        self.__name = name
        self.__age = age

    def bark(self):
        print("Woof, My name is {}, and I'm {} years old, belongs to {}"
              .format(self.__name, self.__age, self.species))

    def change_name(self, new_name: str):
        self.__name = new_name


if __name__ == '__main__':
    dog_1 = Dog("Doge", 1)
    dog_1.bark()

    # 强制访问私有实例属性
    print(dog_1._Dog__name)

    dog_2 = Dog("Cat", 2)
    dog_2.bark()
