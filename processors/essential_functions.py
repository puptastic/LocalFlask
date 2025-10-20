from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        time_end = time()
        print(f"Finished {f.__name__} in {time_end - time_start} seconds.")
        return result
    return wrap