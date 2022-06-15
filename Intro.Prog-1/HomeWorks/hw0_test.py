


def NumeroMayor2(x,y):
    
    if (x == y):
        resultadoF = f"Los numeros {x} y {y} son iguales!"
    else:
        resultado = max (x, y)
        resultadoF = f"El numero mayor de {x} y {y} es {resultado}!"
    return "Holis"
    pass


assert NumeroMayor2(25,23) == "Holis"
print("Funcionó!!!")