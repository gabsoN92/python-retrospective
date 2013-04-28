from collections import deque


def groupby(func, seq):
    result = {}

    for x in seq:
        result[func(x)] = [y for y in seq if func(y) == func(x)]

    return result


def zip_with(func, *iterables):
    zip_iterables = zip(*iterables)
    while True:
        yield func(*next(zip_iterables))


def composer(f, g):
    return lambda x: f(g(x))


def iterate(func):
    yield lambda x: x
    composition = func
    while True:
        yield composition
        composition = composer(func, composition)


def cache(func, cache_size):
    values = {}
    cache_order = deque()

    def func_cashed(*args):
        if args in values:
            return values[args]

        result = func(*args)

        if cache_size:
            if len(values) == cache_size:
                values.pop(cache_order.popleft())
            cache_order.append(args)
            values[args] = result

        return result
    return func_cashed

