# 1. Написатьдекоратор,которыйбудетвыводитьвремявыполнения функции, а также аргументы, с которыми она была вызвана.
def simple_decore(fn):
    def wrapper(arg):
        import time
        start_time = time.time()
        fn(arg)
        end_time = (time.time()) - start_time
        print("{i} - {param}".format(i=end_time, param=arg))

    return wrapper


@simple_decore
def greetings(greet):
    print(greet)


greetings("Hi")

