################################################################################################
# Nombre de archivo: hw2.py (No cambiar el nombre de este archivo)
# El repositorio donde esta tu HW2 es: github.com/unlu-edu-ar/homework-2-TuNombreDeUsuarioGithub
#
# Completa con tu nombre, apellido y DNI
# Nombre y Apellido: Elias Espindola    
# DNI: 42620599
################################################################################################


#################################################
# Funciones que tenés que programar
#################################################

# Cree una función que recibe un número entero N como parámetro, y retorna un 
# booleano. Si el número N es mayor que cero, retorna True. Si el número N es 
# menor o igual a cero, retorna False
def numeroPositivo(x):
    N = (x > 0)
    return N
    pass

# Cree una función que recibe un string como parámetro, y retorna un string con 
# la leyenda "Sos Maria", si el string recibido de argumento fuese "Maria", 
# "Sos Pedro" si el string recibido fuese "Pedro", "No sos Maria ni Pedro. Quien sos?" 
# si el string recibido como argumento no fuese "Maria" ni "Pedro"
def quienSos(x):
    if ( "Maria" == x ):
        respuesta = "Sos Maria"
    elif ( "Pedro" == x):
        respuesta = "Sos Pedro"
    else :
        respuesta = "No sos Maria ni Pedro. Quien sos?"
    return respuesta
    pass
    
# Cree una función que recibe dos números de parámetro, y retorna el menor de 
# ellos, si los números fuesen distintos. Si los números fuesen iguales, debe 
# retornar el string "Son iguales!"
def dameElMenorODecimeSiSonIguales(x, y):
    if(x < y):
        respuesta = x
    elif(y < x):
        respuesta = y
    else:
        respuesta = "Son iguales!"
    return respuesta
    pass

# Cree una función que recibe un número entero entre 1 y 12 de parámetro, 
# correspondiente a un mes y retorna un  string, con el nombre del mes en 
# lenguaje natural. La relación entre números y meses es la siguiente: 1 Enero, 
# 2 Febrero, 3 Marzo, 4 Abril, 5 Mayo, 6 Junio, 7 Julio, 8 Agosto, 9 Septiembre, 
# 10 Octubre, 11 Noviembre, 12 Diciembre
def decimeElMes(x):
    if (x == 1):
       r = "Enero"
    elif (x == 2):
       r = "Febrero"
    elif (x == 3):
       r = "Marzo"
    elif (x == 4):
       r ="Abril"
    elif (x == 5):
       r = "Mayo"
    elif (x == 6):
       r = "Junio"
    elif (x == 7):
       r = "Julio"
    elif (x == 8):
       r = "Agosto"
    elif (x == 9):
       r = "Septiembre"
    elif (x == 10):
       r = "Octubre"
    elif (x == 11):
       r = "Noviembre"
    elif (x == 12):
       r = "Diciembre"
    return r
    pass

# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a
# un mes y retorna un  string, con el nombre de la estación. Considera la 
# relación entre números y estaciones de la siguiente forma: 1, 2, 3: "Verano", 
# 4, 5, 6: "Otoño", 7, 8, 9: "Invierno", 10, 11, 12: "Primavera"
def estacion(x):
    if (x > 0) and (x < 4):
        r = "Verano"
    elif (x < 7) and (x > 3):
        r = "Otoño"
    elif (x < 10) and (x > 6):
        r = "Invierno"
    elif (x < 13) and (x > 9):
        r = "Primavera"
    return r
    pass

# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a
# un mes, y retorna un booleano, que es True si el número del mes fuese par, 
# y False si el número del mes fuese impar
def mesPar(x):
    r = (x % 2) == 0
    return r
    pass

# Cree una función que recibe dos números entre 0 y 10, correspondientes a las
# notas de los exámenes, y retorna un string con la leyenda "Promovido", si el 
# promedio de dichos númueros, fuese mayor o igual a 8, "Regular", si el promedio
# fuese mayor o igual a 4 pero menor a 8, y "Libre" si el promedio de las notas
# fuese menor a 4
def situacionAlumno(p1, p2):
    P = (p1 + p2) / 2
    if (P > 7 ):
        r = "Promovido"
    if (P < 8) and (P > 3):
        r = "Regular"
    if (P < 4):
        r="Libre"
    return r
    pass

# En un triángulo la longitud de cada lado es menor que la suma de los otros dos.
# Cree una función que recibe 3 enteros como parámetros, y retorna un booleano 
# que es True en el caso de que los valores recibidos puedan corresponder a las 
# longitudes de los lados de un triángulo y False en caso contrario. Recuerde 
# que ninguna de las longitudes de los lados de un triángulo puede ser cero, 
# o números negativos.
def esTriangulo(x, y, z):
    if (x > 0) or (y > 0) or (z > 0):
        r = ((x + y) > z ) and ((y + z) > x) and ((z + x) > y)
    else :
        r = False
    return r
    pass

# Cree una función que recibe 3 números enteros como parámetros, y retorna un 
# string con la leyenda:
# "No es un triangulo", si los longitudes no pueden corresponder a un triángulo
# "Equilatero", si puede ser un triángulo y todos las longitudes son iguales
# "Isosceles", si puede ser un triángulo y tiene dos longitudes iguales
# "Escaleno", si puede ser un triángulo y todas las longitudes son diferentes
def tipoTriangulo(x, y, z):
    if (x > 0) or (y > 0) or (z > 0):
        if ((x + y) > z ) and ((y + z) > x) and ((z + x) > y):
           if (x == y == z):
              r = "Equilatero"
           elif (x == y != z) or (y != z == x ) or (z != x == y ):
              r = "Isosceles"
           elif (x != y != z):
              r = "Escaleno"
        else :
            r = "No es un triangulo"
    return r
    pass

#################################################
# Funciones de Test (no modificar)
#################################################

def testNumeroPositivo():
    print('Testeando testNumeroPositivo()... ', end='')
    assert numeroPositivo(10) == True
    assert numeroPositivo(-10) == False
    assert numeroPositivo(0) == False
    print('Pasó!')

def testQuienSos():
    print('Testeando testQuienSos()... ', end='')
    assert quienSos("Maria") == "Sos Maria"
    assert quienSos("Pedro") == "Sos Pedro"
    assert quienSos("Juan") == "No sos Maria ni Pedro. Quien sos?"
    print('Pasó!')

def testDameElMenorODecimeSiSonIguales():
    print('Testeando testDameElMenorODecimeSiSonIguales()... ', end='')
    assert dameElMenorODecimeSiSonIguales(4,1) == 1
    assert dameElMenorODecimeSiSonIguales(-1, 4) == -1
    assert dameElMenorODecimeSiSonIguales(4,4) == "Son iguales!"
    print('Pasó!')

def testDecimeElMes():
    print('Testeando testDecimeElMes()... ', end='')
    assert decimeElMes(1) == "Enero"
    assert decimeElMes(2) == "Febrero"
    assert decimeElMes(3) == "Marzo"
    assert decimeElMes(4) == "Abril"
    assert decimeElMes(5) == "Mayo"
    assert decimeElMes(6) == "Junio"
    assert decimeElMes(7) == "Julio"
    assert decimeElMes(8) == "Agosto"
    assert decimeElMes(9) == "Septiembre"
    assert decimeElMes(10) == "Octubre"
    assert decimeElMes(11) == "Noviembre"
    assert decimeElMes(12) == "Diciembre"
    print('Pasó!')

def testEstacion():
    print('Testeando testEstacion()... ', end='')
    assert estacion(1) == "Verano"
    assert estacion(2) == "Verano"
    assert estacion(3) == "Verano"        
    assert estacion(4) == "Otoño"
    assert estacion(5) == "Otoño"
    assert estacion(6) == "Otoño"
    assert estacion(7) == "Invierno"
    assert estacion(8) == "Invierno"
    assert estacion(9) == "Invierno"    
    assert estacion(10) == "Primavera"
    assert estacion(11) == "Primavera"
    assert estacion(12) == "Primavera"
    print('Pasó!')

def testMesPar():
    print('Testeando testMesPar()... ', end='')
    assert mesPar(1) == False
    assert mesPar(7) == False
    assert mesPar(12) == True
    print('Pasó!')

def testSituacionAlumno():
    print('Testeando testSituacionAlumno()... ', end='')
    assert situacionAlumno(1,3) == "Libre"
    assert situacionAlumno(9,10) == "Promovido"
    assert situacionAlumno(5,7) == "Regular"
    print('Pasó!')

def testEsTriangulo():
    print('Testeando testEsTriangulo()... ', end='')
    assert esTriangulo(6,6,3) == True
    assert esTriangulo(3,0,1) == False
    assert esTriangulo(1,2,3) == False
    assert esTriangulo(-1, 1, 2) == False
    print('Pasó!')

def testTipoTriangulo():
    print('Testeando testTipoTriangulo()... ', end='')
    assert tipoTriangulo(6,6,3) == "Isosceles"
    assert tipoTriangulo(2,2,2) == "Equilatero"
    assert tipoTriangulo(5,3,7) == "Escaleno"
    assert tipoTriangulo(1,2,3) == "No es un triangulo"
    print('Pasó!')

#################################################
# testearTodo y main
#################################################

def testearTodo():
    # comentá los tests que no querés correr!
    testNumeroPositivo()
    testQuienSos()
    testDameElMenorODecimeSiSonIguales()
    testDecimeElMes()
    testEstacion()
    testMesPar()
    testSituacionAlumno()
    testEsTriangulo()
    testTipoTriangulo()

def main():
    testearTodo()

if __name__ == '__main__':
    main()
