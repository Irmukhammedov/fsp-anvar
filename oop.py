import math

# class MyCar:
#     name = "Zaparo'j"
#     name2 = "Malibu"


# car1 = MyCar()
# car2 = MyCar()
# print(car1.name)
# print(car2.name2)




# class Phone:
#     def __init__(self, phone:str, price:int, color:str) -> None:
#         self.phone = phone
#         self.price = price
#         self.color = color

#     def getName(self):
#         return self.phone
    
#     def getPrice(self):
#         return self.price
    
#     def getColor(self):
#         return self.color
    
#     def __str__(self):
#         return self.phone
    
# p1 = Phone('iPhone 14 Pro Max', 1400, 'black')
# p2 = Phone('Redme 12', 750, 'white')
# p3 = Phone('Samsung S23', 1200, 'blue')

# phones = [p1, p2, p3]
# s = 0
# for obj in phones:
#     if obj.getColor == 'black':
#         s += obj.getPrice
# print(s)


"HOME WORK"

# class Car:
#     def __init__(self, carname:str, carprice:int, carcolor:str, carcountry:str, carspeed:str) -> None:
#         self.carname = carname
#         self.carprice = carprice
#         self.carcolor = carcolor
#         self.carcountry = carcountry
#         self.carspeed = carspeed

#     def getCarName(self):
#         return self.carname
    
#     def getCarPrice(self):
#         return self.carprice
    
#     def getCarColor(self):
#         return self.carcolor
    
#     def getCarCountry(self):
#         return self.carcountry
    
#     def getCarSpeed(self):
#         return self.carspeed
    
#     def __str__(self):
#         return f"{self.carname}\n{self.carprice}\n{self.carcolor}\n "

# carname1 = Car('Jentra', 15000, 'black', 'Uzbekistan', '220/km')
# carname2 = Car('BMW M5', 90000, 'yellow', 'Germany', '305/km')
# carname3 = Car('Mercades 222', 50000, 'white', 'Germany', '280/km')

# print(carname2)




# class File:
#     def __init__(self, file_name:str , file_size:float, file_format:str, file_created:str) -> None:
#         self.file_name = file_name
#         self.file_size = file_size
#         self.file_format = file_format
#         self.file_created = file_created

#     def getFile_Name(self):
#         return self.file_name
    
#     def getFile_Size(self):
#         return self.file_size
    
#     def getFile_Format(self):
#         return self.file_format
    
#     def getFile_Created(self):
#         return self.file_created
    
#     def __str__(self) -> str:
#         return f"{self.file_name}\n{self.file_size}\n{self.file_format}\n{self.file_created}"

# file1 = File('test', 77.3, 'py', 'C:\\Users\\HP\\Desktop\\FSP Anvar\\lession11_fayllar.py')
# file2 = File('football', 340.5, 'html', '17/10/2022')

# print(file1)


# class Vehicle:
#     def __init__(self, model:str, max_speed:str, year:int) -> None:
#         self.model = model
#         self.max_speed = max_speed
#         self.year = year

#     def getModel(self):
#         return self.model
    
#     def getMaxSpeed(self):
#         return self.max_speed
    
#     def getYear(self):
#         return self.year
    
#     def __str__(self):
#         return self.model
    
# car = Vehicle("BMW M8", '300/km', 2020)


# class Car(Vehicle):
#     def __init__(self, model: str, max_speed: str, year: int, price:str) -> None:
#         super().__init__(model, max_speed, year)
#         self.price = price

#     def getFullInfo(self):
#         return f"{self.model}\n{self.max_speed}\n{self.year}\n{self.price}\n"

#     def __str__(self):
#         return super().__str__() + self.price
    
# p = Car("Mercades", "280/km", 2023, "100,000$")
# print(p.getFullInfo())

# class Motosikl(Car):
#     def __init__(self, model: str, max_speed: str, year: int, price: str, country:int) -> None:
#         super().__init__(model, max_speed, year, price)
#         self.country = country

#     def getCountry(self):
#         return self.country
    
#     def getFullInfoMoto(self):
#         return f"{self.model}\n{self.max_speed}\n{self.year}\n{self.price}\n{self.country}"
    
#     def __str__(self):
#         return super().__str__() + self.country
    
# FullName = Motosikl("Audi", "400/km", 2021, "20,000$", 'USA')

# print(FullName.getFullInfoMoto())




# class Person:
#     def __init__(self, first_name:str, last_name:str, gender:str, age:int) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.age = age

#     def getFisr_Name(self):
#         return self.first_name
    
#     def getLast_Name(self):
#         return self.last_name
    
#     def getGender(self):
#         return self.gender
    
#     def getAge(self):
#         return self.age
    
#     def __str__(self) -> str:
#         return f"Ismi: {self.first_name}\nFamilyasi: {self.last_name}\nJinsi: {self.gender}\nYoshi: {self.age}"

# person1 = Person("Anvar", "Irmukhammedov", "Male", 20)
# print(person1)

"HOME WORK"

# class Shape:
#     def __init__(self, color:str) -> None:
#         self.color = color

#     def __str__(self) -> str:
#         return self.color
    
# Shape1 = Shape("red")
# print(Shape1)


# class Circle(Shape):
#     def __init__(self, color: str, radius:float) -> None:
#         super().__init__(color, radius)
#         self.radius = radius
   
#     def get_are(self):
#         return math.pi * pow(self.radius, 2)

#     def __str__(self) -> str:
#         return super().__str__() + self.radius
    
# radius1 = Circle("red", 1.0)
# print(radius1)

# class Rectangle(Shape):
#     def __init__(self, color: str, lenght:float, width:float) -> None:
#         super().__init__(color, lenght, width)
#         self.lenght = lenght
#         self.widht = width

#     def get_are(self):
#         return self.lenght * self.widht
    
#     def __str__(self) -> str:
#         return super().__str__() + self.lenght + self.widht
    
# Rectangle1 = Rectangle(1.0, 1.0)
# print(Rectangle1)

# class Square(Rectangle):
#     def __init__(self, color: str, lenght: float, width: float) -> None:
#         super().__init__(color, lenght, width)

#     def __str__(self) -> str:
#         return super().__str__()
    
# Square1 = Square

# class Car:
#     def __init__(self, name:str, color:str, speed:int) -> None:
#         self.name = name
#         self.color = color
#         self.speed = speed
    
#     def getName(self):
#         return self.name
    
#     def getColor(self):
#         return self.color
    
#     def getSpeed(self):
#         return self.speed
    
#     def getInfo(self):
#         return f"\n{self.color} rangli {self.name} moshinasi tezligi {self.speed} ga teng"
    
#     def __str__(self):
#         return self.getInfo
    
# Car1 = Car("Lacetti", "Oq", 220)
# Car2 = Car("Malibu", "Qora", 260)
# Car3 = Car("Matiz", "Kulrang", 180)

# Cars = [Car1, Car2, Car3]
# for cars1 in Cars:
#     print(cars1.getInfo())


# class Phone:
#     def __init__(self, name:str, color:str, price:float) -> None:
#         self.name = name
#         self.color = color
#         self.price = price

#     def setName(self, name):
#         self.name = name
    
#     def getName(self):
#         return self.name
    
#     def setColor(self, color):
#         self.color = color
    
#     def getColor(self):
#         return self.color
    
#     def setPrice(self, price):
#         self.price = price
    
#     def getPrice(self):
#         return self.price
    
#     def __str__(self) -> str:
#         return f"\nNome: {self.name}\nRangi: {self.color}\nNarxi: {self.price}$\n"



# Phone2 = Phone("Redmi Note 4X", "Qora", 150)
# Phone3 = Phone("iPhoneX", "Oq", 700)

# print(Phone2, Phone3)

# from uuid import uuid4

# class Person:
#     def __init__(self, name:str, surname:str, fathername:str) -> None:
#         self.name = name
#         self.surname =surname
#         self.fathername = fathername
    
#     def get_FullInfo(self):
#         return f"Ismi: {self.name}\nFamilyasi: {self.surname}\nOtasiningIsmi: {self.fathername}"
    
#     def __str__(self) -> str:
#         return self.get_FullInfo()
    
    
# class Student(Person):

#     def __init__(self, name: str, surname: str, fathername: str, Kurs:str) -> None:
#         super().__init__(name, surname, fathername)
#         self.__id = uuid4()
#         self.__kurs = Kurs

#     def add_kurs(self, kurs):
#         if kurs >= 0:
#             self.__kurs = kurs
#             print(kurs)
#         else:
#             print("kamaytirib bo'lmaydi")

#     def get_ID(self):
#         return self.__id

#     def get_kurs(self):
#         return self.__kurs

#     def __str__(self) -> str:
#         return super().__str__() + self.__kurs



# class Point:

#     def __init__(self, coordinateX: int, coordinateY: int) -> None:
#         self.coordinateX = coordinateX
#         self.coordinateY = coordinateY

#     def getCoordinateX(self):
#         return self.coordinateX
    
#     def getCoordinateY(self):
#         return self.coordinateY
    
#     def getCoordinate(self):
#         return f"{self.coordinateX} {self.coordinateY}"
    
#     def __str__(self) -> str:
#         return self.getCoordinate()


# class Circle(Point):

#     def __init__(self, coordinateX: int, coordinateY: int, radius: int, color: str) -> None:
#         super().__init__(coordinateX, coordinateY)
#         self.radius = radius
#         self.color = color

#     def getRadius(self):
#         return self.radius
    
#     def getColor(self):
#         return self.color
    
#     def __str__(self) -> str:
#         return super().__str__() + self.radius + " " + self.color
    



class Coint:
    def __init__(self, value:int) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"
        
Coint1 = Coint(20)
Coint1 = Coint(10)
print(Coint1)

class PaperMoney:
    def __init__(self, value:int) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"
    
PaperMoney1 = PaperMoney(100)
PaperMoney1 = PaperMoney(200)
print(PaperMoney1)
    

class Wallet:
    def __init__(self) -> None:
        self.allmoney = []

    def getAllPaperMoney(self):
        sum = 0
        a: int = 0
        for i in self.allmoney:
            if isinstance(i, PaperMoney):
                sum += i.value
                a += 1
        return f"\n\t{a} ta Paper Money\n\nSumma: {sum}\n"
    
    def getAllCoins(self):
        sum = 0
        a: int = 0
        for i in self.allmoney:
            if isinstance(i, Coint):
                sum += (i.value)
                a += 1
        return f"\n\t{a} ta Coin\n\tSumma: {sum}\n"
    
    def addMoney(self, value):
        self.allmoney.append(value)


Wallet1 = Wallet()
w1 = Coint(5)
w2 = Coint(10)
w3 = Coint(15)

w4 = [w1, w2, w3]

print(w4)