import numpy as np

rango = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

def y(x):
    return 0.8504*x + 0.4733

def I(T, H):
    return (T*0.031*9.8*0.0196)/(16*(np.pi**2)*H)

# I = ((0.349**2) * 0.28 * (0.18**2)) / (16 * (np.pi**2) * 0.675)

print(I(0.9401, 0.685))
print(0.031*0.0196/12)
