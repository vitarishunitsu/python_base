class Matrix:
    def __init__(self, inp_list):
        self.data = inp_list

    def __str__(self):
        return f'{self.data}'

    def __add__(self, other):
        new_matrix = self.data[:]
        for column in range(len(new_matrix)):
            for row in range(len(new_matrix[column])):
                new_matrix[column][row] += other.data[column][row]
        return Matrix(new_matrix)


my_list_1 = [
    [1, 2, 3],
    [1, -2, 3],
    [0, 2, 15],
]

my_list_2 = [
    [6, 2, 5],
    [2, -2, 3],
    [1, 2, 15],
]

my_matrix_1 = Matrix(my_list_1)
my_matrix_2 = Matrix(my_list_2)
print(my_matrix_1 + my_matrix_2)
