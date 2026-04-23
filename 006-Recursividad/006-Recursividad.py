# ============================================
# RECURSIVIDAD EN PYTHON
# ============================================
# Conceptos aplicados:
# - Funciones recursivas
# - Caso base
# - Caso recursivo
# ============================================


# ============================================
# FUNCIÓN FACTORIAL
# ============================================

def factorial(number: int) -> int:
    """
    Calcula el factorial de un número usando recursividad.

    Fórmula:
        n! = n * (n-1)!
        0! = 1

    Parámetros:
        number (int): número a calcular

    Retorna:
        int: factorial del número
    """

    # ----------------------------------------
    # VALIDACIÓN
    # ----------------------------------------
    if number < 0:
        print('Los números negativos no tienen factorial')
        return 0

    # ----------------------------------------
    # CASO BASE
    # ----------------------------------------
    elif number == 0:
        return 1

    # ----------------------------------------
    # CASO RECURSIVO
    # ----------------------------------------
    else:
        return number * factorial(number - 1)


# Ejemplo:
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1 * factorial(0)
# = 5 * 4 * 3 * 2 * 1 * 1
# = 120



# ============================================
# FUNCIÓN FIBONACCI
# ============================================

def fibonacci(number: int) -> int:
    """
    Calcula el valor en la posición 'number' de la serie de Fibonacci.

    Serie:
        0, 1, 1, 2, 3, 5, 8...

    Parámetros:
        number (int): posición (empezando desde 1)

    Retorna:
        int: valor en la posición indicada
    """

    # ----------------------------------------
    # VALIDACIÓN
    # ----------------------------------------
    if number <= 0:
        print('La posición tiene que ser mayor que cero')
        return 0

    # ----------------------------------------
    # CASOS BASE
    # ----------------------------------------
    elif number == 1:
        return 0
    elif number == 2:
        return 1

    # ----------------------------------------
    # CASO RECURSIVO
    # ----------------------------------------
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# ============================================
# EJECUCIÓN
# ============================================

print(fibonacci(5))