stock_prices = [
    34.68,  36.09, 
    34.94,  33.97, 
    34.68,  35.82, 
    43.41,  44.29, 
    44.65,  53.56,
    49.85,  48.71, 
    48.71,  49.94, 
    48.53,  47.03, 
    46.59,  48.62, 
    44.21,  47.21
]


def price_at(x):
    price_x_day = stock_prices[x - 1]
    return price_x_day



def max_price(a, b):
    """
    Devuelve el precio máximo entre los días a y b, ambos inclusive.

    Parámetros:
    a -- día inicial (1 a 20)
    b -- día final (1 a 20)

    Reglas:
    - Los días se reciben en formato humano: 1, 2, 3...
    - La lista usa índices de Python: 0, 1, 2...
    """

    # Validación básica
    if a < 1 or b > len(stock_prices) or a > b:
        raise ValueError("a y b deben estar entre 1 y 20, y a no puede ser mayor que b")

    # Convertimos días humanos a índices de Python
    inicio = a - 1
    fin = b

    # Tomamos el tramo desde el día a hasta el día b
    tramo = stock_prices[inicio:fin]

    # Suponemos que el primero es el mayor
    maximo = tramo[0]

    # Recorremos el tramo para buscar un valor más grande
    for precio in tramo:
        if precio > maximo:
            maximo = precio

    return maximo

def min_price(a, b):
    # Validación básica
    if a < 1 or b > len(stock_prices) or a > b:
        raise ValueError("a y b deben estar entre 1 y 20, y a no puede ser mayor que b")

    # Convertimos días humanos a índices de Python
    inicio = a - 1
    fin = b

    # Tomamos el tramo desde el día a hasta el día b
    tramo = stock_prices[inicio:fin]

    # Suponemos que el primero es el menor
    minimo = tramo[0]

    # Recorremos el tramo para buscar un valor más pequeno
    for precio in tramo:
        if precio < minimo:
            minimo = precio

    return minimo
    
print(price_at(12))
print(max_price(1,2))
print(min_price(5,6))
