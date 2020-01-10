class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        if self.qty - other.qty > 0:
            return Cell(self.qty - other.qty)
        else:
            print(f'Клетка {self.qty} меньше {other.qty}')
            return Cell(self.qty)

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)

    def make_order(self, row):
        for i in range(0, self.qty, row):
            print(row*'*')
        print((self.qty % row)*'*')


my_cell = Cell(36)
new_cell = Cell(15)

my_cell = my_cell + new_cell
my_cell.make_order(10)

my_cell = my_cell - new_cell
my_cell.make_order(15)

my_cell = new_cell - my_cell
my_cell.make_order(5)

my_cell = my_cell * new_cell
my_cell.make_order(10)

my_cell = my_cell / new_cell
my_cell.make_order(20)