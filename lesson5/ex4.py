numbers = {
    0: {'en': 'Null', 'ru': 'Ноль'},
    1: {'en': 'One', 'ru': 'Один'},
    2: {'en': 'Two', 'ru': 'Два'},
    3: {'en': 'Three', 'ru': 'Три'},
    4: {'en': 'Four', 'ru': 'Четыре'},
    5: {'en': 'Five', 'ru': 'Пять'},
    6: {'en': 'Six', 'ru': 'Шесть'},
    7: {'en': 'Seven', 'ru': 'Семь'},
    8: {'en': 'Eight', 'ru': 'Восемь'},
    9: {'en': 'Nine', 'ru': 'Девять'}
}
# Построчно пишем, на случай если файл огромный, чтобы не перегружать оперативную память
# Но если сильно хочется:
# lines_block = []
# В теле цикла
# lines_block.append([f"{numbers[_]['ru']}-{_}\n"])
# Менеджер контекста на запись открываем не в теле менеджера на чтение и пишем
# my_write_file.writelines(lines_block)

try:
    with open('ex4_read.txt', 'r') as my_read_file:
        with open('ex4_write.txt', 'w', encoding='utf-8') as my_write_file:
            for line in my_read_file:
                line = line.rstrip('\n').split('-')
                _ = int(line[1])
                my_write_file.write(f"{numbers[_]['ru']}-{_}\n")
except IOError:
    print('File does not exist')
