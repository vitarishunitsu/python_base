while True:
    input_seconds = int(input('Введите время в секундах: '))
    if input_seconds >= 0:
        break
    else:
        print('Пожалуйста, введите положительное значение')

hours = input_seconds // 3600
minutes = (input_seconds - hours*3600) // 60
seconds = input_seconds % 60

print(f"{input_seconds} секунд это - {hours:02d}:{minutes:02d}:{seconds:02d}")