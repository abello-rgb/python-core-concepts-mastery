# ============================================
# OPERACIONES CON CADENAS (STRINGS) EN PYTHON
# ============================================
# Conceptos aplicados:
# - Concatenación y repetición
# - Indexación y slicing
# - Métodos de búsqueda y reemplazo
# - Transformaciones de texto
# - Conversión de tipos
# - Validaciones de contenido
# ============================================


# ============================================
# VARIABLES INICIALES
# ============================================

s1 = 'Hola'
s2 = 'Python'


# ============================================
# CONCATENACIÓN
# ============================================

# Une cadenas de texto
print(s1 + ', ' + s2 + '!')


# ============================================
# REPETICIÓN
# ============================================

# Repite la cadena n veces
print(s1 * 3)


# ============================================
# INDEXACIÓN
# ============================================

# Acceso a caracteres por posición (índice inicia en 0)
print(s1[0] + s1[1] + s1[2] + s1[3])


# ============================================
# LONGITUD
# ============================================

# len() devuelve la cantidad de caracteres
print(len(s2))


# ============================================
# SLICING (SUBCADENAS)
# ============================================

# [inicio:fin] (fin no incluido)
print(s2[2:6])   # 'thon'
print(s2[2:])    # desde índice 2 hasta el final
print(s2[0:2])   # primeros 2 caracteres
print(s2[:2])    # equivalente a [0:2]


# ============================================
# BÚSQUEDA
# ============================================

# Verifica si existe un substring
print('Ho' in s1)   # True
print('i' in s1)    # False


# ============================================
# REEMPLAZO
# ============================================

# replace() sustituye caracteres
print(s1.replace('o', 'a'))  # 'Hala'


# ============================================
# DIVISIÓN (SPLIT)
# ============================================

# Divide la cadena en una lista
print(s2.split('t'))  # ['Py', 'hon']


# ============================================
# TRANSFORMACIÓN DE TEXTO
# ============================================

print(s1.upper())                    # MAYÚSCULAS
print(s2.lower())                    # minúsculas
print('breiner abello'.title())     # Cada palabra inicia en mayúscula
print('breiner abello'.capitalize())# Solo primera letra en mayúscula


# ============================================
# ELIMINAR ESPACIOS
# ============================================

print(' Ingeniero de sistemas '.strip() + ' @DevEnProceso')


# ============================================
# BÚSQUEDA POR POSICIÓN INICIAL/FINAL
# ============================================

print(s1.startswith('Ho'))   # True
print(s1.startswith('Py'))   # False
print(s1.endswith('la'))     # True
print(s1.endswith('thon'))   # False


# ============================================
# BÚSQUEDA DE POSICIÓN
# ============================================

s3 = 'Breiner Abello @breinerabello'

# find() devuelve índice o -1 si no encuentra
print(s3.find('breiner'))     # sensible a mayúsculas → puede ser -1
print(s3.find('abello'))
print(s3.find('B'))

# Convertimos a minúsculas para búsqueda flexible
print(s3.lower().find('a'))


# ============================================
# CONTEO DE OCURRENCIAS
# ============================================

print(s3.lower().count('a'))


# ============================================
# FORMATEO DE STRINGS
# ============================================

# Método clásico
print('Saludo: {} , lenguaje: {} !'.format(s1, s2))

# Método moderno (recomendado)
print(f'Saludo: {s1} , lenguaje: {s2} !')


# ============================================
# TRANSFORMACIÓN STRING ↔ LISTA
# ============================================

# String → lista de caracteres
print(list(s3))

# Lista → string
l1 = [s1, ',', s2, '!']
print(''.join(l1))


# ============================================
# TRANSFORMACIONES NUMÉRICAS
# ============================================

# String → entero
s4 = '123456'
s4 = int(s4)
print(type(s4))

# String → float
s5 = '123456.515'
s5 = float(s5)
print(type(s5))


# ============================================
# VALIDACIONES DE CONTENIDO
# ============================================

s4 = '123456'

print(s1.isalnum())   # Solo letras y números
print(s1.isalpha())   # Solo letras
print(s4.isalpha())   # False
print(s4.isnumeric()) # Solo números