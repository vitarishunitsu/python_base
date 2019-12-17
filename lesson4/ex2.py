some_list = [1, 27, 2, 0, -4, 876, 32, 45, 56, 67, 12, -9, -10, -12, 0, 17, 15, 19, -19, 90, 150, 140]

new_list = [some_list[i] for i in range(len(some_list)) if some_list[i] > some_list[i - 1]]

print(new_list)