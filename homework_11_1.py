# 1. Создать пять классов описывающие реальные объекты. Каждый класс должен содержать минимум
# три приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода.
class Cow:
    def __init__(self, __age, __height, __name):
        self.__age = __age
        self.__height = __height
        self.__name = __name

    def move(self):
        pass

    def eat(self):
        pass


class Cat:
    def __init__(self, __streight, __height, __name):
        self.__streight = __streight
        self.__height = __height
        self.__name = __name

    def sleep(self):
        pass

    def run(self):
        pass


class Refrigerator:
    def __init__(self, __capacity, __height, __brand):
        self.__capacity = __capacity
        self.__height = __height
        self.__brand = __brand

    def fridge(self):
        pass

    def power_on(self):
        pass


class TvSet:
    def __init__(self, __diagonal, __color, __brand_name):
        self.__diagonal = __diagonal
        self.__color = __color
        self.__brand_name = __brand_name

    def show(self):
        pass

    def switch_to(self):
        pass


class Watch:
    def __init__(self, __gender, __size, __brand_name):
        self.__gender = __gender
        self.__size = __size
        self.__brand_name = __brand_name

    def show_time(self):
        pass

    def wind_up(self):
        pass
