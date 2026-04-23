# ============================================
# SISTEMA DE EMPLEADOS - POO EN PYTHON
# ============================================
# Conceptos aplicados:
# - Herencia
# - Composición
# - Polimorfismo
# - Encapsulamiento básico
# - Buenas prácticas (tipado y validaciones)
# ============================================


class Employee:
    """
    Clase base (padre) que representa a cualquier empleado.
    
    Atributos:
        id (int): Identificación del empleado
        name (str): Nombre del empleado
        employees (list): Lista de empleados a su cargo
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
        # Lista de subordinados (composición)
        self.employees: list[Employee] = []

    def add(self, employee: "Employee"):
        """
        Agrega un empleado a la lista de subordinados.

        Parámetros:
            employee (Employee): Objeto empleado a agregar
        """
        # Validación: evitar duplicados
        if employee in self.employees:
            print(f'{employee.name} ya está asignado a {self.name}')
            return
        
        self.employees.append(employee)

    def print_employees(self):
        """
        Imprime los nombres de todos los empleados a cargo.
        """
        if not self.employees:
            print(f'{self.name} no tiene empleados a su cargo')
            return

        print(f'Empleados a cargo de {self.name}:')
        for employee in self.employees:
            print(f' - {employee.name}')

    def __str__(self):
        """
        Representación en texto del objeto.
        """
        return f'Employee(id={self.id}, name={self.name})'


# ============================================
# CLASE MANAGER
# ============================================

class Manager(Employee):
    """
    Representa un gerente general.
    Hereda de Employee.
    """

    def cordinate_projects(self):
        """
        Acción específica del Manager.
        """
        print(f'{self.name} coordina todos los proyectos de la empresa')


# ============================================
# CLASE PROJECT MANAGER
# ============================================

class ProjectManager(Employee):
    """
    Representa un gerente de proyecto.

    Atributos adicionales:
        project (str): Nombre del proyecto asignado
    """

    def __init__(self, id: int, name: str, project: str):
        # Reutiliza el constructor del padre
        super().__init__(id, name)
        
        # Atributo propio
        self.project = project

    def cordinate_project(self):
        """
        Acción específica del Project Manager.
        """
        print(f'{self.name} coordina el {self.project}')

    def __str__(self):
        return f'ProjectManager(name={self.name}, project={self.project})'


# ============================================
# CLASE PROGRAMMER
# ============================================

class Programmer(Employee):
    """
    Representa un programador.

    Atributos adicionales:
        language (str): Lenguaje de programación
    """

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        """
        Acción principal del programador.
        """
        print(f'{self.name} está programando en {self.language}')

    # 🔴 POLIMORFISMO: sobrescribimos el método add
    def add(self, employee: Employee):
        """
        Un programador NO puede tener empleados a su cargo.
        """
        print(f'❌ Un programador no tiene empleados a su cargo. {employee.name} no se agregará')

    def __str__(self):
        return f'Programmer(name={self.name}, language={self.language})'


# ============================================
# CREACIÓN DE OBJETOS (INSTANCIAS)
# ============================================

my_manager = Manager(1152942566, 'Breiner')

my_project_manager1 = ProjectManager(36565645, 'Diana', 'Proyecto #1')
my_project_manager2 = ProjectManager(39595456, 'Aurys', 'Proyecto #2')

my_programmer1 = Programmer(1152945672, 'Leider', 'Python')
my_programmer2 = Programmer(1152944852, 'Henry', 'JavaScript')


# ============================================
# CONSTRUCCIÓN DE LA JERARQUÍA
# ============================================

# Manager → Project Managers
my_manager.add(my_project_manager1)
my_manager.add(my_project_manager2)

# Project Managers → Programmers
my_project_manager1.add(my_programmer1)
my_project_manager2.add(my_programmer2)

# ❌ Intento inválido (polimorfismo en acción)
my_programmer1.add(my_programmer2)


# ============================================
# EJECUCIÓN DE ACCIONES
# ============================================

# Programadores trabajando
my_programmer1.code()
my_programmer2.code()

# Coordinación de proyectos
my_project_manager1.cordinate_project()
my_manager.cordinate_projects()


# ============================================
# VISUALIZACIÓN DE LA ESTRUCTURA
# ============================================

my_manager.print_employees()
print()  # Separador visual
my_project_manager1.print_employees()