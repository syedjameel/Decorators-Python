import time
import io
import contextlib
import inspect


def decorator_2(fn):
    """This is a Decorator function 2 which executes the function "fn"
    and then writes down the functions name, type, sign,
    Args, Doc, Source, Output
    :param fn: It is a Function which is decorated with this decorator_2 function
    """
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        start_time = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as var:
            output = fn(*args, **kwargs)
        counter += 1    # Counter for counting the number of times the function was called
        print(f"{fn.__name__} call {counter} executed in {(time.time() - start_time)} sec")
        print(f"Name:\t{fn.__name__}")
        print(f"Type:\t{type(fn)}")
        print(f"Sign:\t{inspect.signature(fn)}")
        print(f"Args:\tpositional {args}\n\t\tkey=worded {kwargs}") # can also use inspect.getdoc(fn)
        print(f"Doc:\t{fn.__doc__}")
        print(f"Source:\t", end="")
        i=0
        for line in inspect.getsourcelines(fn)[0]:
            print((" " if i == 0 else '\t\t') + line, end="")
            i = 1
        print(f"Output:\t", end="")
        print(f"{output}\n")
        return output
    return wrapper
