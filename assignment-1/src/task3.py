import time
import contextlib
import inspect
import atexit


def exit_hd():
    """To print the ranks of each program just before the program is finished"""
    sorted_ranks = sorted(ranks.items(), key=lambda x: x[1])
    if len(sorted_ranks) >0:
        print("\nPROGRAM\t|\tRANK\t|\tTIME ELAPSED", end="")
        for i in range(len(sorted_ranks)):
            print("\n", sorted_ranks[i][0], "\t\t", i + 1, "\t\t", sorted_ranks[i][1], "sec", end="")
atexit.register(exit_hd)


ranks = dict()  # To store the execution time, and name of the functions
sorted_ranks = []
class decorator_3:
    """This is a decorator class which will show the execution time of the
    functions which are decorated by this class and rank the functions
    based on the execution time and also dumps the output of each function
    to task3_logs.txt file"""
    def __init__(self, fn):
        self.counter = 0
        self.fn = fn

    def __call__(self, *args, **kwargs):
        with open('task3_logs.txt', 'a') as fd:
            with contextlib.redirect_stdout(fd):
                start_time = time.time()
                ret = self.fn(*args, **kwargs)
                total_time = (time.time() - start_time)
                self.counter += 1
                print(f"{self.fn.__name__} call {self.counter} executed in {total_time} sec")
                ranks[self.fn.__name__] = total_time
                print(f"Name:\t{self.fn.__name__}")
                print(f"Type:\t{type(self.fn)}")
                print(f"Sign:\t{inspect.signature(self.fn)}")
                print(f"Args:\tpositional {args}\n\t\tkey=worded {kwargs}")
                print(f"Doc:\t{self.fn.__doc__}")   # can also use inspect.getdoc(self.fn)
                print(f"Source:\t", end="")
                i = 0
                for line in inspect.getsourcelines(self.fn)[0]:
                    print((" " if i == 0 else '\t\t') + line, end="")
                    i = 1
                print(f"Output:\t", end="")
                print(f"{ret}\n")
                return ret
        return ret