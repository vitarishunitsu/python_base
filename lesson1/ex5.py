while True:
    proceeds = float(input('Введите вырученную сумму: '))
    if proceeds >= 0:
        break
    else:
        print('Выручка не может быть отрицательным числом. Пожалуйста, попробуйте снова!')


while True:
    expenses = float(input('Введите сумму издержек: '))
    if expenses >= 0:
        break
    else:
        print('Сумма издержек не может быть отрицательным числом. Пожалуйста, попробуйте снова!')


profit = proceeds - expenses

if profit > 0:
    print(f'Неплохо, прибыль составляет: {profit}')
    print(f'Рентабельность составляет: {profit / proceeds}')
    while True:
        employers = float(input('Введите количество сотрудников: '))
        if employers > 0 and (employers - int(employers)) == 0:
            break
        elif employers == 0:
            print('А как же генеральный директор?')
        else:
            print('Количество сотрудников не может быть отрицательным, или дробным числом!')

    print(f'Прибыль на сотрудника составляет: {profit / employers}')

elif profit == 0:
    print(f'Сработали в 0')

else:
    print(f'Сработали в минус. Перерасход: {profit}')