class Stationery:
    def __init__(self):
        self.title = 'Stationery'

    def draw(self):
        print(f'{self.title} drawing starting')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} is good choice')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        Stationery.draw(self)
        print(f'This {self.title.lower()} is hard')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        Stationery.draw(self)
        print(f'This {self.title.lower()} will draw bright')


my_stationery = Stationery()
my_stationery.draw()
print()

my_pen = Pen()
my_pen.draw()
print()

my_handle = Handle()
my_handle.draw()
print()

my_pencil = Pencil()
my_pencil.draw()
