def calcular_dimension(ratio, dimension, es_ancho=True):
    # Separar el ratio en ancho y alto
    try:
        parte_ancho, parte_alto = map(float, ratio.split(':'))
    except ValueError:
        raise ValueError("El ratio debe tener el formato 'ancho:alto', como '16:9' o '4:3'.")

    if es_ancho:
        # Calcular altura en base al ancho
        altura = dimension * (parte_alto / parte_ancho)
        return round(dimension), round(altura)
    else:
        # Calcular ancho en base a la altura
        ancho = dimension * (parte_ancho / parte_alto)
        return round(ancho), round(dimension)

# Ejemplo de uso
if __name__ == "__main__":
    ratio_input = input("Ingresa el ratio de aspecto (ej: 5:2): ")
    dimension_input = float(input("Ingresa la dimensión conocida (en píxeles): "))
    tipo = input("¿Es esta dimensión el ancho o el alto? (escribe 'ancho' o 'alto'): ").strip().lower()

    if tipo not in ('ancho', 'alto'):
        print("Debes escribir 'ancho' o 'alto'.")
    else:
        es_ancho = tipo == 'ancho'
        ancho, alto = calcular_dimension(ratio_input, dimension_input, es_ancho)
        print(f"La imagen debe tener dimensiones: {ancho}px x {alto}px")