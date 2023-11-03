"""
Pythonda for va while
"""

range #funksiya   sonlar ketma ketligini tashkil qilib beradi:  MASALAN(1, 10),  agar:  print(list(range(1, 6)))   [1, 2, 3, 4, 5]

# for i in range(10):
#     print("Hello Python")

print(list(range(10)))   # 0 dan 10 gacha bo'lgan sonlarni chiqarib beradi

print(list(range(1, 10, 2))) #1-dan boshlab,   10-gacha,    2-ta qator tashlab sanaydi:  masalan(1, 3, 5, 7, 9) 

print(list(range(100, 11, -1)))  #-1 bu step (100-dan orqaga sanaydi 11-gacha)


x = [3, 2, 5]

print(x in 2)  #(2 soni X ichida bormi) degan manoda keladi   BOOL type da malumot qaytaradi (True - False)


for i in range(10): 
    print(i , "Hello Python")  #qiymat bu yerda - "Hello Python"
# 0 Hello Python
# 1 Hello Python
# 2 Hello Python
# 3 Hello Python
# 4 Hello Python
# 5 Hello Python
# 6 Hello Python
# 7 Hello Python
# 8 Hello Python
# 9 Hello Python

"i" #bu yerda har bitta qiymati bittadan ob yuradi 

"for" #'for' faqat 'range' biln ishlidi - har gal sikl aylanvotganda 'range' digi sonlani for aylantirib beradi "i" esa o'zi bilan ob yuradi

my_list = []
for i in range(1, 11):
    if i % 2 == 0:
        my_list.append(i) #my_list qo'shgin 'i'ga
print(my_list)
    
x = "Python"
for i in x:
    print(i)
#H
#E
#L
#L
#O

import random

#random tasodifiy sonlar tanlab beradi
print(random.randint(10, 100))  #randint ikkita argument qabul qiladi (10 dan  100 gacha oralig'ida)

print(random.randrange(1, 40, 3)) #1-startviy(dan) 40-stopviy(gacha)  3-stepviy(3 qator tashab sanidi)

print(random.randint)



numbers = []

for i in range(50):
    number = random.randint(1, 100)
    numbers.append(number) 
print(numbers)

x = []
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        if i in x:
         x.append(numbers)




a = int(input("Son kiriting: "))

for i in range(a, 0, -1):
    if a % i == 0:
        print(a)

