#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_type, age, weight):
        self.animal_type = animal_type
        self.age = age
        self.__weight = weight

    @abstractmethod
    def get_speed(self):
        pass

    def print_animal(self):
        print(f'Parent method: {type(self).__name__}, do something')
