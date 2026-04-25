# ============================================
# GESTIÓN DE ESTUDIANTES
# ============================================
# Conceptos aplicados:
# - Listas de diccionarios
# - Iteración
# - Condicionales
# - Funciones
# - Cálculo de métricas
# ============================================


# Lista de estudiantes (cada estudiante es un diccionario)
students = [
    {"name": "Ana",    "grade": 88, "active": True},
    {"name": "Luis",   "grade": 95, "active": False},
    {"name": "Karla",  "grade": 72, "active": True},
    {"name": "Miguel", "grade": 95, "active": True},
    {"name": "Sara",   "grade": 61, "active": False},
]


# ============================================
# FUNCIÓN 1: ESTUDIANTES ACTIVOS
# ============================================

def active_students(students):
    """
    Retorna una lista con los nombres de los estudiantes activos.

    Parámetro:
        students (list): lista de diccionarios con datos de estudiantes

    Retorna:
        list: nombres de estudiantes activos
    """
    result = []  # Lista donde se almacenarán los estudiantes activos

    for item in students:  # Recorremos cada estudiante
        if item["active"]:  # Validamos si está activo (True)
            result.append(item["name"])  # Guardamos solo el nombre

    return result  # Retornamos la lista final


# ============================================
# FUNCIÓN 2: MEJOR ESTUDIANTE
# ============================================

def top_student(students):
    """
    Retorna el estudiante con la calificación más alta.

    Parámetro:
        students (list): lista de diccionarios

    Retorna:
        dict: estudiante con mejor nota
    """

    best_student_grade = 0  # Inicializamos la nota máxima en 0
    best = None             # Aquí guardaremos el mejor estudiante

    for item in students:  # Iteramos sobre cada estudiante

        # Comparamos la nota actual con la mejor encontrada
        if item["grade"] > best_student_grade:
            best_student_grade = item["grade"]  # Actualizamos la mejor nota
            best = item                         # Guardamos el estudiante

    return best  # Retornamos el diccionario completo


# ============================================
# FUNCIÓN 3: PROMEDIO DE LA CLASE
# ============================================

def class_average(students):
    """
    Calcula el promedio de las calificaciones de la clase.

    Parámetro:
        students (list): lista de diccionarios

    Retorna:
        float: promedio de notas
    """

    grades = []  # Lista para almacenar las notas

    for item in students:
        grades.append(item["grade"])  # Agregamos cada nota a la lista

    # Promedio = suma de notas / cantidad de notas
    prom = sum(grades) / len(grades)

    return prom


# ============================================
# EJECUCIÓN DEL PROGRAMA
# ============================================

# Obtener estudiantes activos
my_active_students = active_students(students)
print("📌 Estudiantes activos:")
print(my_active_students)


# Obtener mejor estudiante
my_top_student = top_student(students)
print("\n🏆 Mejor estudiante:")
print(my_top_student)


# Obtener promedio de la clase
my_average_students = class_average(students)
print("\n📊 Promedio de la clase:")
print(f"{my_average_students:.2f}")