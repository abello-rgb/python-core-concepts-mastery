# ============================================
# VALOR Y REFERENCIA EN PYTHON
# ============================================
# Conceptos clave:
# - Tipos inmutables vs mutables
# - Asignación de variables
# - Paso de argumentos a funciones
# - Efectos secundarios (side effects)
# ============================================


# ============================================
# TIPOS INMUTABLES (COMO SI FUERAN "POR VALOR")
# ============================================
# int, float, str, tuple, bool

my_int_a = 10

# Se copia el valor (en realidad referencia a un objeto inmutable)
my_int_b = my_int_a

# Se reasigna my_int_a a un nuevo valor (nuevo objeto)
my_int_a = 30

# RESULTADO:
# my_int_a → 30
# my_int_b → 10 (no cambia)
# porque los enteros son INMUTABLES

# print(my_int_a)
# print(my_int_b)


# ============================================
# TIPOS MUTABLES (LISTAS)
# ============================================
# list, dict, set

my_list_a = [10, 20]

# Ambas variables apuntan al MISMO objeto en memoria
my_list_b = my_list_a

# Modificamos el objeto (no la referencia)
my_list_b.append(30)

# RESULTADO:
# my_list_a → [10, 20, 30]
# my_list_b → [10, 20, 30]

# print(my_list_a)
# print(my_list_b)


# ============================================
# FUNCIONES CON TIPOS INMUTABLES
# ============================================

my_int_c = 10

def my_int_func(my_int: int):
    """
    Recibe un entero (inmutable).
    Cualquier cambio crea un nuevo valor local.
    """
    my_int = 20  # Nueva asignación (no afecta afuera)
    print(f'Dentro de la función: {my_int}')


my_int_func(my_int_c)

# AFUERA no cambia
print(f'Fuera de la función: {my_int_c}')


# ============================================
# FUNCIONES CON TIPOS MUTABLES
# ============================================

my_list_c = [20, 40]

def my_list_func(my_list: list):
    """
    Recibe una lista (mutable).
    Las modificaciones afectan el objeto original.
    """

    # Modifica directamente la lista original
    my_list.append(30)

    # Ambas variables apuntan al mismo objeto
    my_list_d = my_list

    # Sigue modificando el mismo objeto
    my_list_d.append(15)

    print(f'Dentro función (my_list): {my_list}')
    print(f'Dentro función (my_list_d): {my_list_d}')


my_list_func(my_list_c)

# AFUERA también cambia (efecto secundario)
print(f'Fuera de la función: {my_list_c}')