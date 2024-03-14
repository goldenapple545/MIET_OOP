#!/usr/bin/python3

# Создайте родительский класс "Животное" (Animal), с методом
# "получить_скорость" (get_speed) и атрибутами "тип животного"
# (animal_type) и "возраст" (age). Создайте два наследуемых класса "Птица"
# (Bird) и "Рыба" (Fish), которые перезаписывают поведение метода
# родительского класса. Продемонстрируйте полиморфизм на примере этих
# двух классов и инкапсуляцию. Формула для метода "get_speed" в классе
# "Bird": self.age * 5 Формула для метода "get_speed" в классе "Fish": self.age
# * 2

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_type, age):
        self.animal_type = animal_type
        self.age = age

    @abstractmethod
    def get_speed(self):
        pass
