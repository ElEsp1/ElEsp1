import os
#1. Cree un script que le solicite al usuario ingresar una temperatura en grados
#   Celsius, y valide que la entrada es correcta, teniendo en cuenta que la
#   temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El
#   programa debe permitir reingresar el dato cuantas veces sea necesario, hasta
#   que el usuario provea un dato válido. Procure informar al usuario cuando su
#   dato es inválido, y cuáles son los valores aceptados.

os.system('cls')
val = True
aviso = 0
while val:
    os.system('cls')
    if (aviso >= 2):
        os.system('cls')
        print("Recuerde que el dato a ingresar debe ser numerico!!!")
        print("Además debe estar dentro de los valores -18° y 50°")
    temp = int(input("Ingrese la Temperatura: "))
    if (type(temp) == int) and (temp > -18) and (temp < 50):
        os.system("cls")
        print ("El dato ingresado es correcto, felicidades")
        print (" ")
        input("Presiona Enter para continuar...")
        aviso += 1
        val = False
    else:
        os.system("cls")
        print ("El dato ingresado es incorrecto o está fuera de los parametros, Por favor intente nuevamente...")
        print (" ")
        input("Presiona Enter para continuar...")
        aviso += 1


#2. Cree un script que le solicite al usuario ingresar su edad. Verifique que el dato
#   ingresado sea válido, teniendo en cuenta que la edad es un número entero, y el
#   rango válido para este programa es de 18 a 60 años. El programa debe solicitar
#   el reingreso de manera indefinida, hasta que el dato sea correcto.

os.system('cls')
val = True
aviso = 0
while val:
    os.system('cls')
    if (aviso >= 1):
        os.system('cls')
        print("Recuerde que el dato a ingresar debe ser numerico!!!")
        print("Además debe ser mayor de 18 años y menor de 60.")
        print(" ")
    edad = int(input("Ingrese su edad: "))
    if (type(edad) == int) and (edad > 18) and (edad < 60):
        os.system("cls")
        print ("El dato ingresado es correcto, felicidades")
        print (" ")
        input("Presiona Enter para continuar...")
        aviso += 1
        val = False
    else:
        os.system("cls")
        print ("El dato ingresado es incorrecto o está fuera de los parametros, Por favor intente nuevamente...")
        print (" ")
        input("Presiona Enter para continuar...")
        aviso += 1


#3. Modifique todos los ejercicios anteriores para que en lugar de permitir el
#   reintento de manera ilimitada, el programa permita sólo 10 reintentos. Si el
#   usuario supera el límite de reintentos, el programa debe terminar con el
#   mensaje “Usted está jugando conmigo, yo me retiro”.

# Agregando ésta linea de comando dentro del if de comprobación obtenemos el resultado esperado
#elif (aviso > 9):
#    os.system("cls")
#    print("Usted está jugando conmigo, nos vimo en Diney ")
#    val = False

#4. La técnica de validación para un conjunto específico de valores se puede utilizar
#para construir menús de opciones. Construya un menú que le muestre al
#usuario lo siguiente:
#********* MI PROGRAMA *********
#1. Saludar.
#2. Informar temperatura.
#3. Mostrar nombre de materia.
#4. Salir.
#Seleccione una opción [1-4]:
#- Cuando el usuario ingrese la opción 1, se mostrará el mensaje “Hola,
#bienvenido a mi programa interactivo!”.
#- Cuando el usuario ingrese la opción 2, se mostrará el mensaje “Hay una
#sensación térmica de 20 grados Celsius.”.
#- Cuando el usuario ingrese la opción 3, se mostrará el mensaje “Estás en la
#materia Introducción a la Programación!”.
#- Cuando el usuario ingrese la opción 4, el programa debe terminar,
#mostrando el mensaje “Hasta la próxima!”.
#- Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
#inválida.”.

#import os 
#dato = 0
#val = True
#while val:
#   os.system('cls')
#   print("********* MI PROGRAMA *********")
#   print("1. Saludar.")
#   print("2. Informar temperatura.")
#   print("3. Mostrar nombre de materia.")
#   print("4. Salir.")
#   dato = input()
#   os.system('cls')
#   if (dato == "1"):
#      print("Hola, bienvenido a mi programa interactivo!")
#   elif (dato == "2"):
#      print("Hay una sensación térmica de 20 grados Celsius.")
#   elif (dato == "3"):
#      print("Estás en la materia Introducción a la Programación!")
#   elif (dato == "4"):
#      print(" ")
#      val = False
#   else:
#      print ("Opción inválida.")
#   if (dato != "4"):
#      print(" ")
#      print(" ")
#      print(" ")
#      aux = input("Presione Enter para continuar")
#print ("Hasta la próxima!")

#5. Cree un script que le solicite al usuario ingresar cuál es su color favorito,
#limitando las opciones a rojo, verde, y azul. Aclaraciones:
#- Puede asumir que el usuario ingresará los strings en minúsculas.
#Opcionalmente, puede investigar el uso de las funciones upper() y lower()
#para transformar la entrada a mayúsculas o minúsculas y evitar así
#posibles errores de validación por este detalle.
#- Al validar entre un conjunto de opciones prefijadas (en lugar de hacerlo en
#un rango), es posible que no sea necesario validar el tipo del dato
#ingresado por teclado.
#- Al detectar un dato inválido, el programa debe darle las siguientes
#opciones al usuario:
#** DATO INVÁLIDO **
#1. Reintentar.
#2. Salir.
#- La opción 1. Reintentar le permite al usuario reingresar el dato de manera
#indefinida, siempre mostrando las opciones ante cada intento fallido.
#- La opción 2. Salir finaliza el programa.

intento = 0
menu = True
while menu:
    os.system("cls")
    color = input("Ingrese su color favorito:")
    if color.isalpha:
       if (color != "rojo") and (color != "azul") and (color != "verde"):
           sub = True
           while sub:
              os.system("cls")
              color = "invalido"
              print("** DATO INVÁLIDO **")
              print(" /n 1. Reintentar /n 2. Salir")
              menu = input()
              if menu == "1":
                  menu = True
                  sub = False
              elif menu == "2":
                  menu = False
                  sub = False
              else:
                  print ("Ingrese un dato válido.")
                  input (" /n /n Presione cualquier tecla para continuar...")
                  sub = True
       else:
            menu = False




#6. Al implementar programas interactivos, es normal que la pantalla se llene de
#texto, en detrimento de la experiencia de usuario. Para solucionar este
#inconveniente, Python nos provee una función para limpiar la pantalla (notar
#que esto no tendrá ningún efecto sobre la lógica del programa, simplemente
#dejará la terminal de comandos en blanco). El uso de esta función depende del
#sistema operativo que esté utilizando, pero para empezar deberá importar el
#módulo os, escribiendo la siguiente línea al comienzo de su script:

#import os
#Una vez importado el módulo os, ya podrá utilizar la función para limpiar la
#pantalla en cualquier punto de su programa.
#● En Windows:
#os.system('cls')
#● En Linux:
#os.system('clear')
#Modifique todos los ejercicios de este TP para que cada vez que se reintente
#una entrada o se muestre un menú de opciones, la pantalla esté limpia.