print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

medida = input('mm - cm - m - km: ')
valor = float(input('Valor: '))


if medida == 'mm':
    print(f'{valor} mm son {valor/10} cm')
    print(f'{valor} mm son {valor/1000} m')
    print(f'{valor} mm son {valor/1000000} km')
    
if medida == 'cm':
    print(f'{valor} cm son {valor*10} mm')
    print(f'{valor} cm son {valor/100} m')
    print(f'{valor} cm son {valor/100000} km')
    
if medida == 'm':
    print(f'{valor} m son {valor*1000} mm')
    print(f'{valor} m son {valor/100} cm')
    print(f'{valor} m son {valor/1000} km')
    
if medida == 'km':
    print(f'{valor} km son {valor*1000000} mm')
    print(f'{valor} km son {valor*100000} cm')
    print(f'{valor} km son {valor*1000} m')