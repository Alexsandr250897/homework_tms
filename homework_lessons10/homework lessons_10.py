import  time
class Auto:
    brand: str
    mark: str
    age: int
    color: str
    weight:int
    def __init__(self,brand:str,age:int,mark:str):
        self.brand = 'mersedes'
        self.mark = 'w210'
        self.age = 2000
        self.color = 'black'
        self.weight = 2150
    def move(self):
        print('move')
    def stop(self):
        print('stop')

    def birthday(self):
        return self.age +1

s1 = Auto('mersedes',2000,'w210')
s2 = Auto('audi',2002,'a6')
s3 = Auto('bmw',1999,'e39')

class Truck (Auto):
    def __init__(self,max_load : int):
        self.max_load = 2000
    def move(self):
        print('attention', 'move')

    def load(self):
        print('load')
    time.sleep(1)
s4 = Truck(1500)
class Car(Auto):
    def __init__(self,max_speed: int):
        self.max_speed = '<200>'
    def move(self):
        print('move',self.max_speed)
s5 = Car(220)
print(s4.load())