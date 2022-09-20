import time
import contextlib
import inspect
import atexit
import traceback
import datetime
import io

def exit_hd():
    """To print the ranks of each program just before the program is finished"""
    sorted_ranks = sorted(ranks.items(), key=lambda x: x[1])
    if len(sorted_ranks) > 0:
        print("\nPROGRAM\t|\tRANK\t|\tTIME ELAPSED", end="")
        for i in range(len(sorted_ranks)):
            print("\n", sorted_ranks[i][0], "\t\t", i + 1, "\t\t", sorted_ranks[i][1], "sec", end="")
atexit.register(exit_hd)


ranks = dict()  # To store the execution time, and name of the functions
sorted_ranks = []
class decorator_4:
    """This is a decorator class which will show the execution time of the
    functions which are decorated by this class and rank the functions
    based on the execution time and also dumps the output of each function
    to task3_logs.txt file"""
    def __init__(self, fn):
        self.counter = 0
        self.fn = fn

    def __call__(self, *args, **kwargs):
        try:
            error_file = open("task4_error_logs.txt", "a")
            with open('task4_logs.txt', 'a') as fd:
                with contextlib.redirect_stdout(fd):
                    start_time = time.time()
                    self.fn(*args, **kwargs)
                    total_time = (time.time() - start_time)
                    self.counter += 1
                    print(f"{self.fn.__name__} call {self.counter} executed in {total_time} sec")
                    ranks[self.fn.__name__] = total_time
                    print(f"Name:\t{self.fn.__name__}")
                    print(f"Type:\t{type(self.fn)}")
                    print(f"Sign:\t{inspect.signature(self.fn)}")
                    print(f"Args:\tpositional {args}\n\t\tkey=worded {kwargs}")
                    print(f"Doc:\t{self.fn.__doc__}")
                    print(f"Source:\t", end="")
                    i = 0
                    for line in inspect.getsourcelines(self.fn)[0]:
                        print((" " if i == 0 else '\t\t') + line, end="")
                        i = 1
                    print(f"Output:\t", end="")
                    print(f"{self.fn(*args, **kwargs)}\n")
            fd.close()
        except Exception:
            fd.close()
            error_file.writelines(f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n")
            error_file.close()
        return None

def decorator_4_function(fn):
    """This is a Decorator function 4 using a function which executes the function "fn"
        and then writes down the functions name, type, sign,
        Args, Doc, Source, Output
        :param fn: It is a Function which is decorated with this decorator_2 function
        """
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        try:
            error_file = open("task4_error_logs.txt", "a")
            with open('task4_logs.txt', 'a') as fd:
                with contextlib.redirect_stdout(fd):
                    start_time = time.time()
                    fn(*args, **kwargs)
                    total_time = (time.time() - start_time)
                    counter += 1
                    print(f"{fn.__name__} call {counter} executed in {total_time} sec")
                    ranks[fn.__name__] = total_time
                    print(f"Name:\t{fn.__name__}")
                    print(f"Type:\t{type(fn)}")
                    print(f"Sign:\t{inspect.signature(fn)}")
                    print(f"Args:\tpositional {args}\n\t\tkey=worded {kwargs}")
                    print(f"Doc:\t{fn.__doc__}")    # can also use inspect.getdoc(self.fn)
                    print(f"Source:\t", end="")
                    i = 0
                    for line in inspect.getsourcelines(fn)[0]:
                        print((" " if i == 0 else '\t\t') + line, end="")
                        i = 1
                    print(f"Output:\t", end="")
                    print(f"{fn(*args, **kwargs)}\n")
            fd.close()
        except Exception:
            fd.close()
            error_file.writelines(f"{datetime.datetime.now()}\n{traceback.format_exc()}\n\n")
            error_file.close()
    return wrapper