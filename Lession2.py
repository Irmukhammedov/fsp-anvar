import math

# a = input("Son kiriting: ")
# a = int(input("Son kiritng: "))
# print(a, type(a))

# print('Salom' , end="\n")
# print("Alex!" , end="\n\n")

end="\n"   #bir qator pasga tushurib beradi

sep=""   #"print" dagi qiymatlani orasiga tasir ko'rsatadi

math   #math bilan ishlash doim FLOAT turida malumot qaytaradi



a = abs(7 - 10)   #manfiy soni musbat qilib beradi   |  |  "abs"
b = pow(2, 3)   #darajaga oshirish  2^3
c = math.pow(2, 3)   #FLOAT turida malumot qaytaradi
b1 = math.sqrt(16)   #ildiz osti

print(a, b, c, b1)

print(math.pi) #bu o'zgaruvchi

x = math.floor(4.7)   #pasga yaxlitlab oladi  (4)
x1 = math.ceil(4.2)   #tepaga yaxlitlab oladi (5)
x2 = math.exp(1)    #e o'zi bo'lsa (1) qo'yiladi  (e = 2,71)
l = [2, 3, 4, 5, 6, 7,]  #(SUM) hammasini qo'shib beradi
x3 = sum(l)
x4 = max(l)    #(MAX) eng kotta sonni aniqlab beradi
x5 = min(l)    #(MIN) eng kichik sonni aniqlab beradi
print(x , x1 , x2 , x3 , x4 , x5)


x = int(input("Son kiriting: "))
a = int(input("Son kiriting: "))
c = int(input("Son kiriting: "))

L = (math.sqrt(math.exp(x) - math.cos(pow(x, 2) * pow(a, 5)) ** 4) + math.atan)(math.atan( a - x ** 5) ** 4) / (math.exp(1) * math.sqrt(abs(a + x * pow(c, 4))))

print("Natija:" , L)

x = int(input("Son kiriting: "))
y = int(input("Son kiriting: "))

F = (math.sqrt(2 + y) ** 2 + math.sqrt(math.sin(y + 5)) ** 7) / (math.log(x + 1) - y ** 3)

F = (math.sqrt(pow(2 + y, 2) + pow(math.sin(y + 5), 1 / 7))) / (math.log(x + 1) - y ** 3)

