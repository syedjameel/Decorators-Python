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
            fn(*args, **kwargs)
        counter += 1    # Counter for counting the number of times the function was called
        print(f"{fn.__name__} call {counter} executed in {(time.time() - start_time)} sec")
        print(f"Name:\t{fn.__name__}")
        print(f"Type:\t{type(fn)}")
        print(f"Sign:\t{inspect.signature(fn)}")
        print(f"Args:\tpositional {args}\n\t\tkey=worded {kwargs}")
        print(f"Doc:\t{fn.__doc__}")
        print(f"Source:\t{inspect.getsource(fn)}")
        start = 'print("'           # Starting string from the source code string
        end = '")'                  # Ending string from the source code string
        s = str(inspect.getsource(fn))
        s = (s.split(start))[1].split(end)[0]
        final_output = s.replace('\\n', '\n').replace('\\t', '\t')
        print(f"Output:\t", end="")
        print(final_output)
    return wrapper
