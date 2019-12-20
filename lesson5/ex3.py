try:
    with open('ex3.txt', 'r') as my_file:
        total = 0
        for ind, line in enumerate(my_file):
            line = line.rstrip('\n').split()
            try:
                line[1] = float(line[1])
                if line[1] < 20000:
                    print(f'Employee {line[0]} has salary less than 20000.00 ')
                total += line[1]
            except ValueError:
                print('Not numeric format of salary')
    print(f'Total employees: {ind + 1}, with {total} total salary')
    print(f'Average salary for employee: {total/(ind + 1):0.2f}')
except IOError:
    print('File does not exist')