while True:
    input_d = input('Введите число: ')

    if int(input_d) >= 0:
        break
    else:
        print('Число должно быть положительным. Пожалуйста, попробуйте снова!')


d_number = int(input_d)
dd_number = int(f'{input_d}{input_d}')
ddd_number = int(f'{input_d}{input_d}{input_d}')

summary = d_number + dd_number + ddd_number

print(f'Сумма {d_number} + {dd_number} + {ddd_number} = {summary}')