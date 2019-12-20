try:
    with open('ex2.txt', 'r') as my_file:
        for ind, val in enumerate(my_file):
            val = val.rstrip('\n')
            print(f'String # {ind + 1} "{val}" has {len(val)} symbols')
except IOError:
    print('File does not exist')