
def distance_to_miles(distance_in_km):
    # Paso 1: recibimos una distancia en kilómetros como argumento
    # Paso 2: calculamos la distancia equivalente en millas
    # usando la constante 1609 para la conversión
    miles = distance_in_km / 1609
    # Paso 3: devolvemos el resultado de la conversión
    return miles
my_distance_in_miles = distance_to_miles(10000)

print(my_distance_in_miles)
