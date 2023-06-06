# Escribir un programa que sume todos los números enteros impares desde el 0 hasta el 100
# ----------------------------------------------------------------------------------------#

def sum(start, end):
    # seteo un sumador
    sum = 0
    # convierto a lista
    lista = list(range(start, end))
    for n in lista:
        # sumo solo los que son impares
        if n % 2 == 1: sum += n
    # retorno la suma
    return str(sum)

# mostrar resultado
print(sum(0,100))
