#Торопился, поэтому обработку ввода не сделал. Её вообще уде пора через функции реализовывать...
product_list = []

for i in range(3):
    print(f'Товар № {i+1}')
    name = input('Введите название товара: ')
    cost = input('Введите цену товара: ')
    qty = input('Введите количество товара: ')
    unit = input('Введите единицу измерения товара: ')
    product = {'название': name, 'цена': cost, 'количество' : qty, 'ед.изм.': unit}
    product_list.append((i + 1, product))

print('Статистика: ')

stat_product = {'название': [], 'цена': [], 'количество' : [], 'ед.изм.': []}

for el in product_list:
   stat_product['название'].append(el[1]['название'])
   stat_product['цена'].append(el[1]['цена'])
   stat_product['количество'].append(el[1]['количество'])
   stat_product['ед.изм.'].append(el[1]['ед.изм.'])

print(stat_product)