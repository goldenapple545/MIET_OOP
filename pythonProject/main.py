#!/usr/bin/python3S
from parent_class import Animal


class Bird(Animal):
    def __init__(self, animal_type, age, fly_height):
        super().__init__(animal_type, age, weight=0)
        self.__fly_height = fly_height

    def get_speed(self):
        return self.age * 5


class Fish(Animal):
    def __init__(self, animal_type, age, swim_deep):
        super().__init__(animal_type, age, weight=0)
        self.__swim_deep = swim_deep

    def get_speed(self):
        return self.age * 2

    def print_animal(self):
        print(f'Child method: {type(self).__name__}, I swim in river!')


if __name__ == "__main__":
    parrot = Bird("Bird", 5, 200)
    gold_fish = Fish("Fish", 3, 100)

    print(f'Parrot speed: {parrot.get_speed()}')
    print(f'Gold fish speed: {gold_fish.get_speed()}')

    parrot.print_animal()
    gold_fish.print_animal()
