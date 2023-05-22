print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

medida = input('mm - cm - m - km: ')
valor = float(input('Valor: '))
print('')


if medida == 'mm':
    print(f'{valor} mm^4 son {valor*(10**-4)} cm^4')
    print(f'{valor} mm^4 son {valor*(10**-12)} m^4')
    print(f'{valor} mm^4 son {valor*(10**-24)} km^4')
    
if medida == 'cm':
    print(f'{valor} cm^4 son {valor*10000} mm^4')
    print(f'{valor} cm^4 son {valor*(10**-8)} m^4')
    print(f'{valor} cm^4 son {valor*(10**-20)} km^4')
    
if medida == 'm':
    print(f'{valor} m^4 son {valor*(10**12)} mm^4')
    print(f'{valor} m^4 son {valor*(10**8)} cm^4')
    print(f'{valor} m^4 son {valor*(10**-12)} km^4')
    
if medida == 'km':
    print(f'{valor} km^4 son {valor*(10**24)} mm^4')
    print(f'{valor} km^4 son {valor*(10**20)} cm^4')
    print(f'{valor} km^4 son {valor*(10**12)} m^4')