usr_list = []

print('Здравствуйте! Вводите данные построчно, чтобы составить список строк. \n'
      'Для завершения ввода напечатайте "end"')

while True:
    usr_input = input(f'Строка данных # {len(usr_list) + 1}: ')
    if usr_input != 'end':
        usr_list.append(usr_input)
    else:
        break


print(f'Ваш список строк: {usr_list} cостоит из {len(usr_list)} элементов')

for i in range(1, len(usr_list), 2):
    buff = usr_list[i-1]
    usr_list[i-1] = usr_list[i]
    usr_list[i] = buff

print(f'Преобразуем его: {usr_list}')

