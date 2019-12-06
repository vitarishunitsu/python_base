while True:
    current_val = float(input('Введите текущий результат спортсмена в километрах: '))
    if current_val >= 0:
        break
    else:
        print('Если спортсмен бежит в другую сторону - это тоже результат.'
              'Введите значение без знака минус')

while True:
    target_val = float(input('Введите желаемый результат спортсмена в километрах: '))
    if target_val > 0 and target_val > current_val:
        break
    else:
        print('Желаемый результат должен быть больше нуля и больше начального результата')


day = 1

while current_val <= target_val:
    print(f"{day}'й день: {current_val:.2f} километров")
    current_val *= 1.1
    day += 1

print(f"{day}'й день: {current_val:.2f} километров")
print(f"Ответ: На {day}'й день спортсмен достигнет результата не менее {int(current_val)} километров")

