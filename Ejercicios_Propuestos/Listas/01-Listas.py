# ============================================
# ANÁLISIS DE CALIFICACIONES
# ============================================
# Conceptos aplicados:
# - Listas
# - Funciones
# - Funciones built-in: sum, max, min, sorted
# - Manipulación de datos
# ============================================


# Lista de calificaciones
qualification_list = [72, 95, 88, 61, 95, 74, 88, 55, 95, 80]


# ============================================
# PROMEDIO GENERAL
# ============================================

def course_grade_average(qualifications: list):
    """
    Calcula el promedio de las calificaciones.

    Fórmula:
        promedio = suma de notas / cantidad de notas
    """
    prom = sum(qualifications) / len(qualifications)
    return prom


# ============================================
# NOTA MÁS ALTA Y MÁS BAJA
# ============================================

def show_high_and_low(qualifications):
    """
    Retorna la calificación más alta y la más baja.
    """
    return max(qualifications), min(qualifications)


# ============================================
# TOP 3 Y BOTTOM 3 
# ============================================

def top_and_bottom_3(qualifications):
    """
    Retorna:
    - Las 3 calificaciones más bajas (bottom 3)
    - Las 3 calificaciones más altas (top 3)
    """

    # Ordena de menor a mayor
    order = sorted(qualifications)

    # ❌ Antes estaba invertido en tu código
    bottom_3 = order[:3]     # menores
    top_3 = order[-3:]       # mayores

    return top_3, bottom_3


# ============================================
# CONTAR CUÁNTAS VECES APARECE LA NOTA MÁS ALTA
# ============================================

def count_top_score(qualifications):
    """
    Cuenta cuántas veces se repite la calificación más alta.
    """
    max_calification = max(qualifications)
    count_calification = qualifications.count(max_calification)
    return count_calification


# ============================================
# ELIMINAR LA NOTA MÁS BAJA
# ============================================

def remove_lowest(qualifications):
    sorted_qualifications = sorted(qualifications)
    minimo = min(sorted_qualifications)
    sorted_qualifications.remove(minimo)
    return sorted_qualifications


# ============================================
# NUEVO PROMEDIO (DESPUÉS DE ELIMINAR LA MÁS BAJA)
# ============================================

def new_average(qualifications):
    """
    Calcula el nuevo promedio después de modificar la lista.
    """
    prom = sum(qualifications) / len(qualifications)
    return prom


# ============================================
# SALIDA FORMATEADA (REPORTE DE CALIFICACIONES)
# ============================================

average = course_grade_average(qualification_list)
high, low = show_high_and_low(qualification_list)
top_3, bottom_3 = top_and_bottom_3(qualification_list)
top_count = count_top_score(qualification_list)

# ⚠️ hacemos copia para no dañar la original
updated_list = remove_lowest(qualification_list.copy())
new_avg = new_average(updated_list)

print("\n" + "="*40)
print("📊 REPORTE DE CALIFICACIONES")
print("="*40)

print(f"\n📌 Promedio general: {average:.2f}")

print(f"\n📈 Nota más alta: {high}")
print(f"📉 Nota más baja: {low}")

print(f"\n🏆  Top 3 calificaciones: {top_3}")
print(f"⚠️  Bottom 3 calificaciones: {bottom_3}")

print(f"\n🔁 Veces que se repite la nota más alta: {top_count}")

print("\n🧹 Después de eliminar la nota más baja:")
print(f"   Nueva lista: {updated_list}")
print(f"   Nuevo promedio: {new_avg:.2f}")

print("\n" + "="*40)