#HOME WORK

# class Passenger:
#     def __init__(self, passportID:int, fullname:str, gender:str) -> None:
#         self.passportID = passportID
#         self.fullname = fullname
#         self.gender =gender

#     def setPassportID(self):
#         return self.passportID
    
#     def getPasswordID(self):
#         return self.passportID
    
#     def setFullName(self):
#         return self.fullname
    
#     def getFullName(self):
#         return self.fullname
    
#     def setGender(self):
#         return self.gender
    
#     def getGender(self):
#         return self.gender
    
#     def __str__(self) -> str:
#         return f"\nPasswordID: {self.passportID}\nFullName: {self.fullname}\nGender: {self.gender}"
    
# Passenger1 = Passenger(7777, "Anvar Irmukhammedov", "Male")
# # print(Passenger1)


# class Driver(Passenger):
#     def __init__(self, passportID: int, fullname: str, gender: str, age: int) -> None:
#         super().__init__(passportID, fullname, gender)
#         self.age = age

#     def setAge(self):
#         return self.age
    
#     def __str__(self) -> str:
#         return f"Yoshi: {self.age}\n"
    
# Driver1 = Driver(12345, "Ali Aliyev", "Male", 21)
# # print(Driver1)


# class Train:

#     def __init__(self, traindID: int, name:str, speed: str, driver: Driver) -> None:
#         self.trainID = traindID
#         self.name = name
#         self.speed = speed
#         self.driver = driver

#     def setTraindID(self):
#         return self.trainID
    
#     def getTrainID(self):
#         return self.trainID
    
#     def setName(self):
#         return self.name
    
#     def getName(self):
#         return self.name
    
#     def setSpeed(self):
#         return self.speed
    
#     def getSpeed(self):
#         return self.speed
    
#     def __str__(self) -> str:
#         return f"TrainID: {self.trainID}\nName: {self.name}\nSpeed: {self.speed}\nDriver: {self.driver}"
    
# Train1 = Train(54321, "Afrosiyo", "350\km", Driver1)
# # print(Train1)



# class Platform:
#     def __init__(self, platformID:int, status:str) -> None:
#         self.plantfordID = platformID
#         self.status = status

#     def setPlatfordID(self):
#         return self.plantfordID
    
#     def getPlatformID(self):
#         return self.plantfordID
    
#     def setStatus(self):
#         return self.status
    
#     def getStatus(self):
#         return self.status
    
#     def __str__(self) -> str:
#         return f"PlatformaID: {self.plantfordID}\nStatus: {self.status}"
    
# Platform1 = Platform(55355, "Janbuiy Vogzal")
# # print(Platform1)


# class Trip:
#     def __init__(self, from_dan:str, to_gacha:str, train: Train, platform: Platform, passagers: Passenger, priceTrip: int, dateTrip: str) -> None:
#         self.from_dan = from_dan
#         self.to_gacha = to_gacha
#         self.train = train
#         self.platform = platform
#         self.passagers = []
#         self.priceTrip = priceTrip
#         self.dateTripe = dateTrip

#     def setFrom_dan(self):
#         return self.from_dan
    
#     def getFrom_dan(self):
#         return self.from_dan
    
#     def setTo_gacha(self):
#         return self.to_gacha
    
#     def getTo_gacha(self):
#         return self.to_gacha
    
#     def setTrain(self):
#         return self.train
    
#     def getTrain(self):
#         return self.train
    
#     def setPlanform(self):
#         return self.platform
    
#     def getPlanform(self):
#         return self.platform
    
#     def setPassagers(self):
#         return self.passagers
    
#     def getPassagers(self):
#         return self.passagers
    
#     def setPriceTrip(self):
#         return self.priceTrip
    
#     def getPriceTrip(self):
#         return self.priceTrip
    
#     def setDateTrip(self):
#         return self.dateTripe
    
#     def getDateTrip(self):
#         return self.dateTripe
    
#     def __str__(self) -> str:
#         return f"{self.from_dan}dan ={self.to_gacha}gacha\n{self.train}{self.platform}\nTrip narxi: {self.priceTrip}$\nTrip sanas: {self.dateTripe}\n"
    
# Trip1 = Trip("17 Oktabr", "20 Oktabr", Train1, Platform1, Passenger1, 1000, "6-iyun")
# # print(Trip1)


# class RailwayStation:
#     def __init__(self, name: str, adress: str, trip: Trip) -> None:
#         self.name = name
#         self.adress = adress
#         self.trip = trip

#     def setName(self):
#         return self.name
    
#     def getName(self):
#         return self.name
    
#     def setAdress(self):
#         return self.adress
    
#     def getAdress(self):
#         return self.adress

#     def __str__(self) -> str:
#         return f"\nBekat nomi: {self.name}\nAdress: {self.adress}\n{self.trip}\n"
    
# RailwayStation1 = RailwayStation("Paxtakor bekati", "Tashkent Navoiy ko'chasi", Trip1)
# print(RailwayStation1)

"HOME WORK"

# class Authors:
    
#     def __init__(self, first_name:str, last_name:str) -> None:
#         self.first_name = first_name
#         self.last_name =last_name
    
#     def getFullInfo(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def __str__(self) -> str:
#         return self.getFullInfo()
    
# Authors1 = Authors("Hudoyberdi", "To'xtaboyev")
# Authors2 = Authors("Alisher", "Navoiy")


# class Book:

#     def __init__(self, name:str, page_size:int, authors_list:list) -> None:
#         self.name = name
#         self.page_size = page_size
#         self.authors_list = authors_list
        
#     def getName(self):
#         return self.name
    
#     def getAuthors(self, authors: Authors):
#         self.authors_list.append(authors)

#     def getAuthorslar(self):
#         f = "Yozuvchilar:\n"
#         for i, a in enumerate(self.authors_list, 1):
#             f += f"{i} - Yozuvchi: {a}\n"
#         return f
    
#     def __str__(self):
#        return self.getAuthorslar()

# Authorslar = [Authors1, Authors2]
# book1 = Book("Sehrli Qalpoqcha", 150, Authorslar)
# book2 = Book("Xamsa", 200, Authorslar)


# class Library:

#     def __init__(self, name:str, adress:str, book:list) -> None:
#         self.name = name
#         self.adress = adress
#         self.book = book

#     def getName(self):
#         return f"Kutubxona: {self.name}"
    
#     def getAdress(self):
#         return f"Manzili: {self.adress}"
    
#     def getAllBooks(self, bk_obj:Book):
#         self.book.append(bk_obj)

#     def addBooks(self, *args:Book):
#         for i in args:
#             self.book.append(i)

#     def __str__(self):
#         g = "Kitoblar:\n\t"
#         for i, kitob in enumerate(self.book, 1):
#             g += f"\n{i} - kitobning nomi: {kitob.getName()}\n{kitob.getAuthorslar()}\n***********************"
#         return g
    
# Books = [book1, book2]
# kutubxona = Library("Navoiy", "Paxtakor ko'chasi", Books)
# print(kutubxona)


# class Phone:

#     def __init__(self, name:str, price:int) -> None:
#         self.name = name
#         self.price = price

#     def __add__(self, other):
#         return self.price + other.price
    
#     def __eq__(self, other):
#         return self.price == other
    
#     def __mul__(self, other):
#         return self.price * other.price
    
#     def __lt__(self, other):
#         return self.price > other

# Phone1 = Phone("iPhone X", 2)
# Phone2 = Phone("Samsung S20", 5)

# print(Phone1 * Phone2)




