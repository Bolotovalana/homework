# 2. Написать свой итератор(реализовать у него и метод next и __iter__),
# чтобы при обходе циклом он отдавал только элементы на четных индексах, возведенные в квадрат.

class MyIter:
    def __init__(self, max):
        self.max = max
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.max:
            if self.start % 2 == 0 and self.start != 0:
                res = self.start ** 2
                self.start += 1
                return res
            self.start += 1
        else:
            raise StopIteration


s_iter2 = MyIter(10)
for i in s_iter2:
    print(i)