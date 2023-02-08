def main():
    # Se introduce el primer número
    num1 = int(input("Introduce el primer número: "))

    # Se introduce el segundo número
    num2 = int(input("Introduce el segundo número: "))

    # Se comprueba si el primer número es mayor que el segundo
    if num1 > num2:
        result = "El número más grande es {} y el más pequeño es {}".format(num1, num2)
    # Se ve si es el caso contrario
    elif num1 < num2:
        result = "El número más grande es {} y el más pequeño es {}".format(num2, num1)
    # Si los números son iguales
    else:
        result = "Los números son iguales."
    # Imprime el resultado
    print(result)
main()