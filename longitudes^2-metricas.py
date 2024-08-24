print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

medida = input('mm - cm - m - km: ')
valor = float(input('Valor: '))
print('')


if medida == 'mm':
    print(f'{valor} mm^2 son {valor*0.01} cm^2')
    print(f'{valor} mm^2 son {valor*(10**-6)} m^2')
    print(f'{valor} mm^2 son {valor*(10**-12)} km^2')
    
if medida == 'cm':
    print(f'{valor} cm^2 son {valor*100} mm^2')
    print(f'{valor} cm^2 son {valor*(10**-4)} m^2')
    print(f'{valor} cm^2 son {valor*(10**-10)} km^2')
    
if medida == 'm':
    print(f'{valor} m^2 son {valor*(10**6)} mm^2')
    print(f'{valor} m^2 son {valor*(10000)} cm^2')
    print(f'{valor} m^2 son {valor*(10**-6)} km^2')
    
if medida == 'km':
    print(f'{valor} km^2 son {valor*(10**12)} mm^2')
    print(f'{valor} km^2 son {valor*(10**10)} cm^2')
    print(f'{valor} km^2 son {valor*(10**6)} m^2')