from sys import argv


def income(hours, rate, bonus):
    return int(hours) * float(rate) + float(bonus)


if __name__ == '__main__':
    try:
        print(income(argv[1], argv[2], argv[3]))
    except IndexError:
       print('Указаны не все данные')