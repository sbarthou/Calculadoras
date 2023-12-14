print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

valor_i = float(input('Valor inicial: '))
valor_f = float(input('Valor final: '))
print('')

# aumento
if valor_i < valor_f:
    aumento = ((valor_f - valor_i) / valor_i) * 100
    print(f'{valor_i} ➞ {valor_f} | + {round(aumento, 2)}%')
elif valor_i > valor_f:
    disminucion = ((valor_i - valor_f) / valor_i) * 100
    print(f'{valor_i} ➞ {valor_f} | - {round(disminucion, 2)}%')