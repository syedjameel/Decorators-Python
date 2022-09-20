import io
import time
import contextlib


def decorator_1(fn):
    """This is the Decorator function 1 which is used to decorated other functions
    This function has a wrapper function which counts the function calls
    and counts time for execution of that particular function
    :param fn: It is a function which is decorated by this decorator_1 function"""
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        with contextlib.redirect_stdout(io.StringIO()) as var:
            start_time = time.time()
            fn(*args, **kwargs)
        counter += 1 # Counter
        print(f"{fn.__name__} call {counter} executed in {(time.time() - start_time)} sec")
    return wrapper

