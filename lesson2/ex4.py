while True:
    usr_str = input('Введите строку из нескольких слов, разделённых пробелами: ')
    if usr_str.count(' '):
        break
    print('Строка должна содержать пробелы!')

for index, el in enumerate(usr_str.split(' ')):
    print(f'Строка № {index}, содержимое {el[:10]}')