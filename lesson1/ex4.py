while True:
    input_number = input('Введите целое положительное число: ')

    float_value = float(input_number)
    int_value = int(float_value)

    if float_value >= 0 and (float_value - int_value) == 0:
        break
    else:
        print('Число должно быть больше нуля и без дробной части')


i = 0
max_num = 0

while i < len(input_number):
    if max_num < int(input_number[i]):
        max_num = int(input_number[i])
    i += 1

print(f'Наибольшая цифра из числа: {max_num}')