# 2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5),
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.

def slow_down(_speed):
    if _speed != 0:
        return _speed - 5
    else:
        print("Car is already stopped")


class Car:
    def __init__(self, __make, __model, __year, __speed=0):
        self.__make = __make
        self.__model = __model
        self.__year = __year
        self.__speed = __speed

    def accelerate(self, __speed):
        return __speed + 5

    def stopping(self, __speed):
        while __speed > 0:
            slow_down()
            Car.show_speed(__speed)

    def show_speed(self, __speed):
        print(__speed)

    def u_turn(self, __speed):
        while __speed > 15:
            slow_down()
            Car.show_speed()
        while __speed < 45:
            Car.accelerate(__speed)
            Car.show_speed()
