def div(a, b):
    return a / b


while True:
    try:
        x = float(input('Введите делимое число: '))
        while True:
            try:
                y = float(input('Введите делитель числа: '))
                z = div(x, y)
#                z = (lambda a, b: a / b)(x, y) #Хы
                print(f'{x} / {y} = {z:0.4f}')
                break
            except ValueError:
                print('Делитель должен быть числом')
            except ZeroDivisionError: # Через исключение, потому что ситуация деления на ноль, а не ввода нуля =)
                print('Деление на 0')
    except ValueError:
        print('Делимое должно быть числом')