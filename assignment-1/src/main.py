import random
import inspect
import cmath
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4, decorator_4_function


@decorator_4
#@decorator_4_function
#@decorator_3
#@decorator_2
#@decorator_1
def func():
    """This is a random funtionc which does random stuff"""
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_4
#@decorator_4_function
#@decorator_3
#@decorator_2
#@decorator_1
def funx(n=2, m=5):
    """This is a random funtionx which does random stuff"""
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

@decorator_4
#@decorator_4_function
#@decorator_3
#@decorator_2
#@decorator_1
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    #a = 1/0  # this was deliberately added to check the error handling
    print("some\nmultiline\noutput")

@decorator_4
#@decorator_4_function
#@decorator_3
#@decorator_2
#@decorator_1
def quad(a, b, c):
    """This is a quadratic equation solver function
    For examples if a=1, b=-45 and c=324
    we get 36 and 9 as the roots
    Quadratic equation : ax^2 + bx + c
    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant or the intercept
    """
    roots = lambda a, b, c: ((-b + (cmath.sqrt((b**2) - (4*a*c)))) / (2*a), (-b -(cmath.sqrt((b**2) - (4*a*c)))) / (2*a))
    r = roots(a, b, c)
    print("\n", "The roots for", a, "x^2 + ", b, "x + ", c, " are : ", r)


@decorator_4
#@decorator_4_function
#@decorator_3
#@decorator_2
#@decorator_1
def pasc(n):
    """This is a pascals triangle printer function
    :param n: Number of rows to print from pascals triangle"""
    pascal = lambda n: [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]
    p = pascal(n)
    print("\n", "The pascals triangle ", n, " rows are : ", "\n", p)


if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()

    funh(None, bar2="")
    quad(a=1, b=-45, c=324)
    pasc(n=10)