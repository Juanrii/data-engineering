# Escribir un programa que pida al usuario cuántos números quiere introducir. 
# Luego que lea todos los números y realice una media aritmética.
# -------------------------------------------------------------------------- #

# Leer cantinad de numeros
numbers = int(input('Cuantos numeros quiere ingresar?: '));

# Variable sumador
sum = 0

# Acumulo en sum el ingreso de los numeros
for n in range(numbers):
    sum += int(input(str(n + 1) + " - Ingrese un numero: "))

# Divido la suma total por la cantidad de numeros
# Media Aritmetica = (x1 + x2 + xN) / N
media = float(sum / numbers)

# Muestro el resultado
print('La media aritmetica de los '+ str(numbers)+ ' numeros ingresados es: ' + str(media))