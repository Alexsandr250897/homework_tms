# задание 1
# class Soda:
#     def __init__(self,additive:str):
#         self.additive = additive
#     def show_my_drink(self):
#         if self.additive:
#             print(f'Газировка и {self.additive}')
#         else:
#             print('Обычная газирока')
# i=Soda('')
# print(i.show_my_drink())
# задание 2
# class TriangleChecker:
#     def __init__(self, a: int, b: int, c: int):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         a = self.a
#         b = self.b
#         c = self.c
#         if (not isinstance(a,int)) and (not isinstance(b,int)) and (not isinstance(c,int)):
#             return 'Нужно вводить только числа'
#         elif a < 0 and b < 0 and c < 0:
#             return 'С отрицательными числами ничего не выйдет!'
#         elif a + b > c and b + c > a and a + c > b:
#             return 'Ура, можно построить треугольник!'
#         else:
#             return 'Жаль, но из этого треугольник не сделать.'
#
#
# tr = TriangleChecker(-6, -8, -3)
# print(tr.is_triangle())
# задание 3
# class KgToPounds:
#     def __init__(self,kg):
#         self.__kg = kg
#     def to_pounds(self):
#         return self.__kg * 2.204
#     @property
#     def kg(self):
#         return self.__kg
#     @kg.setter
#     def kg(self,ft_kg):
#         if isinstance(ft_kg,(int|float)):
#             self.__kg = ft_kg
#         else:
#             print('Необходимо ввести число')
#
# fyt = KgToPounds(28)
# print(fyt.to_pounds())
# fyt.kg = 'ten'

