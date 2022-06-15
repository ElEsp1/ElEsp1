#Trabajo Práctico VI
#Estructura alternativa y operadores lógicos

#Para tomar decisiones dentro de un algoritmo utilizaremos la sentencia condicional if:
# ● if evalúa el resultado de una condición booleana, y ejecuta una porción de
#   código contenido en ella si el resultado es “verdadero” (true).
 
# ● La condición de la sentencia if puede estar compuesta por varias
#   subcondiciones; cada condición booleana se relaciona con los operadores
#   lógicos como conjunción (and) o la disyunción (or).
 
# ● Se puede especificar un código a ejecutar si la condición evaluada es “falsa”
#   (false), utilizando la sentencia else.
 
# ● Es posible anidar sentencias if y else de manera infinita.
 
# ● En varias ocasiones será útil incluir un nuevo if en la sentencia else. Python nos
#   permite abreviar esto escribiendo elif (condición):.
 
# ● Recordar que en Python la indentación es parte de la sintaxis; esto es muy
#   importante para saber qué instrucciones están dentro del bloque de un if, else, o
#   elif.

#1. Cree un script que le solicite al usuario ingresar un número por teclado, y
#luego le informe en pantalla si su número es mayor que 10; antes de finalizar
#e independientemente de lo que haya sucedido antes, el script mostrará un
#mensaje de despedida. Ejemplos de cómo debería verse la salida del script:
#  Número mayor que 10:
#  Tu número (N) es mayor que 10!
#  Saludos!
#  Número menor o igual que 10:
#  Saludos!

N=0
N = int(input("Ingrese el Número a evaluar: "))
if (N > 10):
    print(f"Tu Número {N} es mayor que 10!")
print("Nos re vimos!")




#2. Modifique el script anterior para que mantenga el funcionamiento, pero
#ahora, cuando el número no es mayor que 10, también se muestre un
#mensaje “Tu número (N) es menor o igual que 10!”.

N=0
N = int(input("Ingrese el Número a evaluar: "))
if (N > 10):
    print(f"Tu Número {N} es mayor que 10!")
else :
    print(f"Número menor o igual que 10, mal ahí")
print("Nos re vimos!")


#3. Cree un script que le solicite al usuario ingresar dos números por teclado, y
#luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
#de que los números sean iguales, y muestre un mensaje acorde.

N = 0
A = 0
N = int(input("Ingrese el primer Número: "))
A = int(input("Ingrese el segundo Número: "))
if (N > A):
    print(f"El Número {N} es mayor que {A}!")
if (N < A):
    print(f"El Número {N} es menor que {A}!")
if (N == A):
    print(f"Los numero son iguales")
print("Nos re vimos!")

#4. Cree un script que le solicite al usuario ingresar un número por teclado, y le
#informe con un mensaje si su número es positivo, negativo, o 0.

N = 0
N = int(input("Ingrese el Número: "))
if (N > 0):
    print(f"El Número {N} es Positivo!")
if (N < 0):
    print(f"El Número {N} es Negativo!")
if (N == 0):
    print(f"EL numero es Cero")
print("Nos re vimos!")

#5. Cree un script que, dado un número de día de la semana ingresado por
#teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
#números y días de la semana es la siguiente:
#  1 = Domingo.
#  2 = Lunes.
#  3 = Martes.
#  4 = Miércoles.
#  5 = Jueves.
#  6 = Viernes.
#  7 = Sábado.

N = 0
N = int(input("Ingrese el Número: "))
if (N == 1):
    print(f"Es Domingo")
if (N == 2):
    print(f"Es Lunes")
if (N == 3):
    print(f"Es Martes")
if (N == 4):
    print(f"Es Miercoles")
if (N == 5):
    print(f"Es Jueves")
if (N == 6):
    print(f"Es Viernes")
if (N == 7):
    print(f"Es Sábado")

print("Nos re vimos!")

#6. Cree un script que le solicite a un alumno de la asignatura Introducción a la
#Programación que ingrese las notas de sus dos parciales. Como resultado, se
#le debe informar al alumno su situación, junto con la nota promedio. Las
#reglas para saber la situación de un alumno son las siguientes:

# ● Para estar promovido (es decir, cursada aprobada y no requiere
#   rendir final), el alumno debe haber aprobado ambos parciales y
#   tener un promedio mayor o igual a 8.
# ● Para estar regular (cursada aprobada, pero debe rendir final), el
#   alumno debe haber aprobado ambos parciales (nota mayor o igual
#   a 4).
# ● Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
#   menor que 4 en alguno de ellos), entonces queda en condición de
#   libre (es decir, puede rendir un final extendido o recursar).

N = 0
A = 0
N = int(input("Ingrese la primer Nota: "))
A = int(input("Ingrese la segunda Nota: "))
P = (N + A) / 2 
print (f"Tu promedio es {P}")
if (P > 7 ):
    print(f"Promoviste!")
if (P < 8) and (P > 3):
    print(f"Tu condiciones es Regular")
if (P < 4):
    print(f"Tu condición es Libre")
print("Nos re vimos!")


#7. Cree un script que determine si un triángulo es isósceles, equilátero, o
#escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
#números, correspondientes a los tres lados del triángulo.
#equilátero = todos los lados iguales
#isósceles = dos lados iguales
#escaleno = todos los lados diferentes

N = 0
A = 0
R = 0
Z = 0
N = int(input("Ingrese el primer Número: "))
A = int(input("Ingrese el segundo Número: "))
R = int(input("Ingrese el tercer Número: "))

if (N == A == R):
    print(f"El triangulo es equilátero!")
if (N == A != R ) or (N != A == R ) or (R != N == A ):
    print(f"El triangulo es isósceles!")
if (N != A != R):
    print(f"El triangulo es escaleno")
print("Sos groso rey!")

#8. Las estructuras alternativas pueden utilizarse para validar datos. Por
#ejemplo, si se intenta crear una función que tome dos enteros como
#parámetro y muestre el resultado de su división, puede ocurrir un error si el
#denominador es cero. Utilice la estructura alternativa para validar que el
#denominador no sea cero; en caso de serlo, la función deberá mostrar el
#mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
#resultado.

numero = 0
divisor = 0
resultado = 0
numero = int(input("Ingrese el Número a Dividir: "))
divisor = int(input("Ingrese el Divisor: "))
if (divisor < 1):
    print(f"No se puede dividir por 0!")
if (divisor > 0):
    respuesta = (numero / divisor)
    print(f"El Resultado de la division es {respuesta}!")
print("Joyita")

#9. Python ofrece algunas funciones built-in para facilitar la implementación de
#validaciones. A continuación se listan algunas de las más comunes:
#valor.isdigit()
#Retorna True si todos los caracteres de valor son numéricos, False en caso
#contrario.
#valor.isalpha()
#Retorna True si todos los caracteres de valor son alfabéticos (no
#numéricos), False en caso contrario.
#valor.isalnum()
#Retorna True si valor es una combinación alfanumérica (caracteres y
#números), False en caso contrario.
#Codifique una función que reciba un parámetro cualquiera proveniente del
#usuario del programa (que puede contener letras, números, o una combinación
#de ambas), e indique si el mismo es un número, una palabra, o un valor
#alfanumérico. Compruebe que su función resuelve el problema enviándole
#valores correspondientes a las tres posibilidades.

N = input("Ingrese la combinación: ")
A = 0

if ( N.isdigit() ):
    print(f"Los caracteres son numericos")
    A = 1
if ( N.isalpha() ):
    print(f"Los caracteres")
    A = 1
if  (N.isalnum() and (A == 0) ):
    print(f"Los caracteres son alfanumericos")

print("Sos groso rey!")

