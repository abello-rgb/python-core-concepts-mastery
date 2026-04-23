# ============================================
# EJERCICIO: PILAS (STACK) Y COLAS (QUEUE)
# ============================================
# Conceptos:
# - LIFO (Last In, First Out) → Pila
# - FIFO (First In, First Out) → Cola
# ============================================


# ============================================
# PILA (STACK) → LIFO
# ============================================

# Una pila funciona como una torre de platos:
# El último en entrar es el primero en salir

stack = []

# --------------------------------------------
# PUSH (agregar elementos)
# --------------------------------------------

stack.append('1')
stack.append('2')
stack.append('3')

# Estado actual:
# ['1', '2', '3']


# --------------------------------------------
# POP (eliminar último elemento)
# --------------------------------------------

# ❌ Forma manual (no recomendada)
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]

# print(stack_item)  # '3'

# ✔ Forma correcta y profesional
# pop() ya hace todo esto internamente
# print(stack.pop())  # elimina y retorna el último

# print(stack)


# ============================================
# COLA (QUEUE) → FIFO
# ============================================

# Una cola funciona como una fila:
# El primero en entrar es el primero en salir

queue = []

# --------------------------------------------
# ENQUEUE (agregar elementos)
# --------------------------------------------

queue.append('4')
queue.append('5')
queue.append('6')

# Estado:
# ['4', '5', '6']


# --------------------------------------------
# DEQUEUE (eliminar primer elemento)
# --------------------------------------------

# ❌ Esto funciona pero es ineficiente
print(queue.pop(0))

# Estado después:
print(queue)