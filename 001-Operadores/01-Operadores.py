# ============================================
# OPERADORES Y ESTRUCTURAS DE CONTROL EN PYTHON
# ============================================
# Conceptos aplicados:
# - Operadores aritméticos
# - Operadores de comparación
# - Operadores lógicos
# - Operadores de asignación
# - Operadores de identidad y pertenencia
# - Operadores de bits
# - Estructuras de control (if, for, while)
# - Manejo de excepciones
# ============================================


# ============================================
# OPERADORES ARITMÉTICOS
# ============================================

# Realizan operaciones matemáticas básicas
print(f'Suma: 10 + 3 = {10 + 3}')
print(f'Resta: 10 - 3 = {10 - 3}')
print(f'Multiplicación: 10 * 3 = {10 * 3}')
print(f'División: 10 / 3 = {10 / 3}')  # Devuelve float
print(f'Módulo: 10 % 3 = {10 % 3}')    # Residuo
print(f'Exponente: 10 ** 3 = {10 ** 3}')
print(f'División entera: 10 // 3 = {10 // 3}')  # Sin decimales


# ============================================
# OPERADORES DE COMPARACIÓN
# ============================================

# Devuelven valores booleanos (True / False)
print(f'Igualdad: 10 == 3 es {10 == 3}')
print(f'Desigualdad: 10 != 3 es {10 != 3}')
print(f'Mayor que: 10 > 3 es {10 > 3}')
print(f'Menor que: 10 < 3 es {10 < 3}')
print(f'Mayor o igual que: 10 >= 3 es {10 >= 3}')
print(f'Menor o igual que: 10 <= 3 es {10 <= 3}')


# ============================================
# OPERADORES LÓGICOS
# ============================================

# Se usan para combinar condiciones
print(f'AND: (10 + 3 == 13 and 5 - 1 == 4) -> {10 + 3 == 13 and 5 - 1 == 4}')
print(f'OR:  (10 + 3 == 14 or 5 - 1 == 4) -> {10 + 3 == 14 or 5 - 1 == 4}')
print(f'NOT: not (10 + 3 == 14) -> {not (10 + 3 == 14)}')


# ============================================
# OPERADORES DE ASIGNACIÓN
# ============================================

# Permiten modificar el valor de una variable
my_number = 28
print(f'Valor inicial: {my_number}')

my_number += 1   # Suma y asigna
print(f'+= 1 → {my_number}')

my_number -= 1   # Resta y asigna
print(f'-= 1 → {my_number}')

my_number *= 2   # Multiplica y asigna
print(f'*= 2 → {my_number}')

my_number /= 2   # Divide (float)
print(f'/= 2 → {my_number}')

my_number //= 2  # División entera
print(f'//= 2 → {my_number}')

my_number **= 2  # Potencia
print(f'**= 2 → {my_number}')

my_number %= 2   # Módulo
print(f'%= 2 → {my_number}')


# ============================================
# OPERADORES DE IDENTIDAD
# ============================================

# Comparan si dos variables apuntan al mismo objeto en memoria
my_new_number = my_number

print(f'my_number is my_new_number -> {my_number is my_new_number}')
print(f'my_number is not my_new_number -> {my_number is not my_new_number}')


# ============================================
# OPERADORES DE PERTENENCIA
# ============================================

# Verifican si un elemento está dentro de una colección
print(f'"e" in "Breiner" -> {"e" in "Breiner"}')
print(f'"a" not in "Breiner" -> {"a" not in "Breiner"}')


# ============================================
# OPERADORES DE BITS
# ============================================

# Operan a nivel binario
a = 10  # 1010
b = 3   # 0011

print(f'AND: 10 & 3 = {10 & 3}')
print(f'OR: 10 | 3 = {10 | 3}')
print(f'XOR: 10 ^ 3 = {10 ^ 3}')
print(f'NOT: ~10 = {~10}')
print(f'Desplazamiento derecha: 10 >> 2 = {10 >> 2}')
print(f'Desplazamiento izquierda: 10 << 2 = {10 << 2}')


# ============================================
# ESTRUCTURAS DE CONTROL
# ============================================

# --------------------------------------------
# CONDICIONALES (if, elif, else)
# --------------------------------------------

my_string = 'Abello'

if my_string == 'Breiner':
    print(f'Bienvenido {my_string}')
elif my_string == 'Abello':
    print('Tu apellido coincide en la base de datos')
else:
    print('No tienes acceso, comunícate con un administrador')


# --------------------------------------------
# BUCLE FOR
# --------------------------------------------

# Itera sobre una secuencia
for i in range(11):  # 0 a 10
    print(i)


# --------------------------------------------
# BUCLE WHILE
# --------------------------------------------

# Se ejecuta mientras la condición sea verdadera
i = 0
while i <= 10:
    print(i)
    i += 1


# ============================================
# MANEJO DE EXCEPCIONES
# ============================================

try:
    # Código que puede fallar
    print(10 / 1)

except ZeroDivisionError:
    # Error específico
    print('No puedes dividir entre cero')

except Exception as e:
    # Error general
    print(f'Error inesperado: {e}')

finally:
    # Siempre se ejecuta
    print('Ha finalizado el manejo de excepciones')