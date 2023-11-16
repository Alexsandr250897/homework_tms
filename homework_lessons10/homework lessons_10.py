import time


class Auto:
    def __init__(self,brand: str, age: int, mark: str,
                 color: str ='white',weight:int= 1000):
        self.mark = mark
        self.brand = brand
        self.age = age
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        # Если использовать self.age +=1 происходит ошибка invalid syntax
        return self.age +1


s1 = Auto('mersedes', 2000, 'w210')
s2 = Auto('audi', 2002, 'a6')
s3 = Auto('bmw', 1999, 'e39')

class Truck (Auto):
    def __init__(self,max_load:int):
        self.max_load = max_load
        super().__init__(brand='mersedes',age=2000,mark='w210',
                         color= 'red',weight= 1500)

    def move(self):
        print('attention', 'move')

    def load(self):
        time.sleep(1)
        print('load')
s4 = Truck(2000)
print(s4.load())
class Car(Auto):
    def __init__(self,max_speed: str):
        super().__init__(brand='mersedes',age=2000,mark='w210',
                         color='green',weight=2000)
        self.max_speed =max_speed
    def move(self):
        print('move',self.max_speed)
s5 = Car('<220>')
print(s5.move())
