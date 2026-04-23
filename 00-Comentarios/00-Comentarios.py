# ============================================
# FUNDAMENTOS BÁSICOS DE PYTHON
# ============================================
# Conceptos aplicados:
# - Comentarios
# - Variables y reasignación
# - Convención de constantes
# - Tipos de datos primitivos
# - Salida por consola
# - Inspección de tipos (type)
# ============================================


# ============================================
# COMENTARIOS EN PYTHON
# ============================================

# Comentario de una sola línea
# Se usa para explicar una línea específica de código

"""
Comentario multilínea:
Se usa para documentar bloques más grandes.
También puede funcionar como docstring en funciones/clases.
"""


# ============================================
# VARIABLES
# ============================================

# Crear una variable (Python infiere el tipo automáticamente)
my_variable = "Mi variable"

# Reasignación de variable
# Python permite cambiar el valor y el tipo dinámicamente
my_variable = "Nuevo valor de mi variable"


# ============================================
# CONSTANTES (CONVENCIÓN)
# ============================================

# En Python NO existen constantes reales
# Pero por convención se escriben en MAYÚSCULAS
MY_CONSTANTE = "Mi constante"

# ⚠️ Aunque se puede cambiar, NO se debería hacer:
# MY_CONSTANTE = "Otro valor"  # Mala práctica


# ============================================
# TIPOS DE DATOS PRIMITIVOS
# ============================================

# Entero (int)
my_int = 1997

# Flotante (float)
my_float = 1.65

# Booleano (bool)
my_bool = True
my_bool = False  # Reasignación

# Cadenas de texto (str)
my_string = 'Breiner'
my_other_string = "Abello"

# Python permite usar comillas simples o dobles


# ============================================
# SALIDA POR CONSOLA
# ============================================

# print() muestra información en pantalla
print('Hola, esto es Python')


# ============================================
# INSPECCIÓN DE TIPOS
# ============================================

# type() permite conocer el tipo de dato de una variable
print(type(my_int))       # <class 'int'>
print(type(my_float))     # <class 'float'>
print(type(my_bool))      # <class 'bool'>
print(type(my_string))    # <class 'str'>


# ============================================
# BUENAS PRÁCTICAS (EXTRA)
# ============================================

# Puedes imprimir múltiples valores
print("Nombre:", my_string, my_other_string)

# Usar f-strings (forma moderna y recomendada)
print(f"Mi nombre es {my_string} {my_other_string} y nací en {my_int}")

# Verificación dinámica de tipos
if isinstance(my_int, int):
    print("my_int es un entero")

# ============================================
# FIN DEL SCRIPT
# ============================================