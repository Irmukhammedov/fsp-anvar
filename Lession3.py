import math

"""
Solishtirish amallari
> kotta
< kichik
>= kotta yoki teng
<= kichik yoki teng
== tengmi?
!= teng emas

and  (Ko'paytruv misolida) bittasi "false" bo'lsa hammasi "false" bo'ladi
or   (Qoshu misolida) bittas "true" bo'lsa hammas "true" bo'ladi
not  (true >< false / false >< true)

"""



a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))

if a > b:
    print(f"{a} katta {b} dan")
    x = int(input("Son kiriting:"))
    if x % 2 == 0:
        print(f"{x} sonni juft:")
    else:
        print(f"{x} sonni juft emas:")
elif a == b:
    print(f"{a} teng {b} ga")
else:
    print(f"{b} katta {a} dan")


staj = int(input("Ish stajizni kiritingh: "))
oylik = int(input("Oylik maoshingizni kiriting: "))
u = 0
if 2 <= staj and staj < 5:
    u = oylik * 0.02
    oylik = oylik + u
elif 5 <= staj and staj < 10:
    u = oylik * 0.02
    oylik = oylik + u
else:
    print(f"Ushbu {staj} uchun oylik summasi ko'zda tutilmagan !!!")
   
print(f"Jami oylik: {oylik}")
print(f"Ustama summasi: {u}")



a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))
c = int(input("Son kiriting: "))

if a > 0:
    a = a ** 3
else:
    a = 0
if b > 0:
    b = b ** 3
else:
    b = 0
if c > 0:
    c = c ** 3
else:
    c = 0