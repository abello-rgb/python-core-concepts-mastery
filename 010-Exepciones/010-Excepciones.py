# ============================================
# MANEJO DE EXCEPCIONES EN PYTHON
# ============================================
# Conceptos aplicados:
# - Validación de datos
# - Lanzamiento de excepciones (raise)
# - Manejo de errores con try/except
# - Manejo de errores específicos vs generales
# - Buenas prácticas (mensajes claros)
# ============================================


def process_params(parameters: list):
    """
    Procesa una lista de parámetros realizando validaciones y operaciones.

    Parámetros:
        parameters (list): Lista que debe contener al menos 3 elementos:
            - parameters[0]: número (dividendo)
            - parameters[1]: número (divisor)
            - parameters[2]: valor a imprimir y operar

    Excepciones:
        IndexError: Si la lista tiene menos de 3 elementos
        ZeroDivisionError: Si el divisor es 0
        TypeError: Si los tipos de datos no son correctos
    """

    # ============================================
    # VALIDACIÓN DE LONGITUD
    # ============================================
    if len(parameters) < 3:
        # Se lanza una excepción manualmente
        raise IndexError("La lista debe tener al menos 3 elementos")

    # ============================================
    # VALIDACIÓN DE DIVISIÓN POR CERO
    # ============================================
    if parameters[1] == 0:
        # Evitamos un error matemático
        raise ZeroDivisionError("No se puede dividir entre cero")

    # ============================================
    # EJECUCIÓN DE OPERACIONES
    # ============================================

    # Imprime el tercer elemento
    print(f'Tercer parámetro: {parameters[2]}')

    # División (puede lanzar TypeError si no son números)
    result_division = parameters[0] / parameters[1]
    print(f'División: {result_division}')

    # Suma (puede fallar si no es numérico)
    result_sum = parameters[2] + 5
    print(f'Suma: {result_sum}')


# ============================================
# BLOQUE DE EJECUCIÓN CONTROLADA
# ============================================

try:
    # Llamada a la función con datos de prueba
    process_params([1, 2, 'Breiner', 3])

# ============================================
# MANEJO DE ERRORES ESPECÍFICOS
# ============================================

except IndexError as e:
    # Error cuando faltan elementos en la lista
    print('❌ Error: El número de elementos debe ser al menos 3')
    print(f'Detalle técnico: {e}')

except ZeroDivisionError as e:
    # Error cuando el divisor es cero
    print('❌ Error: No se puede dividir entre cero')
    print(f'Detalle técnico: {e}')

except TypeError as e:
    # Error cuando hay tipos incompatibles (ej: string + int)
    print('❌ Error: Tipo de dato inválido en las operaciones')
    print(f'Detalle técnico: {e}')

# ============================================
# MANEJO GENERAL (ÚLTIMA LÍNEA DE DEFENSA)
# ============================================

except Exception as e:
    # Captura cualquier error no previsto
    print(f'❌ ERROR inesperado: {e}')

# ============================================
# BLOQUE OPCIONAL (SIEMPRE SE EJECUTA)
# ============================================

finally:
    print('✔ Fin del proceso (con o sin errores)')