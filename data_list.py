#Bacis Data Type
brand1 = 'Toyota'
brand2 = 'Honda'
brand3 = 'BMW'
brand4 = 'Mercedes'
brand5 = 'Ferrari'


print(brand1)
print(brand2)
print(brand3)
print(brand4)
print(brand5)

#data list 
brand = ['Toyota', 'Honda', 'BMW', 'Mercedes', 'Ferrari']
print(brand)
brand.append('Mclearn')
print(brand)

#print brand 2
print(f'Car {brand[2]}!')

print('\n All Car')
for a in brand:
    print(f'merk {a}!')

print('\n All Car : Automotive')
for a in range (0, len(brand)):
    print(f'{a}. Merk {brand[a]}!')
    