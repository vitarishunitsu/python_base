import json

firms = {}
firms_list = []
try:
    with open('ex7.txt', 'r') as my_file:
        total_profit = 0
        for ind, line in enumerate(my_file):
            line = line.rstrip('\n').split()
            try:
                profit = float(line[-2]) - float(line[-1])
                if profit > 0:
                    total_profit += profit
            except ValueError:
                print('Not numeric format')
            firms.update({line[0]: profit})
        aver_profit = total_profit / (ind + 1)
    firms_list.append(firms)
    firms_list.append({'average profit': aver_profit})

    with open('ex7.json', 'w') as my_json:
        json.dump(firms_list, my_json)

# Кириллица в файле закодирована. Попробуем считать обратно.
    with open('ex7.json', 'r') as my_json:
        print(json.load(my_json))

except IOError:
    print('File does not exist')