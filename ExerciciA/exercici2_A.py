# Función para saludar al usuario por su nombre y decirle cual es el significado de su nombre
def saluda_por_nombre():
    # Solicita el nombre del usuario
    nombre = input("Inserta tu nombre: ")
    # Lista de nombres conocidos
    nombres = ['Céline', 'Alfredo', 'Ivy', 'Alicia', 'Anna']
    # Verifica si el nombre introducido se encuentra en la lista de nombres conocidos
    if nombre in nombres:
        if nombre == 'Anna':
            result = "Hola {}! Tu nombre significa “llena de gracia”, “benéfica”, “compasiva”".format(nombre)
        elif nombre == 'Céline':
            result = "Hola {}!  Tu nombre es una forma femenina del romano caelestis que significa “celestial”".format(nombre)
        elif nombre == 'Alfredo':
            result = "Hola {}! Tu nombre significa “el que es aconsejado por los elfos” o “el aconsejado”.".format(nombre)
        elif nombre == 'Ivy':
            result = "Hola {}!  Tu nombre es de origen inglés, y su significado es “hiedra”.".format(nombre)
        else:
            result = "Hola {}! Tu nombre proviene del griego antiguo Αλήθεια (alétheia), que significa ”verdad”.".format(nombre)
    # En caso de que el nombre no se encuentre en la lista de nombres conocidos
    else:
        result = "Este nombre no está en la lista."
    print(result)
saluda_por_nombre()

