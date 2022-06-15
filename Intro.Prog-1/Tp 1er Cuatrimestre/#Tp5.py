#Trabajo Práctico V
#Funciones propias

#Hasta ahora, sólo utilizamos funciones built-in, es decir, funciones predefinidas por el
#lenguaje Python. En los siguientes ejercicios aprenderemos a crear nuestras propias
#funciones. Las funciones en Python se definen con la siguiente estructura:

#1. Cree una función que reciba dos números como parámetro, y muestre en
#pantalla la suma aritmética de ambos. Invoque a la función con dos números
#leídos desde teclado.


def Suma_Arit(b,a):
    resultado = int(a) + int(b)
    print(resultado)
    pass
N1 = int (input("Ingrese el Primer número a sumar: "))
N2 = int (input("Ingrese el Segundo número a sumar: "))
Suma_Arit(N1,N2)

#2. Modifique el script del ejercicio anterior para que la función retorne el resultado
#en vez de mostrarlo. El programa debe seguir mostrando el resultado en
#pantalla.

def Suma_Arit(b,a):
    resultado = a + b
    return resultado

N1 = int (input("Ingrese el Primer número a sumar: "))
N2 = int (input("Ingrese el Segundo número a sumar: "))
resultado = Suma_Arit(N1,N2)
print (resultado) 

#3. Cree una función que reciba un string como parámetro, y retorne la cantidad de
#letras que posee. Luego, utilice la función para escribir un programa que solicite
#ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
#ese nombre.

def Cant_Letras(nombre):
    resultado = len(nombre)
    return resultado

nombre = input("Ingrese el nombre de Usuario: ")
resultado = Cant_Letras(nombre)
print(f"El Nombre de Usuario {nombre} tiene la cantidad de {resultado} letras")

#4. Cree una función que reciba dos números como parámetro (base y exponente),
#y retorne el resultado de elevar base a la potencia exponente.

def Potencia_Exp(base,exponente):
    resultado = base**exponente 
    return resultado

base = int(input("Ingrese el número Base: "))
exponente = int(input("Ingrese el Exponente: "))
resultado = Potencia_Exp(base,exponente)
print(f"La base {base} con el exponente {exponente} da como resultado: {resultado}")


#5. Cree una función que reciba un string como parámetro, y retorne el mismo
#string, pero con todas las letras convertidas a mayúsculas.

def Min_Mayus(nombre):
    resultado = nombre.upper()
    return resultado 

nombre = input("Ingrese la/las palabras a convertir: ")
resultado = Min_Mayus(nombre)
print(" ", resultado, " ")


#6. Modifique la función del ejercicio anterior para que retorne dos versiones del
#string recibido como parámetro: primero la versión en minúsculas, y luego la
#versión en mayúsculas.

def Min_Mayus(nombre):
    resultado_final = (f"La palabra {str(nombre.lower())} En mayúscula sería {str(nombre.upper())}")
    return resultado_final

nombre = input("Ingrese la/las palabras a convertir: ")
resultado = Min_Mayus(nombre)
print(" ", resultado, " ")

#7. Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
#y retorne True si nombre1 tiene más letras que nombre2, o False en caso
#contrario.

def Cant_Letras_VF(Nombre1, Nombre2):
    resultado = (len(Nombre1)) > (len(Nombre2)) 
    return resultado

N1 = input("Ingrese el primer nombre a comparar: ")
N2 = input ("Ingrese el segundo nombre a comparar: ")
resultado = Cant_Letras_VF(N1, N2)
print(f"El nombre {N1} tiene mayor cantidad de caracteres que el nombre {N2} : Respuesta {resultado}") 


#8. Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
#llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
#un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
#programa_principal.py, que ejecute el programa haciendo uso de la función
#creada en el otro archivo.

from Modulo_cadena import * 

resultado = leer_cadena()

print(f"La cadena ingresada es: {resultado}")

