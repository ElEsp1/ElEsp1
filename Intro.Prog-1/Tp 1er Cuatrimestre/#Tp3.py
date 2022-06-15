# 1. Cree un script que almacene un número entero en una variable, y luego
#muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N
#es |N|”. Finalmente, verifique que su programa funciona correctamente,
#ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego
#con el valor -10 (la salida debería ser 10 nuevamente).

#N = -10
#print("El valor absoluto de N es", abs(N))

#***********************************************************************************************************************************************************************************#

#2. Cree un script que almacene su nombre de pila en una variable, y luego
#muestre en pantalla la cantidad de letras de ese nombre, con el mensaje “El
#nombre [NOMBRE] tiene [N] letras.”.

nombre = "Elias"
print(f"El nombre {nombre} tiene {len(nombre)} letras")

#***********************************************************************************************************************************************************************************#

#3. Cree un script que almacene, en dos variables, una base y un exponente, y
#luego muestre en pantalla el resultado de elevar el número base a la
#potencia exponente.

base = 14
exponente = 5
resultado = base ** exponente
print("el resultado es ", resultado)

#***********************************************************************************************************************************************************************************#

#4. Implemente un algoritmo en Python para calcular el perímetro de un
#rectángulo, conociendo su base y altura. Los datos se deben almacenar en
#variables, y el resultado se debe mostrar en pantalla.
#perímetro = 2 * (base + altura)

base = 13
altura = 25
perimetro = 2 * (base + altura)
print("el perimetro del rectangulo es ", perimetro)


#***********************************************************************************************************************************************************************************#

#5. Implemente un algoritmo en Python para calcular el área de un rectángulo,
#conociendo su base y altura. Los datos se deben almacenar en variables, y el
#resultado se debe mostrar en pantalla.
#área = base * altura

base = 13
altura = 25
area = base * altura
print("el perimetro del rectangulo es ", area)


#***********************************************************************************************************************************************************************************#

#6. Implemente un algoritmo que intercambie los valores entre dos variables a y b
#cualesquiera. Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la
#variable a debería ser igual 5, y la variable b debería ser igual a 10.

#opcion que se espera de nosotros

A = 10
B = 7
C = A 
A = B 
B = C
print(A, B)

#mejor opcion 

A = 10 
B = 7 
A = B + A 
B = A - B 
A = A - B 
print(A , B)


#***********************************************************************************************************************************************************************************#

#7. En Python es posible resolver el problema del intercambio de valores sin hacer
#uso de variables adicionales, mediante la sintaxis de asignación múltiple.
#Investigue de qué se trata dicha funcionalidad, y utilícela para resolver el
#ejercicio anterior sin usar variables auxiliares/adicionales.

A = 10
B = 7
A, B = B, A
print(A , B)


#***********************************************************************************************************************************************************************************#

#8. Escriba un algoritmo que, conociendo las notas de los dos parciales de un
#alumno de la asignatura Introducción a la Programación, muestre en
#pantalla su promedio.

parcial1 = 8
parcial2 = 9
promedio = (parcial1 + parcial2) / 2
print(promedio)


#***********************************************************************************************************************************************************************************#


#9. Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
#ahorrada en su cuenta (almacenando ese monto en una variable), muestre
#en pantalla los montos convertidos en dólares (U$1 = $102.5), reales ($R1 =
#$14.1), y euros (€1 = $104.5). La salida del programa debe tener el siguiente
#formato:

ahorros = 342552
dolares = ahorros / 102.5
reales = ahorros / 14.1
euros = ahorros / 104.5
print("Tus ahorros en pesos son $ "+str(ahorros))
print("conversion a Dolares U$D "+str(dolares))
print("conversion a Reales $R "+str(reales))
print("conversion a Euros € "+str(euros))






