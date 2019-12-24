class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.position, self.name, self.surname])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


new_worker = Position('Pontius', 'Pilatus', 'Praefectus', {'wage': 100, 'bonus': 999})

print(f'{new_worker.get_full_name()} has {new_worker.get_total_income()} income')
