from math import factorial
from functools import reduce
from ex5 import mult


def fibo_gen():
    for i in range(1, 16):
        # yield factorial(i)
        yield reduce(mult, [_ for _ in range(1, i + 1)])


for el in fibo_gen():
    print(el)
