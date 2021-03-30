# 2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5),
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.
# 4. Просмотреть ваше задание, где вы реализовывали класс Car и подумать,
# где стоит добавить выкидывание(raise) исключений(например, когда скорость может стать меньше 0).
# В месте, где вы работаете с этим классом , добавьте обработку этих исключений, используя конструкцию try.
class Car:
    def __init__(self, _make, _model, _year):
        self._make = _make
        self._model = _model
        self._year = _year
        self._speed = 0

    def accelerate(self):
        self._speed = self._speed + 5

    def slow_down(self):
        if self._speed != 0:
            if (self._speed - 5) < 0:
                raise Speed_lower_zero_Exception
            else:
                self._speed = self._speed - 5
        elif self._speed == 0:
            print("Car is stopped")
        else:
            self._speed = 0
            print("Car is already stopped")

    def stop(self):
        while self._speed > 0:
            self.slow_down()
            self.show_speed()
        else:
            self.slow_down()

    def show_speed(self):
        print(self._speed)

    def u_turn(self):
        while self._speed > 15:
            self.slow_down()
            self.show_speed()
        while self._speed < 45:
            self.accelerate()
            self.show_speed()


class Speed_lower_zero_Exception(BaseException):
    pass
