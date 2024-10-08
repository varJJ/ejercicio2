import math

def suma(a,b):
    # Funcion suma Por Juan Jose Vargas 
    return a+b

def resta(a,b):
    #Funcion resta por : Vicente Mauricio Quinsamolle Vargas
    return a-b   

def multiplicacion(a,b):
    # Función implementada por Valeria Nicole Daza Chambi
    return a * b

def division(a,b):
    #Función de división desarrollado por Jhazmin Portuguez Colque
    if b == 0:
        return "Error: División por cero"
    return a / b

def raiz_cuadrada(a):

    # Implementado por Aiza Arce Jhoel Gustavo

    # Verifica si el número es negativo
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    # Calcula y devuelve la raíz cuadrada del número
    return math.sqrt(a)

def modulo(a,b):
    # Funcion implementada por Alan Giovanni Mora Vargas
    #TODO: "Implementar el módulo de dos números"
    if (a > b):
        return a % b
    else: 
        print('No se puede sacar el modulo de un numero menor al divisor')

def factorial(a):
    #implementado por Jafet Abner Canaza Febrero
    if (a%1==0 or a>0):
        if(a!=1):
            res = a*factorial(a-1)
        else: res =a
    else : res = 0
    return res

def log(a):
    # Funcion implementada por Gary E. Camacho G.
    if a <= 0:
        raise ValueError("El logaritmo natural no está definido para números no positivos.")
    
    n = iterations
    x = (a - 1) / (a + 1)
    result = 0

    for i in range(1, n+1, 2):
        term = (x ** i) / i
        result += term

    return 2 * result

def deg_to_rad(a):
    # Función implementada por Maria Fernanda Pizarroso Troncoso
    return math.radians(a)
