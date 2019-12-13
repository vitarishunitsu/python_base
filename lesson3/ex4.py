def expn(x, y):
    mx = x
    for _ in range(abs(y)-1): x *= mx
    return 1/x

#def expn(x, y):
#    return x**y


while True:
    try:
        a = float(input('Введите действительное положительное число (основание):  '))
        if a > 0:
            while True:
                try:
                    b = float(input('Введите целое отрицательное число (показатель): '))
                    if b < 0 and b - int(b) == 0:
                        b = int(b)
                        print(f'{a} в степени {b} = {expn(a, b):0.6f}')
                        break
                    else:
                        print('Число должно быть целым и отрицательным!')
                except ValueError:
                    print('Нельзя вводить строку!')
        else:
            print('Число должно быть действительным и положительным')
    except ValueError:
        print('Нельзя вводить строку!')
