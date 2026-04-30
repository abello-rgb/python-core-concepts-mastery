# =========================================================
# 🌍 Calculadora del Área Superficial de un Planeta
# =========================================================
#
# Este programa:
# 1. Guarda una lista de planetas.
# 2. Escoge un planeta aleatoriamente.
# 3. Asigna el radio correspondiente al planeta.
# 4. Calcula el área superficial usando la fórmula:
#
#       Área = 4 * π * r²
#
# 5. Muestra el resultado en pantalla.
#
# =========================================================

# Importamos el valor de PI desde el módulo math
from math import pi

# Importamos la función choice del módulo random
# y le cambiamos el nombre a "ch"
from random import choice as ch


# ---------------------------------------------------------
# Lista de planetas disponibles
# ---------------------------------------------------------
planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]


# ---------------------------------------------------------
# Función para calcular el área superficial de un planeta
# ---------------------------------------------------------
def cal_area(random_planet, r):
    """
    Calcula el área superficial de un planeta.

    Parámetros:
    random_planet (str): Nombre del planeta.
    r (int | float): Radio del planeta.

    Fórmula:
    Área = 4 * π * r²
    """

    # Fórmula del área superficial de una esfera
    area = 4 * pi * r**2

    # Mostramos el nombre del planeta y el área calculada
    print(f'{random_planet}: {area}')


# ---------------------------------------------------------
# Seleccionar un planeta aleatoriamente
# ---------------------------------------------------------
random_planet = ch(planets)


# ---------------------------------------------------------
# Verificar qué planeta fue seleccionado
# y asignar su radio correspondiente
# ---------------------------------------------------------

if random_planet == 'Mercury':

    # Radio de Mercurio en kilómetros
    r = 2440

    # Llamar a la función
    cal_area(random_planet, r)

elif random_planet == 'Venus':

    # Radio de Venus en kilómetros
    r = 6052

    cal_area(random_planet, r)

elif random_planet == 'Earth':

    # Radio de la Tierra en kilómetros
    r = 6371

    cal_area(random_planet, r)

elif random_planet == 'Mars':

    # Radio de Marte en kilómetros
    r = 3390

    cal_area(random_planet, r)

elif random_planet == 'Saturn':

    # Radio de Saturno en kilómetros
    r = 58232

    cal_area(random_planet, r)

else:
    # Mensaje de error en caso de que ocurra algo inesperado
    print('¡Ups! Se produjo un error.')