juego = 'si'

while juego == 'si':
    print('Estoy jugando el juego')
    print('Ahora saca el jugador')
    carta_jugador = 1
    jugador = input('Quiere sacar otra carta')
    while jugador == 'si':
        print('saco otra carta')
        print('me fijo que onda las cartas')
        jugador = input('Queres otra carta?')
    juego = input('Quiere jugar de nuevo')