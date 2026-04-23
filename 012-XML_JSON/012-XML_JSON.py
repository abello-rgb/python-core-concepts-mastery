import os
import xml.etree.ElementTree as xml
import json

# ============================================
# DATOS BASE
# ============================================

data = {
    "name": "Brais Moure",
    "age": 36,
    "birth_date": "29-04-1987",
    "programming_languages": ["Python", "Kotlin", "Swift"]
}

xml_file = "mouredev.xml"
json_file = "mouredev.json"


# ============================================
# XML - CREACIÓN
# ============================================

def create_xml():
    """
    Convierte el diccionario 'data' en un archivo XML.
    """

    # Nodo raíz
    root = xml.Element("data")

    # Recorrer el diccionario
    for key, value in data.items():
        child = xml.SubElement(root, key)

        # Si es lista → crear múltiples nodos
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            # Convertimos a string (XML solo guarda texto)
            child.text = str(value)

    # Crear árbol y guardarlo en archivo
    tree = xml.ElementTree(root)
    tree.write(xml_file)


create_xml()

# --------------------------------------------
# LECTURA XML
# --------------------------------------------
with open(xml_file, "r") as xml_data:
    print(xml_data.read())

# Eliminar archivo
os.remove(xml_file)


# ============================================
# JSON - CREACIÓN
# ============================================

def create_json():
    """
    Guarda el diccionario 'data' en formato JSON.
    """
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)


create_json()

# --------------------------------------------
# LECTURA JSON
# --------------------------------------------
with open(json_file, "r") as json_data:
    print(json_data.read())

# Eliminar archivo
os.remove(json_file)


# ============================================
# EXTRA: CONVERSIÓN A OBJETOS
# ============================================

# Volvemos a crear archivos
create_xml()
create_json()


class Data:
    """
    Clase para representar los datos como objeto.
    """

    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages


# ============================================
# LECTURA XML → OBJETO
# ============================================

with open(xml_file, "r") as xml_data:

    # Parsear XML
    root = xml.fromstring(xml_data.read())

    # Extraer datos
    name = root.find("name").text
    age = int(root.find("age").text)  # ✔ convertir a int
    birth_date = root.find("birth_date").text

    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    # Crear objeto
    xml_class = Data(name, age, birth_date, programming_languages)

    print(xml_class.__dict__)


# ============================================
# LECTURA JSON → OBJETO
# ============================================

with open(json_file, "r") as json_data:

    json_dict = json.load(json_data)

    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["programming_languages"]
    )

    print(json_class.__dict__)


# ============================================
# LIMPIEZA FINAL
# ============================================

os.remove(xml_file)
os.remove(json_file)