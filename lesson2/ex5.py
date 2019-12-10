usr_list = []


while True:
    try:
        usr_inp = float(input('Введите натуральное число: '))
        if 0 <= usr_inp and usr_inp - int(usr_inp) == 0:
            usr_list.append(int(usr_inp))
            usr_list.sort(reverse = True)
            print(f'Рейтинг: {usr_list}')
        else:
            print('Число должно быть натуральным.')
    except ValueError:
        print('Нужно натуральное число, а не строка.')