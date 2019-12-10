err_str = 'Номер месяца должен быть целым числом в диапазоне от 1 до 12'
seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10 , 11]}

while True:
    try:
        usr_month = float(input('Введите номер месяца (1-12): '))
        if 1 <= usr_month <= 12 and (usr_month - int(usr_month)) == 0:
            usr_month = int(usr_month)
            break
        else:
            print(err_str)
    except ValueError:
        print(err_str)


for key in seasons:
    if usr_month in seasons[key]:
        print(f'Месяц {usr_month} относится к {key}')
        break
