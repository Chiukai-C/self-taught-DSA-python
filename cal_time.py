# calculate the running time of a function

import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("The running time of %s is %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper

