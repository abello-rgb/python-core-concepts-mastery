# ============================================
# HERENCIA Y POLIMORFISMO EN PYTHON
# ============================================
# Conceptos:
# - Clase base (Animal)
# - Clases hijas (Dog, Cat)
# - Sobrescritura de métodos (override)
# - Polimorfismo
# ============================================


# ============================================
# CLASE BASE (PADRE)
# ============================================

class Animal:
    """
    Clase base que representa un animal genérico.
    """

    def __init__(self, name):
        # Atributo común para todos los animales
        self.name = name

    def sound(self):
        """
        Método que debe ser implementado por las clases hijas.
        """
        pass  # No hace nada (método incompleto)


# ============================================
# CLASE HIJA: PERRO
# ============================================

class Dog(Animal):
    """
    Representa un perro.
    Hereda de Animal.
    """

    def sound(self):
        # Sobrescribe el método del padre
        print('Guau!')


# ============================================
# CLASE HIJA: GATO
# ============================================

class Cat(Animal):
    """
    Representa un gato.
    """

    def sound(self):
        # Sobrescribe el método del padre
        print('Miau!')


# ============================================
# FUNCIÓN POLIMÓRFICA
# ============================================

def print_sound(animal: Animal):
    """
    Recibe cualquier objeto tipo Animal
    y ejecuta su método sound().
    """
    animal.sound()


# ============================================
# EJECUCIÓN
# ============================================

# ❌ Objeto de la clase base
my_animal = Animal('Animal')
print_sound(my_animal)  # No imprime nada

# ✔ Objetos de clases hijas
my_dog = Dog('Choky')
print_sound(my_dog)

my_cat = Cat('Canelita')
print_sound(my_cat)