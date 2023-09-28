print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

medida = input('g - kg - ton: ')
valor = float(input('Valor: '))
r = int(input('Número de decimales: '))
print('')

if medida == 'g':
    print(f'{valor} g/m son {round(valor/1000, r)} kg/m')
    print(f'{valor} g/m son {round(valor/1000000, r)} ton/m')
    
if medida == 'kg':
    print(f'{valor} kg/m son {round(valor*1000, r)} g/m')
    print(f'{valor} kg/m son {round(valor/1000, r)} ton/m')
    
if medida == 'ton':
    print(f'{valor} ton/m son {round(valor*1000000, r)} g/m')
    print(f'{valor} ton/m son {round(valor*1000, r)} kg/m')