"""
============================================
EJERCICIO 1: DICCIONARIO BÁSICO (PELÍCULA)
============================================

Objetivo:
Crear un diccionario con información de una película
y mostrar solo algunos de sus campos.
"""

# Definición de un diccionario (estructura clave-valor)
movie: dict = {
    'title': 'American Horror Stories',  # Nombre de la película
    'year': 2021,                        # Año de lanzamiento
    'rating': 5.0,                       # Calificación (float)
    'available': True,                   # Disponibilidad (booleano)
}

# Acceso a valores del diccionario usando su clave
# print(f'Película: {movie["title"]}, Rating: {movie["rating"]} ⭐')


"""
============================================
EJERCICIO 2: INVENTARIO DE PELÍCULAS
============================================

Trabajamos con una lista de diccionarios.
Cada diccionario representa una película.
"""

movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8, "available": True},
    {"title": "Interstellar", "year": 2014, "rating": 8.6, "available": False},
    {"title": "The Batman", "year": 2022, "rating": 7.8, "available": True},
    {"title": "Oppenheimer", "year": 2023, "rating": 8.4, "available": True},
]


# ============================================
# FUNCIÓN 1: OBTENER PELÍCULAS DISPONIBLES
# ============================================

def get_available(movies):
    """
    Retorna una lista con los títulos de las películas disponibles.

    Parámetro:
        movies (list): lista de diccionarios

    Retorna:
        list: títulos de películas disponibles
    """
    available = []  # Lista donde guardaremos los resultados

    for movie in movies:
        # Verificamos si la película está disponible
        if movie["available"]:
            available.append(movie["title"])  # Guardamos solo el título

    return available


# ============================================
# FUNCIÓN 2: MEJOR PELÍCULA (POR RATING)
# ============================================

def best_rated(movies):
    """
    Retorna la película con mayor calificación.

    Parámetro:
        movies (list): lista de diccionarios

    Retorna:
        dict: película con mejor rating
    """
    rating = 0      # Variable para guardar el mayor rating encontrado
    best = None     # Variable para guardar la mejor película

    for movie in movies:
        # Si encontramos una película con mejor rating
        if movie["rating"] > rating:
            rating = movie["rating"]  # Actualizamos el valor máximo
            best = movie              # Guardamos la película completa

    return best


# ============================================
# FUNCIÓN 3: PROMEDIO DE CALIFICACIONES
# ============================================

def average_rating(movies):
    """
    Calcula el promedio de rating de todas las películas.

    Parámetro:
        movies (list): lista de diccionarios

    Retorna:
        float: promedio de ratings
    """
    ratings = []  # Lista acumuladora

    for movie in movies:
        ratings.append(movie["rating"])  # Agregamos cada rating

    # Promedio = suma / cantidad
    return sum(ratings) / len(ratings)


# ============================================
# EJECUCIÓN DEL PROGRAMA
# ============================================

# Obtener películas disponibles
disponibles = get_available(movies)

print("\n===== 🎬 TÍTULOS DISPONIBLES =====")
print(disponibles)


# Obtener la mejor película
best_rating = best_rated(movies)

print("\n===== 🏆 MEJOR PELÍCULA =====")
print(best_rating)


# Obtener promedio de ratings
prom_rating = average_rating(movies)

print("\n===== 📊 PROMEDIO DE CALIFICACIONES =====")
print(f"{prom_rating:.2f}")