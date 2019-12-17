from sys import argv
from itertools import count, cycle
from random import randint

for _ in count(int(argv[1])):
    print(_)
    if _ > int(argv[1])+500:
        break

for _ in cycle([argv[i] for i in range(1, len(argv))]):
    print(_)
    if randint(15, 100) < 17:
        break
