from random import randint, uniform

with open('ex5.txt', 'r+') as my_file:
    for _ in range(randint(10, 20)):
        my_file.write(f'{uniform(1, 100)} ')
    my_file.seek(0)
    file_content = my_file.read().split()
    print(file_content)

try:
    total = 0
    for _ in file_content:
        total += float(_)
    print(total)
except ValueError:
    print('File is damaged')
