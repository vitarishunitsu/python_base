with open('ex1.txt', 'w') as my_file:
    while True:
        inp_str = input('Записать в файл строку: ')
        if inp_str:
            my_file.writelines(inp_str + '\n')
        else:
            break
