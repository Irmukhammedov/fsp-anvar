import random


# number = int(input('Son kiriting: '))

# i = 2
# while True:

#     if number % i == 0:
#         number = number / i
#         print(i)
#     if number % i == 0:
#         continue
#     elif number == 1:
#         break
#     else:
#         i += 1


# numbers = ['1 000 000', '1 233', '1 245 123', '123', ' 123 456']

# for i in numbers:
#     print(''.join(i.split()))

# a = '123 133'
# print(a.split())
# s = ''
# for i in a.split():
#     print(i)
#     s += i
# print(s)

# a = '123 133'
# l = ['33', '21', 'asd']
# s = ''.join(a.split())
# print(s)

# my_list = [str(i) for i in range(10, 33)]

# print('||'.join(my_list))

# m = ['123', 'asd', '!@#']
# print('^'.join(m))


# my_dict = {
#     'name' : 'Alex',
#     'age' : 22,
#     'numbers' : [2, 3, 4],
#     'phone_number' : '+998991234567'
# }

# m = ['name', 'club', 'country']
# n = {}
# print(n.fromkeys(m, 'Anvar'))
# print(n.fromkeys(m, 0))
# for key , value in my_dict.items():
    # print(f"{key} : {value}")
# my_dict['email'] = 'noname@gmail.com'
# my_dict['adress'] = 'Tashkent city'
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('age'))
# x = my_dict.popitem()
# my_dict.update()
# print(my_dict.get('age'))
# my_dict.setdefault('phone', '545363')
# print(my_dict)


#1-misol

# n = int(input("Son kiriting: "))
# x = int(input("Son kiriting: "))
# m = []

# for i in n,x:
#     if n < x:
#         m.append(i)
#         print(m, "O'sish")
#     elif n > x:
#         m.append(i)
#         print(m, 'Kamayish')
#     else:
#         print("Tartibsiz")


#2-misol

# a = []

# for i in range(20):
#     a.append(random.randint(1, 100))
# print(a)

# max_item = a[0]
# min_item = a[0]

# if i > max_item:
#     max_item == i

# elif i < min_item:
#     min_item == i

# print(f"{max_item} + {min_item} = {max_item + min_item}")


#3-misol

# n = int(input("Son kiriting: "))
# a = []

# for i in range(n):
#     a.append(input(str(i + 1) + '-sonni kiriting: '))
# print(a)

# s = 0
# for i in a:
#     if i >= 10 and i <= 99:
#         s + i
# print(s)


#4-misol

# a = []
# for i in range(10):
#     a.append(random.randint(1, 200))
# print(a)
# orta = sum(a) / len(a)

# toq = []
# juft = []
# for j in a:
#     if j % 2 == 0:
#         juft.append(j)
#     else:
#         toq.append(j)
# print(f"{toq} - toq sonlar")
# print(f"{juft} - juft sonlar")
# print(f"Orta arefmetigi: {orta}")


#5-misol
# a = int(input("Son kiriting: "))
# mylist = []
# for i in range(a):
#     mylist.append(int(input(str(i + 1) + '-sonni kiriting: ')))
# print(mylist)

# if i % 2 != 0:
#     print("Rost")
# elif i % 2 == 0:
#     print("Yolg'on")

#6-misol

# mylist = []
# for i in range(10):
#     mylist.append(random.randint(1, 200))
# print(mylist)

# for i in mylist:
#     if i % 3 == 0:
#         if i > 10 and i < 99:
#             print(f"ushbu {i} soni '3' ga bolinadi")

#7-misol

# mylist = [2, -2, 5, -5, 11, -11, 20, -20]
# g = 0
# for i in range(len(mylist)):
#     for j in range(i+1, len(mylist)):
#         if mylist[i] == mylist[j]:
#             g += 1
# print(g)


#8-misol

# n = input("Son kiriting: ").split()

# for i in n:
#     if n.count(i) >= 2:
#         print(f"{i} = {i} Takrorlanish mavjud")
#     else:
#         print("Takrorlanuvchi mavjudcemas")
#         break

#9-misol

# n = [4, 2, 5, 7, 9, -1]
# a = 0
# for i in n:
#     if i > 0:
#         a += i
# print(a)

#10misol

# a = int(input("Son kiriting:"))
# b = int(input("Son kiriting:"))
# s = []

# for i in range(a, b):
#     s.append(random.randint(1, 200))
# print(s)

# max_item = s[0]
# min_item = s[0]

# if i > max_item:
#     max_item = i
# else:
#     print(f"{i} Mavjud emas")

# if i < min_item:
#     min_item = i
# else:
#     print(f"{i} Mabjud emas 2")

# print(f"{max_item} = Max item")
# print(f"{min_item} = Min item")

#11-misol

# n = int(input("Manfiyga son kiriting: "))
# manfiy = []

# for i in range(n):
#     manfiy.append(random.randint(-100, -1))
# print(manfiy)

# manfiy_max = manfiy[0]
# for i in manfiy:
#     if i < manfiy_max:
#         manfiy_max = i

# m = int(input("Musbatga son kiriting: "))
# musbat = []

# for i in range(m):
#     musbat.append(random.randint(1, 100))
# print(musbat)

# musbat_max = musbat[0]
# for i in musbat:
#     if i > musbat_max:
#         musbat_max = i

# print(f"{manfiy_max} Manfiy Max /n {musbat_max} Musbat Max")

#12-misol

# n = [3, 5, 8, 0, 12, 4, 7, 9, 0, 2]

# main_1 = n.index(0)
# main_2 = n.index(0, main_1 + 1)

# umumiy = sum(n[main_1 + 1: main_2])
# print(f"Nollar orasidsgi yig'indi {umumiy}")

#13-misol

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# yigindi = sum(mylist[0::2])
# print(yigindi)

# mylist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# o = 0
# for i in range(1, len(mylist2), 2):
#     o += mylist2[i]
# print(o)

#14-misol

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# juft = sum(mylist[1::2])
# print(juft)

#15-misol

# a = int(input("Son kiriting: "))
# mylist = []
# for i in range(a):
#     mylist.append(random.randint(1, 500))
# print(mylist)
# b = []
# for i in mylist:
#     if i % 10 == 0:
#         b.append(i)
# print(f"{b} 10 soniga bo'linadi")

#16-misol

# a = int(input("Son kiriting: "))
# mylist = []
# for i in range(a):
#     mylist.append(random.randint(-50, 50))
# print(mylist)
# musbat_sonlar = []
# for i in mylist:
#     if i < 0:
#         musbat_sonlar.append(i)
# print(musbat_sonlar)

#17-misol

# a = int(input("Son kiriting: "))
# sonlar = []
# for i in range(a):
#     sonlar.append(random.randint(1, 500))
# print(f"TARTIBSIZ {sonlar}")
# osish = sorted(sonlar)
# print(f"O'SISH TARTIBIDA {osish}")

#18-misol

# a = int(input("Son kiriting: "))
# mylist = []
# for i in range(a):
#     mylist.append(random.randint(1, 100))
# print(mylist)
# m = []
# for i in mylist:
#     if i % 7 == 0:
#         m.append(i)
# print(f"Ushbu {m} sonlari 7 ga bo'linadi")

#19-misol

# r = int(input("Musbat sonlar uchun: "))
# musbat = []
# for i in range(r):
#     musbat.append(random.randint(-50, 50))
# print(musbat)
# musbat_list = []
# for i in musbat:
#     if i > 0:
#         musbat_list.append(i)
# print(musbat_list)

# z = int(input("Manfiy sonlar uchun: "))
# manfiy = []
# for j in range(z):
#     manfiy.append(random.randint(-50, 50))
# print(manfiy)
# manfiy_list = []
# for j in manfiy:
#     if j < 0:
#         manfiy_list.append(j)
# print(manfiy_list)

# print(f"Musbat sonlar {musbat_list}")
# print(f"Manfiy sonlar {manfiy_list}")


#20-misol

# mylist = []
# for i in range(20):
#     mylist.append(random.randint(1, 100))
# print(mylist)
# min_item = mylist[0]
# for i in mylist:
#     if i < min_item:
#         min_item = i
# min_index = mylist.index(min_item)
# print(f"Min qiymat {min_item} Min index {min_index}")

#21-misol

# mylist = []
# for i in range(20):
#     mylist.append(random.randint(1, 100))
# print(mylist)
# max_item = mylist[0]
# for i in mylist:
#     if i > max_item:
#         max_item = i
# max_index = mylist.index(max_item)
# print(f"Max qiymat {max_item} Max index {max_index}")

#22-misol

# x = [5, -2, 3, -7, 8, 0, -4, 1, 6, -9, 2, 4, -3, 7, 10, -6, 9, -1, -8, 11]
# manfiy = []
# indexlar = []
# for i in range(len(x)):
#     if x[i] < 0:
#         manfiy.append(x[i])
#         indexlar.append(i)
#     if len(manfiy) == 3:
#         break
# print(f"Manfiy sonlar {manfiy}")
# print(f"Indexlari {indexlar}")

#23-misol

# mylist = [random.randint(1, 100) for i in range(20)]
# print(mylist)

# max_item = mylist[0]
# max_index = 0
# min_item = mylist[0]
# min_index = 0
# for i, v in enumerate(mylist):
#     if v > max_item:
#         max_item = v
#         max_index = i

#     if v < min_item:
#         min_item = v
#         min_index = i

# tmp = mylist[max_index]
# mylist[max_index] = mylist[min_index]
# mylist[min_index] = tmp
# print("Resoult", mylist)

#24-misol

# x = [5, -2, 3, -7, 8, 0, -4, 1, 6, -9, 2, 4, -3, 7, 10, -6, 9, -1, -8, 11]
# manfiy = []
# indexlar = []
# for i in range(len(x)):
#     if x[i] > 0:
#         manfiy.append(x[i])
#         indexlar.append(i)
#     if len(manfiy) == 3:
#         break
# print(f"Manfiy sonlar {manfiy}")
# print(f"Indexlari {indexlar}")

#25-misol

# m = [3, 5, 8, 14, 16, 29, 35, 12]
# v = 11
# n = []
# n1 = []
# for i in m:
#     if i < 11:
#         n.append(i)
#     elif i > 11:
#         n1.append(i)

# m.clear()
# m.extend(n)
# m.append(11)
# m.extend(n1)
# print(m)

#26-misol

# a = [3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 1, 9, 6, 4]

# v1 = a.index(1)
# v2 = a.index(1, v1 + 1)
# umumiy = sum(a[v1 + 1: v2])
# print(umumiy)