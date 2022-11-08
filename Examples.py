# clase #5
from typing import Tuple, Dict, List
from typing import Tuple
from typing import Dict, List
positives: List[int] = [1, 2, 3, 4, 5]
users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000',
    },
    {
        'name': 'México',
        'people': '9000000',
    },
    {
        'name': 'Colombia',
        'people': '999999999999'
    },
]
numbers: Tuple[int, float, int] = (1, 0.5, 1)


CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 1)
    },
]




# # Creando un iterador
# my_list = [1,2,3,4,5]
# my_iter = iter(my_list)
# # Iterando un iterador
# print(next (my_iter))
# # Cuando no quedan datos, la excepción StopIteration es elevada


# # Creando un iterador
# my_list = (1,2,3,4,5]
# my_iter = iter(my_list)
# # Iterando un iterador
# while True:
# try:
# element = next (my_iter)
# print(element)
# except StopIteration:
# break


# class EvenNumbers:
# "'''Clase que implementa un iterador de todos los números pares, o los números pares hasta un máximo"""
# def
# -init__(self, max-None):
# self.max = max
# def
# iter _(self):
# self.num = 0
# return self
# def
# next _(self):
# if not self.max or self.num < self.max:
# result = self.num
# self.num += 2
# return result
# else;
# raise StopIteration


# def my_gen():
# "*"'Un ejemplo de generadores"""
# print( 'Hello world!')
# n = 0
# yield n
# print( 'Hello heaven!")
# n = 1
# yield n
# print( 'Hello hell!')
# n = 2
# yield n
# a = my_gen()
# print(next(a)) #Hello world! print(next(a)) #Hello heaven! print(next(a)) #Hello hell! print(next(a)) StopIteration


# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}
# my_set3 = my_set1 | my_set2
# print(my_set3)

# my_set1 = {3, 4,
# 5}
# my_set2 = {5, 6, 7}
# my_set3 = my_setl & my_set2
# print(my_set3)

# my_set1 = {3, 4, 5}
# my_set2 = 15, 6,
# my_set3 = my_set1 - my_set2
# print(my_set3)
# my_set4 = my_set2 - my_setl
# print(my_set4)


# my_seti = (3, 4, 5}
# my_set2 = {5, 6, 7}
# my_set3 = my_seti ^ my_set2
