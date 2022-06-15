#Tp1
#Ejercicio 1
#N = 3+4 
print(f"hola mundo",N)
#***********************************************************************************************************************************************************************************#
#Ejercicio de prueba clase 16/3

A = 10 
B = 7 
A = B + A 
B = A - B 
A = A - B 
print(A , B)

#***********************************************************************************************************************************************************************************#

#Cree un nuevo script llamado pruebas.py, y luego copie y pegue el siguiente
#contenido:
#  **Respuesta** el error está en la primer linea (mi caso linea 17) donde la fucnion "print" está mal escrita

pint('Esto es una prueba')
print(10 - 1)

#***********************************************************************************************************************************************************************************#

#Un colega programador nos ha proporcionado un script que resuelve la
#multiplicación de dos números y muestra el resultado en pantalla; el
#contenido del script es el siguiente:

numero1 = 10
numero2 = 5
resultado = numero1 * numero2
print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado))

#Ejecute el código para verificar el funcionamiento del script, y luego analice
#detenidamente el código y responda:
#- ¿Qué son numero1, numero2, y resultado? ** Respuesta ** los 3 anteriormente mensionados son las varibales a utilizar en el programa donde se almacenan los datos
#- ¿Por qué es necesario utilizar la función str(...) para mostrar en pantalla los
#valores de numero1, numero2, y resultado?  **Respuesta** la funcino "str" castea los datos de las funciones a utilizar para que todas sean de tipo string ya que print(f) sólo púede sumar ese tipo de dato.

#***********************************************************************************************************************************************************************************#

#Ejercicio 6
#Cree un script llamado mi_nombre.py, el cual almacene su nombre completo

nombre_completo = "Elias Espindola"

#***********************************************************************************************************************************************************************************#

#Modifique el código del ejercicio anterior para que el nombre se almacene en
#una variable, y el apellido en otra. Además, introduzca una tercera variable
#para almacenar su edad. Ahora, en pantalla muestre el mensaje “Mi nombre
#completo es [NOMBRE] [APELLIDO] y tengo [EDAD] años.”.

nombre = "Elias"

apellido = "Espindola"

edad = "21"

print(f"Mi nombre completo es {nombre} {apellido} y tengo {edad} años")

#***********************************************************************************************************************************************************************************#

#Cree un script llamado numero_favorito.py, y almacene su número favorito en
#una variable. Luego muestre en pantalla el mensaje “Mi número favorito es
#[N]”.

numero_favorito = 8

print("Mi numero favorito es#",numero_favorito)

#***********************************************************************************************************************************************************************************#
#Se le ha solicitado a dos programadores que resuelvan el mismo problema:
#conociendo el total de inscriptos de una asignatura y cuántos alumnos han
#asistido a la clase de hoy, queremos un programa que nos muestre en
#pantalla el porcentaje de asistencia del día de hoy. Las dos versiones que
#realizaron los programadores son:

   #Programador A
   # almaceno cuántos alumnos asistieron a la clase de hoy
alumnos_presentes = 35
   # almaceno el total de inscriptos en la asignatura
alumnos_inscriptos = 54
   # calculo del porcentaje de alumnos presentes en la clase de hoy
porcentaje_presentes = (alumnos_presentes * 100) / alumnos_inscriptos
   # muestro el porcentaje calculado en pantalla
print('Hoy asistió el ' + str(porcentaje_presentes) + ' porciento del alumnado.')
   
   # Programador B
p = 35
i = 54
pp = (p * 100) / i
print('Hoy asistió el ' + str(pp) + ' % del alumnado.')

   #Analice detenidamente ambas versiones, y luego responda:
   #- ¿Ambas versiones resuelven el problema?. si, ambos lo hacen.
   #- ¿Cuál versión es más legible y fácil de comprender?. son iguales, la diferencia está en cómo cada uno interprete las variables, por lo tanto son iguales de comprender.
   #- ¿Qué desventajas tiene escribir código en la forma en que lo hace el
   #Programador B?. depende de quién les la precentación puede llegar a ser dificil entender a qué refiere con las abreviaturas de las variables.


 




