discipline = {}
try:
    with open('ex6.txt', 'r') as my_read_file:
        for line in my_read_file:
                line = line.rstrip('\n').split()
                name = line[0].rstrip(':')
                hours = 0
                for _ in range(1, 4):
                    if '-' not in line[_]:
                        pos = line[_].index('(')
                        hours += int(line[_][:pos])
                discipline.update({name: hours})
    print(discipline)
except IOError:
    print('File does not exist')