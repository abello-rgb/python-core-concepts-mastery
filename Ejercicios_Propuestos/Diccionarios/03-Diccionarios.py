# ============================================
# GESTIÓN DE ESCUELA
# ============================================
# Conceptos aplicados:
# - Diccionarios anidados
# - Listas dentro de diccionarios
# - Iteración
# - Funciones
# - Búsqueda y filtrado
# ============================================


# Diccionario principal que representa una escuela
school = {
    "name": "CUN",               # Nombre de la escuela
    "city": "Santa Marta",      # Ciudad
    "students": [               # Lista de estudiantes
        {"name": "Ana",    "grade": 88, "active": True},
        {"name": "Luis",   "grade": 95, "active": False},
        {"name": "Karla",  "grade": 72, "active": True},
    ]
}


# ============================================
# FUNCIÓN 1: INFORMACIÓN DE LA ESCUELA
# ============================================

def school_info(school):  
    """
    Imprime la información básica de la escuela.

    Parámetro:
        school (dict): diccionario con datos de la escuela
    """
    name = school["name"]
    city = school["city"]

    print(f'🏫 Escuela: {name} / 🌍 Ciudad: {city}')


# ============================================
# FUNCIÓN 2: CONTAR ESTUDIANTES ACTIVOS
# ============================================

def active_count(school):
    """
    Retorna una lista con los nombres de los estudiantes activos.

    Parámetro:
        school (dict)

    Retorna:
        list: nombres de estudiantes activos
    """
    result = []  # Lista acumuladora

    # Accedemos a la lista de estudiantes dentro del diccionario
    for item in school["students"]:
        if item["active"]:  # Validamos si está activo
            result.append(item["name"])  # Guardamos el nombre

    return result


# ============================================
# FUNCIÓN 3: MEJOR ESTUDIANTE DE LA ESCUELA
# ============================================

def best_in_school(school):
    """
    Retorna el nombre del estudiante con la mejor calificación.

    Parámetro:
        school (dict)

    Retorna:
        str: nombre del mejor estudiante
    """

    # 🔴 Mejora: evitar iniciar en 0
    best = school["students"][0]

    for item in school["students"]:
        if item["grade"] > best["grade"]:
            best = item

    return best["name"]


# ============================================
# EJECUCIÓN DEL PROGRAMA
# ============================================

# Mostrar información de la escuela
school_info(school)

# Obtener estudiantes activos
my_count_active = active_count(school)
print(f'\n📌 Estudiantes activos: {my_count_active}')

# Obtener mejor estudiante
my_best_student = best_in_school(school)
print(f'\n🏆 Mejor estudiante: {my_best_student}')