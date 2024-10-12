def suma(a, b):
    """Esta funcion suma dos numeros"""
    return a+b

def resta(a, b):
    """Esta funcion resta dos numeros"""
    return a-b

def multiplicacion(a,b):
    """Esta funcion multiplica dos numeros"""
    return a*b

def division(a,b):
    """Esta funcion divide dos numeros"""
    if b==0:
        return "Error:Division entre cero"
    else:
        return a/b


if __name__=="__main__":
    num1= 5
    num2= 3
    resultado_suma = suma(num1,num2)
    resultado_resta = resta(num1,num2)
    resultado_multi = multiplicacion(num1,num2)
    resultado_division = division(num1,num2)

    print(f"La suma de {num1} y {num2} es:{resultado_suma}")
    print(f"La resta de {num1} y {num2} es:{resultado_resta}")
    print(f"La multiplicacion de {num1} y {num2} es:{resultado_multi}")
    print(f"La division de {num1} y {num2} es:{resultado_division}")