# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib,
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber("Hasan")
# print(salom_ber.__doc__)
# def calc (son):
#     for n in range(2,10):
#         if not son % n:
#             print(f"{son} {n} ga qoldiqsiz bulinadi - qoldiq {son%n}")
#         else:
#             print(f"{son} {n} ga qoldiq bilan bulinadi - qoldiq {son%n}")
#
# son = int (input("Istalgan son kiriting: "))
# calc(son)
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
#
# # avto1 = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2018)
# # avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanik', 2016, 15000)
# # avtolar = [avto1, avto2]
# # print(avtolar)
# print("Avtolar ruyhatini kiriting")
# avtolar = []
# while True:
#     print("Quyidagi ma'lumotlarni kiriting\n", end='')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# for avto in avtolar:
#     print(avto['model'])
# def fib(son):
#     ls = []
#     ks = []
#     for n in range(1, son+1):
#         if n>2:
#             x = ls[n-1]+ls[n-2]
#         ls.append(x)
#
#     return ls
#
#
#
# print(fib(int(input('Sonni kiriting'))))


# def daraja (n):
#     return lambda x: x**n
# kv = daraja(2)
# kub = daraja(3)
#
# print(kv(2))
# print(kub(3))

# from math import sqrt
# son = list(range(11))
# ildiz = list(map(sqrt,son))
# print(ildiz)

# sonlar = list(range(11))
# # def draja (x):
# #     return x**2
# # print(list(map(draja, sonlar)))
#
# print(list(map(lambda x: x**2, sonlar)))

# a = [4, 5, 6]
# b = [7, 8,9]
# print(list(map(lambda x,y:x+y, a, b)))


# import random as r
# sonlar = r.sample(range(100), 10)
# # def juft (x):
# #     return x%2==0
# # juft_son = list(filter(juft, sonlar))
# juft_son = list(filter(lambda x: x%2==0, sonlar))
# print(sonlar)
# print(juft_son)

# mevalar = ['olma','anor','anjir','baftoli',"o'rik","tarvuz","qovun","banan"]
# mevalar_b = list(filter(lambda x: x.startswith('b'), mevalar))
# print(mevalar_b)