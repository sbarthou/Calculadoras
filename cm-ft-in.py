import math

print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')


medida = input('cm - ft - in - ft+in: ')
if medida == 'ft+in':
    print('(Ingresar solo números enteros)')
    ft = int(input('ft: '))
    inch = int(input('in: '))
else: valor = float(input('Valor: '))
redondear = input('Redondear valores? (si/no): ')
if redondear == 'si':
    decimales = int(input('Número de decimales: '))
print('')


if medida == 'cm':
    if redondear == 'si':
        print(f'{valor} cm son {round(valor/30.48, decimales)} ft')
    else:
        print(f'{valor} cm son {valor/30.48} ft')
    if redondear == 'si':
        print(f'{valor} cm son {round(valor/2.54, decimales)} in')
    else:
        print(f'{valor} cm son {valor/2.54} in')
    if redondear == 'si':
        print(f'{valor} cm son {math.floor(valor/30.48)} ft y {round((valor%30.48)/2.54, decimales)} in ({math.floor(valor/30.48)}\'{round((valor%30.48)/2.54)}" aprox)')
    else:
        print(f'{valor} cm son {math.floor(valor/30.48)} ft y {(valor%30.48)/2.54} in ({math.floor(valor/30.48)}\'{round((valor%30.48)/2.54)}" aprox)')
        
        
if medida == 'ft':
    if redondear == 'si':
        print(f'{valor} ft son {round(valor*30.48, decimales)} cm')
    else:
        print(f'{valor} ft son {valor*30.48} cm')
    if redondear == 'si':
        print(f'{valor} ft son {round(valor*12, decimales)} in')
    else:
        print(f'{valor} ft son {valor*12} in')
    if valor != int(valor):
        if redondear == 'si':
            deci = valor - int(valor)
            print(f'{valor} ft son {math.floor(valor)} ft y {round(deci*12, decimales)} inches ({math.floor(valor)}\'{round(deci*12)}" aprox)')
        else:
            deci = valor - int(valor)
            print(f'{valor} ft son {math.floor(valor)} ft y {deci*12} inches ({math.floor(valor)}\'{round(deci*12)}" aprox)')
        
        
        
if medida == 'in':
    if redondear == 'si':
        print(f'{valor} in son {round(valor*2.54, decimales)} cm')
    else:
        print(f'{valor} in son {valor*2.54} cm')
    if redondear == 'si':
        print(f'{valor} in son {round(valor/12, decimales)} ft')
    else:
        print(f'{valor} in son {valor/12} ft')
    if redondear == 'si':
        print(f'{valor} in son {math.floor(valor/12)} ft y {round(valor%12, decimales)} inches ({math.floor(valor/12)}\'{round(valor%12)}" aprox)')
    else:
        print(f'{valor} in son {math.floor(valor/12)} ft y {valor%12} inches ({math.floor(valor/12)}\'{round(valor%12)}" aprox)')
        
        
if medida == 'ft+in':
    if redondear == 'si':
        print(f'{ft} ft y {inch} in ({ft}\'{inch}") son {round((ft*30.48 + inch*2.54), decimales)} cm')
    else:
        print(f'{ft} ft y {inch} in ({ft}\'{inch}") son {ft*30.48 + inch*2.54} cm')
    if redondear == 'si':
        print(f'{ft} ft y {inch} in ({ft}\'{inch}") son {round((ft + inch/12), decimales)} ft')
    else:
        print(f'{ft} ft y {inch} in ({ft}\'{inch}") son {ft + inch/12} ft')
    if redondear == 'si':
        print(f'{ft} ft y {inch} in ({ft}\'{inch}") son {round((ft*12 + inch), decimales)} in')
    else:
        print(f'{ft} ft y {inch} in ({ft}\'{inch}") son {ft*12 + inch} in')