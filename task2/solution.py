def groupby(func, seq):
    result = {}
    
    for x in seq:
        result[func(x)] = [y for y in seq if func(y) == func(x)]
    
    return result


def zip_with(func, *iterables):
    zip_iterables = zip(*iterables)
    while True:
        yield func(*next(zip_iterables))


def iterate(func):
    yield lambda x: x
    for y in iterate(func):
        yield lambda x: func(y(x))