class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_mass(self, thickness):
        return self.__length * self.__width * thickness * 25


new_road = Road(5000, 20)

print(new_road.calc_mass(5))
