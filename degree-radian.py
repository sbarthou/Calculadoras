# Calculadora para transformar grados a radianes y biseversa

import math
from fractions import Fraction

print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

medida = int(input('Grados (0) - Radianes (1): '))
angulo = float(input('Ángulo: '))

redondear = input('Redondear valores? si(s)/no(n): ')
if redondear == 's' or redondear == 'si':
    redondear = 'si'
    decimales = int(input('Número de decimales: '))
print('')
    

if medida == 0:
    angulo = int(angulo)
    frac = Fraction(angulo, 180)
    rad = (math.pi/180)*angulo
    if redondear == 'si':
        print(f'{angulo}° son π({frac}) = {round(rad, decimales)} rad')
    else:
        print(f'{angulo}° son π({frac}) = {rad} rad')
elif medida == 1:
    gra = (180/math.pi)*angulo
    if redondear == 'si':
        print(f'{angulo} rad son {round(gra, decimales)}°')
    else:
        print(f'{angulo} rad son {gra}°')