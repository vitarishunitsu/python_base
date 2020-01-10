from abc import ABC, abstractmethod


class Dress:
    def __init__(self, name):
        self.name = name
        self.__dress_type = 'Dress'


# Декоратор исключает из наследования декорируемую функцию
@property
@abstractmethod
def cloth(self):
    return 0


# Можно считывать, нельзя записывать
@property
@abstractmethod
def dress_type(self):
    return self.__dress_type


class Costume(Dress):
    def __init__(self, name):
        super(Costume, self).__init__(name)
        self.__dress_type = 'Costume'
        self.H = 0

    @property
    def cloth(self):
        return float(self.H * 2 + 0.3)

    @property
    def dress_type(self):
        return self.__dress_type


class Coat(Dress):
    def __init__(self, name):
        super(Coat, self).__init__(name)
        self.__dress_type = 'Coat'
        self.V = 0

    @property
    def cloth(self):
        return float(self.V / 6.5 + 0.5)

    @property
    def dress_type(self):
        return self.__dress_type


my_coat = Coat('Some coat')
my_coat.V = 54
print(my_coat.name)
print(my_coat.dress_type)
print(my_coat.cloth)
print()
my_costume = Costume('Some costume')
my_costume.H = 1.88
print(my_costume.name)
print(my_costume.dress_type)
print(my_costume.cloth)
