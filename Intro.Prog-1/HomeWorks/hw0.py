#################################################
# hw0.py (No cambiar el nombre de este archivo)
# Completar los siguientes datos:
# Nombre:Elias Espindola    
# DNI:42620599
#################################################


#################################################
# Funciones que tenés que programar
#################################################


def hello_world():
    return"Hello World!"
    # Modificar este código para que la función hello_world retorne el
    # string "Hello World!"
    pass


#################################################
# Funciones de Test (no modificar)
#################################################


def test_hello_world():
    print("Testeando hello_world()... ", end="")
    assert hello_world() == "Hello World!"
    print("Pasaste!")


#################################################
# testAll y main
#################################################


def testAll():
    # comentá los tests que no querés correr!
    test_hello_world()


def main():
    testAll()


if __name__ == "__main__":
    main()
