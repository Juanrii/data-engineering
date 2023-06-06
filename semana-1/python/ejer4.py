# Dadas dos listas (las que se quiera crear), generar una tercera 
# con los elementos que estén presentes en AMBAS listas. 
# Retornar esta nueva lista pero sin elementos duplicados.
# ----------------------------------------------------------------#

def convertStringToList(str):
    # sepearamos por espacios
    lista = str.split()
    # Se convierten a enteros
    return [int(n) for n in lista]

def obtenerInterseccion(lista1, lista2):
    # Se crean dos conjuntos y se busca la interseccion (&) de ambos
    # Se convierte a una lista
    return list(set(lista1) & set(lista2))

# Ingreso de listas
lista1 = input("Ingrese una lista de numeros separadas por espacios: ")
lista2 = input("Ingrese la segunda lista: ")

# Conversion de strings a listas
lista1 = convertStringToList(lista1)
lista2 = convertStringToList(lista2)

# Guardo la lista final con los valores que coiniciden en ambas
listaFinal = obtenerInterseccion(lista1, lista2)

# Mostrar el resultado
print('La lista resultante es: ' + str(listaFinal))