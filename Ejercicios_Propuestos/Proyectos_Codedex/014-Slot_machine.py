import random

# =========================
# SLOT MACHINE GAME 🎰
# =========================

# Lista de símbolos posibles
symbols = ['🍒', '🍇', '🍉', '7️⃣']


def play():
    """
    Función principal del juego.

    El jugador puede:
    - Presionar 'Y' para jugar.
    - Presionar 'N' para salir.

    El juego genera 3 símbolos aleatorios
    y verifica si el jugador obtuvo Jackpot.
    """

    # Se solicita la primera opción al usuario
    option = input('Ingresa "Y" para jugar o "N" para salir: ').upper()

    # El juego continuará mientras el usuario escriba Y
    while option == 'Y':

        # Genera 3 símbolos aleatorios
        result = random.choices(symbols, k=3)

        # Muestra el resultado en pantalla
        print(f'\n {result[0]} | {result[1]} | {result[2]} ')

        # =========================
        # VERIFICAR JACKPOT
        # =========================

        # Si los 3 símbolos son 7️⃣ → gana
        if result == ['7️⃣', '7️⃣', '7️⃣']:
            print('🎉 ¡Jackpot! 💰')
        else:
            print('❌ Intenta nuevamente')

        # =========================
        # PREGUNTAR SI DESEA CONTINUAR
        # =========================

        option = input(
            '\nIngresa "Y" para jugar otra vez o "N" para salir: '
        ).upper()

    # Si el usuario sale del juego
    print('\n👋 ¡Gracias por jugar!')


# =========================
# INICIAR JUEGO
# =========================

play()