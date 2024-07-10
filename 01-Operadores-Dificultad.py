# Creamos el bucle for en el rango entre el 10 y el 56
for numero in range(10,56):
    # Pedimos que compruebe que el número es divisible entre 2 y hacemos que no muestre números divisibles entre 3 y tampoco el número 16
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
