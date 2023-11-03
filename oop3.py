# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):

#     def __init__(self, a:int, b:int) -> None:
#         self.a = a
#         self.b = b

#     def area(self):
#         return self.a * self.b
    
#     def perimeter(self):
#         return (self.a + self.b) * 2
    
#     def __str__(self) -> str:
#         return f"{self.a} {self.b}"
    
# r = Rectangle(4, 5)
# print(r.area())


# class Triangle(Shape):

#     def __init__(self, a, b, c) -> None:
#         self.a = a
#         self.b = b
#         self.c = c

#     def area(self):
#         p = (self.a + self.b +self.c) / 2
#         s = pow(p * (p - self.a) * (p * self.b) * (p * self.c), 1/2)
#         return s
    
#     def perimeter(self):
#         return (self.a + self.b + self.c)
    
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c}"
    
# t = Triangle(3, 4, 5)
# print(t.area())


# class Circle(Shape):

#     def __init__(self, r) -> None:
#         self.r = r

#     def area(self):
#         return 3.14 * self.r ** 2
    
#     def perimeter(self):
#         return 6.28 * self.r

#     def __str__(self) -> str:
#         return f"{self.r}" 

# from random import randint
# import time

# x = ['ali', 'alex', 'toshmat', 'azim']

# for i in range(10):
#     print(x[randint(0, len(x) - 1)])
#     time.sleep(2)