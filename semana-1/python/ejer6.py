# Contar cuantas veces aparece un elemento en una lista
# ------------------------------------------------------#

# Reutilizo funcion del ejer4
def convertStringToList(str):
    lista = str.split()
    return [n for n in lista]

# Pedir una lista
lista = input("Ingrese una lista de elementos separados por espacio: ")
# Pedir el elemento a contar
objetivo = input("Ingrese el elemento a buscar: ")

# Convertir a lista lo que ingreso
lista = convertStringToList(lista)

# Cantidad de veces
x = str(lista.count(objetivo))

# Mostrar el resultado
print('El elemento: ' + objetivo + ' aparece ' + x + ' veces en la lista')