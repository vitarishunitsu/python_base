class Car:
    __is_police = False

    def __init__(self, speed=0, color='black', name='Ford'):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        if self.__is_police:
            print(f'Police {self.color} {self.name} has started')
        else:
            print(f'{self.color.capitalize()} {self.name} has started')

    def stop(self):
        print(f'{self.color.capitalize()} {self.name} has stopped')
        self.speed = 0

    def turn(self, direction):
        print(f'{self.color.capitalize()} {self.name} has turned {direction}')

    def show_speed(self):
        print(f'Current speed of {self.color.lower()} {self.name} is {self.speed}')


class PoliceCar(Car):
    __is_police = True


class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print(f'Speed limit 60 exceeded')


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print(f'Speed limit 40 exceeded')


class SportCar(Car):
    pass


police = PoliceCar(color='black and white')
police.go()
police.speed = 90
police.show_speed()
police.turn('right')
police.stop()
print()

lamborghini = SportCar(color='white', name='Lamborghini')
lamborghini.go()
lamborghini.speed = 100
lamborghini.show_speed()
lamborghini.turn('left')
lamborghini.stop()
print()

mario_car = WorkCar(name='Fiat', color='yellow')
mario_car.go()
mario_car.speed = 100
mario_car.show_speed()
mario_car.turn('back')
mario_car.stop()
print()

my_car = TownCar(name='Volkswagen', color='grey')
my_car.go()
my_car.speed = 70
my_car.show_speed()
my_car.turn('right')
my_car.stop()
print()
