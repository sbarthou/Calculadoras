print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

print('Opciones:\n\n 1) Decimal a Binario\n 2) Binario a Decimal\n')
opcion = int(input('Ingrese una opción: '))


def decimal_a_binario(num):
    # Verificamos si el número es 0
    if num == 0:
        return '0'
    
    binario = []
    while num > 0:
        residuo = num % 2
        binario.append(str(residuo))
        num = num // 2
    
    # Invertimos la lista para obtener el binario en el orden correcto
    binario.reverse()
    
    # Unimos la lista en una cadena y la retornamos
    return ''.join(binario)


def binario_a_decimal(binario):
    # Inicializamos el valor decimal a 0
    decimal = 0
    
    # Recorremos cada dígito en el binario
    for digito in binario:
        # Multiplicamos el valor actual por 2 y añadimos el dígito actual
        decimal = decimal * 2 + int(digito)
    
    return decimal


if opcion == 1:
    num = int(input('Ingrese un número entero: '))
    print('')
    
    binario = decimal_a_binario(num)
    print(f'{num} en binario es {binario}')

if opcion == 2:
    num = str(input('Ingrese el número binario: '))
    print('')
    
    decimal = binario_a_decimal(num)
    print(f'{num} en decimal es {decimal}')