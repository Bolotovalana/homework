print((lambda **kwargs: {key * 2: value for key, value in zip(kwargs.keys(), kwargs.values())})(d=5, f=5))
