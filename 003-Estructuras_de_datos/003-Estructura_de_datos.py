# ============================================
# ESTRUCTURAS DE DATOS EN PYTHON
# ============================================
# Conceptos aplicados:
# - Listas (mutables y ordenadas)
# - Tuplas (inmutables)
# - Sets (sin duplicados, no ordenados)
# - Diccionarios (clave - valor)
# - Operaciones básicas (CRUD)
# ============================================


# ============================================
# LISTAS (list)
# ============================================
# - Ordenadas
# - Mutables (se pueden modificar)
# - Permiten duplicados

my_list: list = [
    'Breiner',
    'Diana',
    'Aury',
    'Alex'
]

print(f'Lista inicial: {my_list}')


# --------------------------------------------
# AGREGAR ELEMENTOS
# --------------------------------------------

# append() agrega al final
my_list.append('Choky')
print(f'Después de append: {my_list}')


# --------------------------------------------
# ELIMINAR ELEMENTOS
# --------------------------------------------

# remove() elimina por valor
my_list.remove('Breiner')
print(f'Después de remove: {my_list}')


# --------------------------------------------
# ACTUALIZAR ELEMENTOS
# --------------------------------------------

# Acceder por índice (posición)
print(f'Elemento en posición 1: {my_list[1]}')

# Modificar valor
my_list[1] = 'Aurystela'
print(f'Después de actualizar: {my_list}')


# --------------------------------------------
# ORDENAR LISTA
# --------------------------------------------

# Ordena alfabéticamente (si son strings)
my_list.sort()
print(f'Lista ordenada: {my_list}')


# ============================================
# TUPLAS (tuple)
# ============================================
# - Ordenadas
# - Inmutables (NO se pueden modificar)
# - Permiten duplicados

my_tuple: tuple = (
    'Breiner',
    'Abello',
    '@bad997',
    '36'
)

# Acceso por índice
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])


# ⚠️ No puedes modificar directamente una tupla
# Pero puedes crear una nueva tupla ordenada
my_tuple = tuple(sorted(my_tuple))
print(f'Tupla ordenada: {my_tuple}')


# ============================================
# SETS (set)
# ============================================
# - NO ordenados
# - NO permiten duplicados
# - Mutables

my_set: set = {
    'Honda',
    '2005',
    'Picanto'
}

print(f'Tipo de dato: {type(my_set)}')


# --------------------------------------------
# AGREGAR Y ELIMINAR
# --------------------------------------------

my_set.add('Morado')
my_set.remove('Morado')


# ⚠️ IMPORTANTE:
# Un set NO es ordenado.
# Esto:
my_set = set(sorted(my_set))
# 👉 convierte a lista ordenada y luego a set,
# pero el set final NO garantiza orden real.

print(f'Set final: {my_set}')


# ============================================
# DICCIONARIOS (dict)
# ============================================
# - Estructura clave: valor
# - Mutables
# - Claves únicas

my_dict: dict = {
    'name': 'Susuky',
    'model': 'Camper',
    'year': '2018',
}


# --------------------------------------------
# INSERTAR
# --------------------------------------------

my_dict['email'] = 'breinerabello@gmail.com'


# --------------------------------------------
# ACCEDER
# --------------------------------------------

print(f"Nombre: {my_dict['name']}")


# --------------------------------------------
# MODIFICAR
# --------------------------------------------

my_dict['year'] = '2025'


# --------------------------------------------
# ELIMINAR
# --------------------------------------------

del my_dict['model']


# --------------------------------------------
# ORDENAR DICCIONARIO
# --------------------------------------------

# sorted() devuelve una lista de tuplas (clave, valor)
# Luego lo convertimos nuevamente a dict
my_dict = dict(sorted(my_dict.items()))

print(f'Diccionario final: {my_dict}')