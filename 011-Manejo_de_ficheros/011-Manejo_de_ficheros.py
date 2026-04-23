import os

# ============================================
# MANEJO DE ARCHIVOS + CRUD EN PYTHON
# ============================================
# Conceptos:
# - Escritura y lectura de archivos
# - Uso de "with open"
# - Persistencia básica (tipo base de datos)
# - CRUD (Create, Read, Update, Delete)
# - Procesamiento de strings
# ============================================


# ============================================
# EJERCICIO BÁSICO (CREAR, LEER, ELIMINAR)
# ============================================

file_name = "mouredev.txt"

# --------------------------------------------
# ESCRITURA (modo "w" → sobrescribe archivo)
# --------------------------------------------
with open(file_name, "w") as file:
    file.write("Brais Moure\n")
    file.write("36\n")
    file.write("Python")

# --------------------------------------------
# LECTURA
# --------------------------------------------
with open(file_name, "r") as file:
    print(file.read())

# --------------------------------------------
# ELIMINACIÓN
# --------------------------------------------
os.remove(file_name)


# ============================================
# EXTRA: SISTEMA DE TIENDA (CRUD)
# ============================================

file_name = "breiner_shop.txt"

# Crear archivo si no existe
open(file_name, "a").close()


while True:

    # ----------------------------------------
    # MENÚ
    # ----------------------------------------
    print("\n===== TIENDA =====")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")


    # ========================================
    # 1. CREAR (ADD)
    # ========================================
    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")

        # Guardamos como texto separado por coma
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")


    # ========================================
    # 2. LEER (READ)
    # ========================================
    elif option == "2":
        name = input("Nombre: ")

        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(f'Producto encontrado: {line.strip()}')
                    break
            else:
                print("Producto no encontrado")


    # ========================================
    # 3. ACTUALIZAR (UPDATE)
    # ========================================
    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")

        with open(file_name, "r") as file:
            lines = file.readlines()

        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)


    # ========================================
    # 4. ELIMINAR (DELETE)
    # ========================================
    elif option == "4":
        name = input("Nombre: ")

        with open(file_name, "r") as file:
            lines = file.readlines()

        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)


    # ========================================
    # 5. MOSTRAR TODO
    # ========================================
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())


    # ========================================
    # 6. TOTAL DE VENTAS
    # ========================================
    elif option == "6":
        total = 0

        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.strip().split(", ")

                quantity = int(components[1])
                price = float(components[2])

                total += quantity * price

        print(f'Total ventas: {total}')


    # ========================================
    # 7. TOTAL POR PRODUCTO
    # ========================================
    elif option == "7":
        name = input("Nombre: ")
        total = 0

        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.strip().split(", ")

                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])

                    total += quantity * price
                    break

        print(f'Total de {name}: {total}')


    # ========================================
    # 8. SALIR
    # ========================================
    elif option == "8":
        os.remove(file_name)
        print("Archivo eliminado. Saliendo...")
        break


    # ========================================
    # OPCIÓN INVÁLIDA
    # ========================================
    else:
        print("Selecciona una opción válida.")