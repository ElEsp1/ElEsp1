#1. Cree un script que, al ejecutarlo, le solicite al usuario ingresar su nombre de
#pila, luego lo salude y calcule la cantidad de letras del nombre, mostrando el
#mensaje “Hola, [NOMBRE], tu nombre tiene [N] letras.”.

nombre= input("ingrese su nombre de pila: ")
print(f"El nombre {nombre} tiene {len(nombre)} letras")


#***********************************************************************************************************************************************************************************#

#2. Cree un script que lea dos números enteros por teclado, y luego muestre en
#  pantalla el resultado de la suma entre ellos.

numero1 = input("ingrese el primer numero ")
numero2 = input("ingrese el segundo numero ")
resultado = int(numero1) + int(numero2)
print("La suma de ambos es:",resultado)


#***********************************************************************************************************************************************************************************#


#3. Cree un script que muestre en pantalla el perímetro de un rectángulo,
#leyendo su base y altura desde teclado.
#perímetro = 2 * (base + altura)

base = input("Ingrese la base del Rectagulo: ")
altura = input("Ingrese la Alutra del Rectangulo: ")
perimetro = 2 * (int(base) + int(altura))
print("el perimetro del rectangulo es ", perimetro)


#***********************************************************************************************************************************************************************************#


#4. Cree un script que le solicite a un alumno ingresar su apellido, la nota del
#primer parcial, y la nota del segundo parcial. Finalmente, se debe mostrar un
#reporte con la siguiente información:

alumno = input("Ingrese su Apellido: ")
parcial1 = input("Ingrese su nota del Primer Parcial: ")
parcial2 = input("Ingrese su nota del Segundo Parcial: ")
promedio = (int(parcial1) + int(parcial2)) /2
print("Alumno ",alumno,":")
print("- Primer Parcial: ",parcial1,".")
print("- Segundo Parcial: ",parcial2,".")
print("- Promedio: ", promedio)


#***********************************************************************************************************************************************************************************#


#5. Cree un script que lea dos números de teclado (una base y un exponente) y
#luego muestre en pantalla el resultado de elevar el número base a la
#potencia exponente.

base = input("Ingrese la base: ")
exponente = input("Ingrese el exponente: ")
resultado = int(base) ** int(exponente)
print(f"El resultado de {base} elevado a {exponente} es :{resultado}")


