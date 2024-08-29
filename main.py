from aritmetica import (
    suma, resta, multiplicacion, division, potencia,
    raiz_cuadrada, modulo, factorial, log, deg_to_rad
)

def main():
    a = 10
    b = 5

    print(f"Suma: {suma(a, b)}")
    print(f"Resta: {resta(a, b)}")
    print(f"Multiplicación: {multiplicacion(a, b)}")
    print(f"División: {division(a, b)}")
    print(f"Potencia: {potencia(a, b)}")
    print(f"Raíz Cuadrada: {raiz_cuadrada(a)}")
    print(f"Módulo: {modulo(a, b)}")
    print(f"Factorial: {factorial(a)}")
    print(f"Logaritmo Natural: {log(a)}")
    print(f"Convertir Grados a Radianes: {deg_to_rad(a)}")

if __name__ == "__main__":
    main()