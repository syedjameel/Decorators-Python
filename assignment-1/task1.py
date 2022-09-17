import io
import time
import contextlib


def decorator_1(fn):
    counter = 0

    def wrapper():
        nonlocal counter
        start_time = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as var:
            fn()
        counter += 1 # Counter
        print(f"{fn.__name__} call {counter} executed in {(time.time() - start_time)} sec")
    return wrapper

