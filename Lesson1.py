# print("1st lesson")
# car_0 = {'model':'Ferrari', 'rang':'qizil'}
# print(car_0)
# print(car_0['model'])
# print(car_0['rang'])
#
# en_uz = {'apple':'olma', 'appricot':'urik', 'banana':'banan'}
# suz = en_uz.get('appl', 'Bunday suz yuq lug\'atda')
# print(en_uz.keys())
# # for key, value in en_uz.items():
#     print(f"Kalit {key}")
#     print(f"Qiymat {value}")
#
# mahsulotlar = {
# 'olma':1000,
# 'anor':2000,
# 'uzum':4000,
# 'anjir':25000,
# 'shaftoli':30000}
# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# print(mahsulotlar)
# for mahsulot in mahsulotlar :
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olibkeling")

# NESTING
car0 = {
    'model':'lacetty',
    'rang' : 'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomat'
}

car1 = {
    'model':'nexia3',
    'rang' : 'qora',
    'yil':2015,
    'narh':9000,
    'km':89000,
    'korobka':'mexanik'
}

car2 = {
    'model':'gentra',
    'rang' : 'qizil',
    'yil':2019,
    'narh':11000,
    'km':8900,
    'korobka':'mexanik'
}

# car = car1
# print(f"{car['model'].title()},"
#       f"{car['rang'].title()} rang,"
#       f"{car['yil']}-yil, {car['narh']}$"
#       )

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rang'].title()} rang,"
#           f"{car['yil']}-yil, {car['narh']}$"
#           )
# print(cars[0]['model'])

malibus =[]
for n in range(10):
    malibu={
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
    }
    malibus.append(malibu)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

for malibu in malibus[6:]:
    malibu['rang'] = 'sariq'
    malibu['korobka'] = 'mexanik'

for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=4000
    else: malibu['narh']=3500
print(malibus)