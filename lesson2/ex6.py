# Торопился, поэтому обработку ввода не сделал. Её вообще уде пора через функции реализовывать...
product_list = []

for i in range(3):
    print(f'Товар № {i + 1}')
    name = input('Введите название товара: ')
    cost = input('Введите цену товара: ')
    qty = input('Введите количество товара: ')
    unit = input('Введите единицу измерения товара: ')
    product = {'название': name, 'цена': cost, 'количество': qty, 'ед.изм.': unit}
    product_list.append((i + 1, product))

print('Статистика: ')

print(product_list)
stat_product = dict.fromkeys(product.keys(), [])
print(stat_product)
for el in product_list:
    for key in el[1]:
        stat_product[key].append(el[1].get(key))

