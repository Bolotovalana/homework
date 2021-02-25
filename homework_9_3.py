def decor(func):
    def wrapper(param):
        param_new = [a for a in param if a % 2]
        return func(param_new)

    return wrapper


@decor
def getList(list):
    print(list)


getList([1, 2, 3, 4, 5, 6, 7, 8, ])