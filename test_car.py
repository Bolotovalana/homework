import unittest
from car import Car, Speed_lower_zero_Exception


class test_car(unittest.TestCase):
    def setUp(self) -> None:
        self.car1 = Car("M", "s", 1998)

    def tearDown(self) -> None:
        del self.car1

    def test_accelerate(self):
        self.car1.accelerate()
        self.assertEqual(self.car1._speed, 5)

    def test_slow_down(self):
        self.car1._speed = 5
        self.car1.slow_down()
        self.assertEqual(self.car1._speed, 0)
        self.car1._speed = -1
        self.assertRaises(Speed_lower_zero_Exception, lambda: self.car1.slow_down())

    def test_stop(self):
        self.car1._speed = 15
        self.car1.stop()
        self.assertEqual(self.car1._speed, 0)

    def test_u_turn(self):
        self.car1._speed = 25
        self.car1.u_turn()
        self.assertEqual(self.car1._speed, 45)


if __name__ == '__main__':
    unittest.main()
