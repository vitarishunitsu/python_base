from random import randint


def make_list():
    for i in range(20):
        yield randint(0, 20)


def format_list(in_list):
    return [i for i in in_list if in_list.count(i) < 2]


some_list = [3, 56, 4, 21, 56, 690, 0, 1, 1, 1, 45, 76, 90, 32, 45, 31, -4, -2, 6, 13, 4, 678, 325, 499]
rand_list = [i for i in make_list()]

print(some_list)
print(format_list(some_list))
print()
print(rand_list)
print(format_list(rand_list))
