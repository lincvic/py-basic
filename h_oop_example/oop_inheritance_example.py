class Animal:
    species = "Animal"

    def __init__(self, weight: int):
        self.weight = weight

    @staticmethod
    def speak():
        print("I'm an animal.")


# Dog会继承Animal的方法与属性
class Dog(Animal):

    @staticmethod
    def bark():
        print("Woof!")

    # 重写父类方法
    # def speak(self):
    #     print("I'm a dog !")


if __name__ == '__main__':
    my_dog = Dog(1)
    my_dog.speak()
    my_dog.bark()
    print(my_dog.weight)
