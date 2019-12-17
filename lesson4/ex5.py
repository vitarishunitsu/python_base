from functools import reduce


def mult(el_prev, el):
    return el_prev * el


if __name__ == '__main__':
    some_list = [i for i in range(100, 1001, 2)]
    print(some_list)
    print(reduce(mult, some_list))
