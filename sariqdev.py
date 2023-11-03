# son = int(input("Son kiriting: "))
# kvadrat = son ** 2
# print(f"{son} ning kvadrati {kvadrat} ga teng")

# son1 = int(input("Son kiriting: "))
# kub = son1 ** 3
# print(f"{son1} ning kubi {kub} ga teng")

# yil = int(input("Yilingizni kiriting: "))
# yosh = 2023 - yil
# print(f"Sizning yoshingiz {yosh} da")


# davlatlar = ["France", "USA", "Spain", "Germany", "Argentina", "Brazil"]
# print(davlatlar)
# print(len(davlatlar))
# davlatlar.sort(reverse=False)
# print(davlatlar)

# juft_sonlar = list(range(120, 1200, 2))
# print(juft_sonlar)
# print(sum(juft_sonlar))
# print(max(juft_sonlar) - min(juft_sonlar))
# print(list(juft_sonlar[:20]))
# print(list(juft_sonlar[-20:]))
# print(list(juft_sonlar[530:550]))


# taomlar = []
# taomlar.append("osh")
# taomlar.append("mastava")
# taomlar.append("shashli")
# taomlar.append("qozon kabob")
# taomlar.append("sho'rva")
# print(taomlar)

# nonushta = taomlar[:]
# print(nonushta)

# nonushta.remove("osh")
# nonushta.remove("qozon kabob")
# nonushta.remove("mastava")
# nonushta.append("non")
# nonushta.append("somsa")

# print(f"Taomlar: {taomlar}")
# print(f"Nonushta: {nonushta}")

# tuple(nonushta)
# nonushta[0] = "non va somsa"
# print(nonushta)



# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())


# admin = input("Login kiriting: ")
# if admin == "admin":
#     print(f"Hush kelibsiz ! {admin}")
# else:
#     print("Xush kelibsiz ! ")



# son = int(input("Son kiritng: "))
# if son % 2 == 0:
#     print("Rahmat")
# else:
#     print("Bu juft son emas !")



# yosh = int(input("Yoshingizni kiriting: "))

# if yosh <= 4 or yosh >= 65:
#     price = 0
# elif yosh <= 18:
#     price = 8000
# elif yosh >= 18:
#     price = 10000
# print(f"Sizga kirish {price} so'm")


# x = input("Son kiriting: ")
# y = input("Son kiriting: ")

# if x == y:
#     print(f"IF ishladi: {x} = {y}")
# elif x < y:
#     print(f"Elif ishladi: {x} < {y}")
# else:
#     print(f"Else ishladi: {x} > {y}")


# mahsulotlar = ["pamidor", "guruch", "bodring", "non" , "piypz", "yog'", "cola", "suv", "banan", "olma", "sut"]
# savat = []

# for i in range(5):
#     savat.append(input(f"Savatga {i+1} mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savat bo'sh")


# mahsulotlar = ["pamidor", "guruch", "bodring", "non" , "piypz", "yog'", "cola", "suv", "banan", "olma", "sut"]
# savat = []

# for i in range(5):
#     savat.append(input(f"Savatga {i+1} mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print(f"Do'konimizda quydagi mahsulotlar yo'q")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotrlar mavjud")


# users = ["anvar", "izzat", "samariddin", "abdulloh", "rixsiboy"]
# login = input("Login kiriting: ")
# if login in users:
#     print(f"Bu {login.title()} degaan login mavjud !")
# else:
#     print("Xush kelibisz !")


# son = int(input("Istalgan butun son: "))
# for i in range(1, 11):
#     if not son % i:
#         print(f"{son} soni {i} ga qoldiqsiz bo'linadi")


# yosh = int(input("Yoshingiz nechida? "))

# if yosh <= 4 or yosh >= 60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")


# son = float(input("Juft son kiriting: "))
# if son % 2 == 0:
#     print("Bu son juft emas")
# else:
#     print("Rahmat!")


# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x } ={y}")
# elif x<y:
#     print(f"{x} < {y}")
# else:
#     print(f"{x} > {y}")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")  




# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print(f"Xush kelibsiz! {login}")



# otam = {
#     "ism" : "adham irmukhammedov",
#     "yosh" : 47,
#     "t_yil" : 1976
# }

# print(f"\nIsimlari: {otam['ism'].title()} \nYoshlari: {otam['yosh']} \nTug'ulgan yillari: {otam['t_yil']}\n")


# family = {
#     "adam" : "osh",
#     "onam" : "norin",
#     "ukam" : "gamburger",
#     "uakm 2" : "neskuik"
# }

# print(f"Onamning sevimli taomlari {family['onam']}")


# python_malumot_turlari = {
#     "string" : "matn",
#     "integer" : "butun son",
#     "float" : "o'nlik son",
#     "list" : "ro'yhat",
#     "tuple" : "o'zgarmas ro'yhat",
#     "dict" : "lug'at",
#     "bool" : "true, false"

# }

# print(python_malumot_turlari)


# soz = input("Kalit so'z kiriting: ".lower())
# print(python_malumot_turlari.get(soz, "Mavjud emas"))

# soz = input("Kalit so'z kiriting: ".lower())
# tarjima = python_malumot_turlari.get(soz)
# if tarjima == None:
#     print("Bunday so'z mavjud")



