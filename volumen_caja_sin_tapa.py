# Volumen máximo con área superficial dada.

from sympy import *
import math

area = int(input("Área superficial: "))
cara = input("Tiene base rectangular y dos caras cuadradas? (y/n): ")
print('------------------------------------------------------')

x, y, z, l = symbols('x y z l')

if cara == 'y':
    b = (area - 2*x**2)/3*x
    v = (area/3)*x - (2*x**3)/3
    v_diff = diff(v, x)
    raiz_x = solve(v_diff)[1]
    V = v.subs(x, raiz_x)
    raiz_y = solve(raiz_x**2 * y - V)[0]

    print(f'Volumen máximo: {round(V, 2)} unidades cúbicas.\nx = {round(raiz_x, 2)}, y = {round(raiz_y, 2)}')
    
    
if cara == 'n':
    eq1 = Eq(y*z, l*(y + 2*z))
    eq2 = Eq(x*z, l*(x + 2*z))
    eq3 = Eq(x*y, l*(2*y + 2*x))
    eq4 = Eq(x*y + 2*x*z + 2*y*z - area, 0)
    sol = solve([eq1, eq2, eq3, eq4], (x, y, z, l))

    result = list(sol[1])
    result.pop(-1)
    V = N(math.prod(result))
    
    print(f'Volumen máximo: {round(V, 2)} unidades cúbicas.\nx = {round(N(result[0]), 2)}, y = {round(N(result[1]), 2)}, z = {round(N(result[2]), 2)}')