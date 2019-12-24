from time import sleep


def light_gen():
    index = 0
    direction = True
    while True:
        yield index
        index = index + 1 if direction else index - 1
        if index == 0:
            direction = True
        elif index == 2:
            direction = False


class TrafficLight:
    def __init__(self, t_red=7, t_yellow=2, t_green=5):
        self.__index_list = light_gen()
        self.__color = [
            {'red': t_red},
            {'yellow': t_yellow},
            {'green': t_green}
        ]

    def running(self, exit_cnt):
        for _ in self.__index_list:
            exit_cnt -= 1
            current_light, time_on = list(*self.__color[_].items())
            print(f'Now is {current_light} light for {time_on} seconds')
            sleep(time_on)
            if not exit_cnt:
                break


cross_road_1 = TrafficLight()
cross_road_2 = TrafficLight(3, 1, 2)

# Каждый светофор живёт сам по себе
cross_road_1.running(2)
print()
cross_road_2.running(2)
print()
cross_road_1.running(3)
print()
cross_road_2.running(5)
