def calcular_alfa_hex(porcentaje):
    # Convertir el porcentaje a un valor entre 0 y 255
    valor_alfa = int(porcentaje / 100 * 255)

    # Convertir el valor a formato hexadecimal y asegurarse de que tenga dos dígitos
    alfa_hex = format(valor_alfa, "02X")

    return alfa_hex


print("Ingrese solo enteros")
porcentaje = int(input("Porcentaje: "))
print('---------------')
alfa_hex = calcular_alfa_hex(porcentaje)

print(f"{porcentaje}% ➞ {alfa_hex} en\x1B[3m hex\x1B[0m")