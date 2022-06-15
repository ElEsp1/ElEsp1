#Escriba una función en Python que permita procesar la información sobre n webinars (charlas online). 
#La función recibirá como parámetro la cantidad de webinars que deben ser procesados (n).
#Por cada webinar, el programa debe solicitar ingresar el título de la actividad y el número de inscriptos. 
#Por ejemplo, una entrada válida del programa sería el valor 77 para el número de inscriptos e 
#“Introducción a Redes Neuronales” para el título.
#Una vez procesados todos los webinars, el programa debe informar:
#El promedio de inscriptos entre todos los webinars.

#Además, la función debe retornar El título del webinar con la menor cantidad de inscriptos y el 
#El título del webinar con la mayor cantidad de inscriptos

INPUT: n(int)
OUTPUT: tit_mayor (str), tit_menor(str)

def webinar(n):

# Promedio = (sumatoria de todos los elementos) / (cantidad total de elementos)

   sumatoria = 0
   mayor_cant_inscriptos = 0
   menor_cant_inscriptos = 9999999999 (mayor numero entero que se puede representar en tipo de dato entero)
   tit_mayor = ""
   tit_menor = ""
  
   for i in range(n):
      tit = input("Ingrese un titulo: ")
      cant_inscriptos = int(input("Ingrese la cantidad de inscriptos")) 


      sumatoria = sumatoria + cant_inscriptos

      # Averiguo menor
      if cant_inscriptos <= menor_cant_inscriptos:
          tit_menor = tit
          menor_cant_inscriptos = cant_incriptos

      # Averiguo mayor
      if cant_inscriptos >= mayor_cant_inscriptos:
          tit_mayor = tit
          mayor_cant_inscriptos = cant_incriptos

   if n > 0: 
      promedio = sumatoria/n
      print(promedio)
   else:
      print("No se ingresaron webinars")


   return tit_mayor, tit_menor


#Prueba webinar(0) --> "", "" y imprime el mensaje "No se ingresaron webinars"
n = 0
sumatoria = 0
tit_mayor = ""
tit_menor = ""


#Prueba webinar(1) --> "Titulo1 ingresado x usuario..", "Titulo1 ingresado x usuario y imprime promedio
sumatoria = 0 --> 4 
mayor_cant_inscriptos = 0 --> 4
menor_cant_inscriptos = 9999999999 --> 4
tit_mayor = "" --> "Programacion en HTML"
tit_menor = "" --> "Programacion en HTML"
i = 0
tit = "Programacion en HTML"
cant_inscriptos = 4
promedio = 4

#======================================================================================
#Escriba una función en Python que reciba como parámetros dos números naturales n y m, 
#donde n < m, (no hace falta validar) y retorne el producto de todos los números entre 
#n y m ellos incluidos. 
E1: n=2, m=4, resultado=2*3*4=24
E2: n=1, m=2, resultado=1*2=2

INPUT: n, m (int)
OUTPUT: prod (int)


def productoria(n,m):

   prod = 1
   for i in range (n, m+1):
       prod = i*prod  


   return prod

PRUEBA: productoria(1,2) --> 2
n = 1
m = 2
prod = 1 --> 1 --> 2
i = 1 -->2

PRUEBA: productoria(2,4) --> 24
n = 2
m = 4
prod = 1 --> 2 --> 6 --> 24
i = 2 --> 3 --> 4

#Variación: Escriba una función en Python que reciba como parámetro una lista de enteros y 
#muestre por pantalla la sumatoria de todos los números de la lista. 
E1: [3,7, 1] Muestra 11
E2: [1] Muestra 1

INPUT: l: list(int)
OUTPUT: None
#La función muestra por pantalla la sumatoria

def sumar_lista(l):

   sumatoria = 0

    for i in range(len(l)):
       sumatoria = sumatoria + l[i]      


   # for i in l:
   #    sumatoria = sumatoria + i   

   print(sumatoria)

PRUEBA: sumar_lista([1]) --> None (muestra por pantalla 1)
l = [1]
sumatoria = 0 --> 1
i = 0

PRUEBA: sumar_lista([3,7,1]) --> None (muestra por pantalla 11)
l = [3,7,1]
sumatoria = 0 --> 3 --> 10 --> 11
i = 0 --> 1 --> 2


PRUEBA: sumar_lista([1]) --> None (muestra por pantalla 1)
l = [1]
sumatoria = 0 --> 1
i = 1

PRUEBA: sumar_lista([3,7,1]) --> None (muestra por pantalla 11)
l = [3,7,1]
sumatoria = 0 --> 3 --> 10 --> 11
i = 3 --> 7 --> 1