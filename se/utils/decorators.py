
from time import perf_counter as pc
from functools import wraps
# import inspect


def time_track(func):
    @wraps(func)
    def inner(*args):
        t0 = pc()
        func(*args)
        time = pc() - t0
        print(f'{func} levou %.20f s' % time)
        return time
    return inner
