# ============================================
# FUNCIONES EN PYTHON (USER-DEFINED FUNCTIONS)
# ============================================
# Conceptos aplicados:
# - Definición de funciones
# - Retorno de valores
# - Parámetros y argumentos
# - Argumentos por defecto
# - Retornos múltiples
# - *args y **kwargs
# - Funciones anidadas
# - Funciones built-in
# ============================================


# ============================================
# FUNCIÓN SIMPLE (SIN PARÁMETROS NI RETORNO)
# ============================================

def greet():
    """
    Función básica que imprime un mensaje.
    """
    print('Hola, desde una función simple en Python')


# Llamada a la función
greet()


# ============================================
# FUNCIÓN CON RETORNO
# ============================================

def return_greet():
    """
    Retorna un mensaje en lugar de imprimirlo.
    """
    return 'Hola, desde una función con return en Python'


# ⚠️ Aquí estás sobrescribiendo el nombre "greet"
# Esto es válido, pero puede generar confusión
greet_message = return_greet()
print(greet_message)


# ============================================
# FUNCIÓN CON UN ARGUMENTO
# ============================================

def arg_greet(nombre):
    """
    Recibe un nombre y muestra un saludo.
    """
    print(f'Hola, Bienvenido {nombre}')


arg_greet('Breiner')


# ============================================
# FUNCIÓN CON VARIOS ARGUMENTOS
# ============================================

def args_greet(nombre_trabajador, dependencia):
    """
    Recibe nombre y dependencia (área de trabajo).
    """
    print(f'Hola, {nombre_trabajador}, perteneces a {dependencia}')


args_greet('Breiner', 'Sistemas')


# ============================================
# FUNCIÓN CON ARGUMENTO POR DEFECTO
# ============================================

def default_arg_greet(name='Nombre no definido'):
    """
    Si no se pasa argumento, usa el valor por defecto.
    """
    print(f'Hola, {name}')


default_arg_greet()          # Usa valor por defecto
default_arg_greet('Diana')   # Sobrescribe el valor


# ============================================
# FUNCIÓN CON PARÁMETROS Y RETORNO
# ============================================

def return_arg_greet(greet, name):
    """
    Combina dos parámetros y retorna un mensaje.
    """
    return f'{greet}, {name}'


print(return_arg_greet('Hi', 'Breiner Abello'))


# ============================================
# RETORNO DE MÚLTIPLES VALORES
# ============================================

def multiple_return_greet():
    """
    Retorna múltiples valores (en realidad es una tupla).
    """
    return 'Hola', 'Python'


# Desempaquetado de valores
greet, name = multiple_return_greet()
print(greet)
print(name)


# ============================================
# ARGUMENTOS VARIABLES (*args)
# ============================================

def variable_arg_greet(*names):
    """
    Recibe un número variable de argumentos.
    Se almacenan como una tupla.
    """
    for name in names:
        print(f'Hola, {name}')


variable_arg_greet('Python', 'JavaScript', 'Java')


# ============================================
# ARGUMENTOS CON CLAVE (**kwargs)
# ============================================

def variable_key_arg_greet(**data):
    """
    Recibe argumentos con clave (diccionario).
    """
    for key, value in data.items():
        print(f'{key}: {value}')


variable_key_arg_greet(
    language='Python',
    name='Breiner',
    edad=28
)


# ============================================
# FUNCIONES ANIDADAS
# ============================================

def funcion_externa():
    """
    Función que contiene otra función dentro.
    """

    def funcion_interna():
        """
        Solo existe dentro de la función externa.
        """
        print('Contenido de la función interna')

    # Llamada a la función interna
    funcion_interna()


funcion_externa()


# ============================================
# FUNCIONES BUILT-IN (DEL LENGUAJE)
# ============================================

# len() → longitud
print(len('Breiner'))

# type() → tipo de dato
print(type('Breiner'))

# Métodos de string
print('Peligro'.upper())  # Convierte a mayúsculas