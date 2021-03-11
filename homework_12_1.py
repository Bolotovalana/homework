# 1. Написать свой класс MyOpen, объекты которого должны поддерживать протокол контекстного менеджера.
# Он должен работать аналогично with open(‘file.txt’, ‘w+’) as f.
# Т.е вы можете применять его следующим образом:
# with MyOpen(file.txt’, ‘w+’) as f:
class MyOpen:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


my = MyOpen
with my('file.txt', 'w+') as f:
    f.write("Hello1")