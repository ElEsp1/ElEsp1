#1. Cree un script para mostrar los primeros 100 números enteros positivos,
#comenzando desde el 1.

for i in range (1,101):
    print(i)

#2. Modifique el script del ejercicio anterior para que se muestren sólo los números
#pares. Para saber si un número es par, utilice el operador de módulo (%).

for i in range (1,101,2):
    if ((i%2)==0):
        print(i)

#3. Cree un script para calcular el resultado de sumar los números desde el 75 al
#150.

resultado = 0
for i in range (75,151):
    resultado = resultado + i
print (resultado)

#4. Cree un script que le solicite al usuario ingresar un número entero, y muestre
#en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
#este ejercicio, pero recuerde que la función range no incluye al valor máximo
#enviado como parámetro.
#factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n

numero = int(input("Ingrese el numero a factorizar"))
mult=1
for i in range (1,numero):
    mult = mult * i 
resultado = mult * numero
print (resultado)

#5. Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
#uno, informarle si el mismo es positivo, negativo, o cero.

for i in range (0,10):
    numero = int(input("Ingrese el numero a averiguar"))
    if (numero==0):
        print("El número es igual a 0")
    elif((numero%2)==0):
        print("El número ingresado es Par")
    else:
        print("El número ingresado es Impar")


#6. Cree un script que le solicite al usuario ingresar 10 números, y una vez
#ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
#ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
#y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
#ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

posicion = 0
mayor = 0
for i in range (0,10):
    numero = int(input("Ingrese Los Números "))
    posicion +=1
    if (numero > mayor):
        mayor = numero 
        r_pos = posicion
print (f"El mayor número ingresado es {mayor}, y lo ingresaste en la posición {r_pos}")

#7. Extienda el script del ejercicio anterior para que también informe el número
#mínimo ingresado, y su posición.

posicion = 0
mayor = 0
menor = 0
for i in range (0,10):
    numero = int(input("Ingrese Los Números "))
    posicion +=1
    if (numero > mayor):
        mayor = numero 
        r_pos = posicion
    if (numero < menor):
        menor = numero 
        r_men_pos = posicion
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
for i in range (0,7):
    numero = int(input("Ingrese Las precipitaciones del día "))
    posicion +=1
    if (numero > mayor):
        mayor = numero 
        r_pos = posicion
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