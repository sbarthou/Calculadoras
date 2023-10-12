import math

print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

opcion = int(input('Calcular hipotenusa (1) o cateto (2): '))

if opcion == 1:
    cat1 = float(input('Cateto 1: '))
    cat2 = float(input('Cateto 2: '))
elif opcion == 2:
    cat = float(input('Cateto: '))
    hip = float(input('Hipotenusa: '))
else: 
    print('Opcion no valida')

redondear = input('Redondear valores? si(s)/no(n): ')
if redondear == 's' or redondear == 'si':
    decimales = int(input('Número de decimales: '))
print('')

if opcion == 1:
    hip = math.hypot(cat1, cat2)
    if redondear == 'si':
        print(f'Hipotenusa: {round(hip, decimales)}')
    else:
        print(f'Hipotenusa: {hip}')
elif opcion == 2:
    cateto = math.sqrt(hip**2 - cat**2)
    if redondear == 'si':
        print(f'Cateto: {round(cateto, decimales)}')
    else:
        print(f'Cateto: {cateto}')