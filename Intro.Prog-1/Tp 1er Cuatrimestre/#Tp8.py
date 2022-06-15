#1. Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
#usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
#el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
#para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.


palabra = ""
while (palabra != "parar"):
    palabra = input("Ingrese la palabra: ")
    if (palabra != "parar"):
        print (f"La palabra ingresada es {palabra}")
print ("--- TERMINADO ---")

    

#2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
#hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
#cargar. Una vez ingresadas las notas, el programa debe informar la nota
#promedio (tenga cuidado de no incluir al -1 dentro del promedio).

notas = 0
contador = 0
suma = 0
while (notas != -1):
    suma = suma + notas
    notas = int(input ("Ingrese la nota del parcial: "))
    if (notas != -1):
        contador += 1
suma = suma/contador
print (f"El promedio de las notas ingresadas es {suma}")


#3. Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
#programa debe ser capaz de solicitarle al usuario que reingrese el número
#cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
#vez que detecte un error de validación, informele al usuario cuál fue el error, con
#los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
#fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
#válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.


numero = False
while (numero == False):
    dato = input("Ingrese un numero valido")
    if ( dato.isalpha() ):
       print ("El dato ingresado no es numérico")
    elif ((int(dato) < 1) and (int(dato) > 100)):
       print ("El numero ingresado está fuera del rango permitido")
    if ((int(dato) > 1) and (int(dato) < 100)):
        numero = True
print (f"{numero} es válido, Gracias!")


#4. Construya un menú que le muestre al usuario lo siguiente:
#********* MI PROGRAMA *********
#1. Saludar.
#2. Informar temperatura.
#3. Mostrar nombre de materia.
#4. Salir.
#Seleccione una opción [1-4]:
#● - Cuando el usuario ingrese la opción 1, se mostrará el mensaje:
#“Hola, bienvenido a mi programa interactivo!”.
#● - Cuando el usuario ingrese la opción 2, se mostrará el mensaje
#“Hay una sensación térmica de 20 grados Celsius.”.
#● - Cuando el usuario ingrese la opción 3, se mostrará el mensaje
#“Estás en la materia Introducción a la Programación!”.
#● - Cuando el usuario ingrese la opción 4, el programa debe terminar,
#mostrando el mensaje “Hasta la próxima!”.
#● - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
#inválida.”.
#Tip 1: crear al menos una función propia, que se encargue exclusivamente
#de mostrar el menú de opciones en pantalla.
#Tip 2: puede utilizar la instrucción os.system('cls') para limpiar la
#pantalla antes de volver a mostrar el menú. De esta manera su programa
#será más legible en la terminal. Para poder utilizar dicha instrucción
#deberá importar, al principio del script, la librería os de la siguiente
#manera:

#import os
# su código

#Tip 3: antes de limpiar la pantalla y volver a mostrar el menú, puede
#esperar a que el usuario confirme que ha terminado de leer la información
#presentada, simplemente utilizando la función

#input(‘PRESIONE ENTER PARA CONTINUAR’).

import os 
dato = 0
while (dato != 4):
   os.system('cls')
   print("********* MI PROGRAMA *********")
   print("1. Saludar.")
   print("2. Informar temperatura.")
   print("3. Mostrar nombre de materia.")
   print("4. Salir.")
   dato = int(input())
   os.system('cls')
   if (dato == 1):
      print("Hola, bienvenido a mi programa interactivo!")
   elif (dato == 2):
      print("Hay una sensación térmica de 20 grados Celsius.")
   elif (dato == 3):
      print("Estás en la materia Introducción a la Programación!")
   elif (dato == 4):
      print(" ")
   else:
      print ("Opción inválida.")
   if (dato != 4):
      print(" ")
      print(" ")
      print(" ")
      aux = input("Presione Enter para continuar")
print ("Hasta la próxima!")



#5. Si bien el while es útil cuando desconocemos la cantidad de veces que
#repetiremos un bloque de instrucciones, también puede ser utilizado en los
#mismos casos que es utilizado el for (aunque la inversa no es verdadera).
#Rehaga todos los ejercicios del Trabajo Práctico VII utilizando un while en
#lugar de un for.


#1. Cree un script para mostrar los primeros 100 números enteros positivos,
#comenzando desde el 1.

numero = 1
while (numero != 101):
   print (f"{numero}")
   numero += 1

#2. Modifique el script del ejercicio anterior para que se muestren sólo los números
#pares. Para saber si un número es par, utilice el operador de módulo (%).

numero = 2
while (numero != 102):
   print (f"{numero}")
   numero += 2

#3. Cree un script para calcular el resultado de sumar los números desde el 75 al
#150.

numero = 75
suma = 0 
while (numero != 151):
   suma = numero + suma 
   numero += 1
print (f"El resultado es : {suma}")

#4. Cree un script que le solicite al usuario ingresar un número entero, y muestre
#en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
#este ejercicio, pero recuerde que la función range no incluye al valor máximo
#enviado como parámetro.
#factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n

numero = int(input("Ingrese el numero a factorizar "))
resultado = 1
contador = 1
flag = True
while (flag):
   resultado = resultado * contador
   contador += 1
   if (numero+1 == contador):
      flag = False
print (f"El factorial del numero ingresdo es: {resultado}")

#5. Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
#uno, informarle si el mismo es positivo, negativo, o cero.


contador = 0
while (contador != 10):
    numero = int(input("Ingrese el numero a averiguar"))
    if (numero==0):
        print("El número es igual a 0")
    elif((numero%2)==0):
        print("El número ingresado es Par")
    else:
        print("El número ingresado es Impar")
    contador += 1

#6. Cree un script que le solicite al usuario ingresar 10 números, y una vez
#ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
#ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
#y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
#ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

posicion = 0
mayor = 0
contador = 0
while (contador != 10):
    numero = int(input("Ingrese Los Números "))
    posicion +=1
    if (numero > mayor):
        mayor = numero 
        r_pos = posicion
    contador += 1
print (f"El mayor número ingresado es {mayor}, y lo ingresaste en la posición {r_pos}")


#7. Extienda el script del ejercicio anterior para que también informe el número
#mínimo ingresado, y su posición.

posicion = 0
mayor = 0
menor = 0
contador = 0
while (contador != 10):
    numero = int(input("Ingrese Los Números "))
    posicion +=1
    if (numero > mayor):
        mayor = numero 
        r_pos = posicion
    if (numero < menor):
        menor = numero 
        r_men_pos = posicion
    contador += 1
print (f"El mayor número ingresado es {mayor}, y lo ingresaste en la posición {r_pos}")
print (f"El menor número ingresado es {menor}, y lo ingresaste en la posición {r_men_pos}")


#8. Un cliente ha solicitado un programa que le permita ingresar los mililitros de
#lluvia caídos diariamente en una semana, para que el programa le informe en
#pantalla el promedio de precipitación de esa semana. El cliente también desea
#saber cuál fue el día en que más llovió en la semana.
#A modo ilustrativo, un reporte generado por el programa debería verse como
#sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
#El promedio de precipitaciones fue de XX mls. diarios.
#El día de más precipitaciones fue el xxxxxx (nombre del día).
#Tenga en cuenta que la numeración de los días de la semana comienza con el 1
#para el día domingo.
#Codifique el programa para dar solución a lo solicitado por el cliente.

posicion = 0
mayor = 0
contador = 0
while (contador != 7):
    numero = int(input("Ingrese Las precipitaciones del día "))
    posicion +=1
    if (numero > mayor):
        mayor = numero 
        r_pos = posicion
    contador += 1
if (r_pos==2):
    r = "Lunes"
elif (r_pos==3):
    r = "Martes"
elif (r_pos==4):
    r = "Miercoles"
elif (r_pos==5):
    r = "Jueves"
elif (r_pos==6):
    r = "Viernes"
elif (r_pos==7):
    r = "Sábado"
elif (r_pos==1):
    r = "Domingo"
print("Luego de haber leído las precipitaciones de los 7 días de la semana")
print(f"El promedio de precipitaciones fue de {mayor} mls. diarios")
print(f"El día de más precipitaciones fue el {r} (nombre del día)")





