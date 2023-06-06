# Escribir un programa que lea un número impar por teclado. 
# Si el usuario no introduce un número impar, debe repetirse 
# el proceso hasta que lo introduzca correctamente.
# ----------------------------------------------------------- #

# leer numero impar y parsearlo a entero
num = int(input('Ingrese un numero impar por favor: '));

# mientras el resto sea 0, vuelvo a pedir el numero
while num % 2 == 0:
    num = int(input(str(num) + ' es par. Ingrese un numero impar por favor: '));

# muestro el numero impar
print('El numero ' + str(num) + ' es impar. Gracias')