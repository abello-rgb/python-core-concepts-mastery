# ============================================
# CLASE PROGRAMMER (ATRIBUTOS Y MÉTODOS)
# ============================================
# Conceptos:
# - Atributos de clase vs instancia
# - Constructor (__init__)
# - Modificación de atributos
# - Métodos de instancia
# ============================================


class Programmer:
    """
    Representa un programador.

    Atributos de clase:
        surname (str): Apellido compartido por defecto (puede ser sobrescrito)

    Atributos de instancia:
        name (str): Nombre del programador
        age (int): Edad
        lenguages (list): Lista de lenguajes de programación
    """

    # ============================================
    # ATRIBUTO DE CLASE
    # ============================================
    # Este valor es compartido por TODAS las instancias
    surname: str = None

    def __init__(self, name: str, age: int, lenguages: list):
        """
        Constructor de la clase.

        Se ejecuta automáticamente al crear un objeto.
        """
        self.name = name
        self.age = age
        self.lenguages = lenguages  # ⚠️ lista = tipo mutable

    def print(self):
        """
        Muestra la información del programador.
        """
        print(
            f'Nombre: {self.name} / '
            f'Apellido: {self.surname} / '
            f'Edad: {self.age} / '
            f'Lenguajes: {self.lenguages}'
        )


# ============================================
# CREACIÓN DE OBJETO
# ============================================

my_programmer = Programmer('Breiner', 28, ['Python', 'JavaScript'])

# Primera impresión
my_programmer.print()


# ============================================
# MODIFICACIÓN DE ATRIBUTO DE CLASE (A NIVEL INSTANCIA)
# ============================================

# Aquí NO modificas el atributo de clase global,
# creas un atributo de instancia con el mismo nombre
my_programmer.surname = 'Abello'

my_programmer.print()


# ============================================
# MODIFICACIÓN DE ATRIBUTOS DE INSTANCIA
# ============================================

my_programmer.age = 29
my_programmer.print()