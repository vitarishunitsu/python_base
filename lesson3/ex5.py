def analyse_list(inp_str):
    """
    Calculates summary of numbers in list before stop-symbol 'Q' or not numeric symbols.
    :param inp_str: list of numbers/any types
    :return: float-type summary, bool-type quit flag - be changed if 'Q' recognized, int-type last numeric symbol in inp_str
    """
    result = 0
    quit_flag = False
    p = len(inp_str)
    for _ in inp_str:
        try:
            result += float(_)
        except ValueError:
            p = inp_str.index(_)
            if _.upper() == 'Q':
                quit_flag = True
                print('Команда выхода из программы')
                break
            else:
                print(f'{_} не является числом!')
                break
    return result, quit_flag, p


total = None
stop_sig = False
print('Вводите строку чисел, разделённых пробелами, для выхода из программы введите "Q": ', end='')
while not stop_sig:
    usr_str = input().split()
    cur_sum, stop_sig, ind = analyse_list(usr_str)
    if total is None:
        total = 0
    else:
        print(f'{total} + ', end='')
    total += cur_sum
    if usr_str[:ind]:
        print(' + '.join(usr_str[:ind]), end=' = ')
    else:
        print('0', end=' = ')
    print(total)
