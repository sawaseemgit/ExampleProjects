from time import time


def perf(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(t2 - t1)
        return result

    return wrapper


@perf
def hello():
    for i in range(1000000):
        i * 10


hello()
