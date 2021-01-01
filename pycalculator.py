# Calculadora en Python utilizando funciones simples por Brais Cuns Varela (MurkyCuns)

import math
import random

# Creamos la función que sume dos números:
def suma (num1, num2):
	return num1 + num2

# Creamos la función que reste dos números:
def resta (num1, num2):
	return num1 - num2

# Creamos la función que multiplique dos números:
def multiplicacion (num1, num2):
	return num1 * num2

# Creamos la función que divida dos números:
def division (num1, num2):
	return num1 / num2

def potencia (num1, num2):
	resultado = math.pow(num1, num2)
	return resultado

def logaritmo (num1, num2):
	resultado = math.log(num2, num1)
	return resultado

# Creamos un menú como interfaz de texto para el usuario:
print(" ")
print("---------- Bienvenido a la Calculadora de MurkyCuns ----------")
print(" ")
print("Lista de opciones disponibles:")
print(" ")
print("1.- Sumar")
print("2.- Restar")
print("3.- Multiplicar")
print("4.- Dividir")
print("5.- Potencia")
print("5.- Potencia")
print("6.- Logaritmo")
print(" ")
print("--------------------------------------------------------------")
print(" ")

while True:
	# Guardamos en una variable la opción escogida por el usuario:
	eleccion = input("Seleccione una opción indicando su número: ")

	# Comprobamos si la opción elegida se encuentra entre una de las 4 posibles:
	if eleccion in ('1', '2', '3', '4', '5', '6'):

		# Introducimos los números con los que operar:
		num1 = float(input("Introduzca el primer número: "))
		num2 = float(input("Introduzca el segundo número: "))

		# Comprobamos la elección escogida y realizamos la ejecución de los casos posibles:
		if eleccion == '1':
			print(num1, "+", num2, "=", suma(num1, num2))

		elif eleccion == '2':
			print(num1, "-", num2, "=", resta(num1, num2))

		elif eleccion == '3':
			print(num1, "*", num2, "=", multiplicacion(num1, num2))			

		elif eleccion == '4':
			print(num1, "/", num2, "=", division(num1, num2))

		elif eleccion == '5':
			print(num1, "^", num2, "=", potencia(num1, num2))

		elif eleccion == '6':
			print("El logaritmo en base ", num2, " de ", num1, " es: ", logaritmo(num1, num2))

		# Creamos una variable para conocer si el usuario desea continuar:
		continuar = input("¿Desea realizar otra operación? Introduzca 'Si' o 'No': ")

		# Comprobamos la elección introducida por el usuario:
		if continuar == 'Si':
			eleccion == False

		elif continuar == 'No':

			# Mostramos un mensaje de despedida al usuario si elige no realizar más operaciones:
			print("Ha sido un placer ayudarle con sus operaciones matemáticas. ¡Que tenga un gran día, tarde, noche, o lo que proceda!")
			
			break

	# Indicamos al usuario que si la opción introducida no corresponde con las anteriores, la opción introducida es errónea:
	else:
		print(" ")
		print("La opción previamente introducida no está entre las disponibles actualemente...")
		print(" ")