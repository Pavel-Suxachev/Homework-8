# Модуль 5. Часть 1. Уровень 1

class StringVar:
    def __init__(self, value):
        self.value = value
    def get(self):
        return self.value
    def set(self, value1):
        self.value = value1

value = 'Value'
value1 = 'Value1'
print(value)
print(value1)

# Модуль 5. Часть 1. Уровень 2

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def dist(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance
    
p1=Point(1,2)
p2=Point(2,3)
print(p1.dist(p2))

