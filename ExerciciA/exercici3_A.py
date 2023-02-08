# Función para adivinar un número, dando pistas sobre si es más grande o más pequeño

import random

def adivina_el_numero():
    # Establece el rango entre 0 y 100
    numero_aleatorio = random.randrange(0, 100)
    adivinanza = int(input("Adivina un número entre 0 y 100: "))
    while adivinanza != numero_aleatorio:
        if adivinanza > numero_aleatorio:
            print("El número es más pequeño.")
            adivinanza = int(input("Adivina otro número: "))
        else:
            print("El número es más grande.")
            adivinanza = int(input("Adivina otro número: "))
    print("¡Muy bien! ¡Has adivinado el número! Era el {}".format(numero_aleatorio))

adivina_el_numero()
