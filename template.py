############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint

def sacar_carta():
    '''
    Esta función toma una carta de un mazo de forma aleatoria. La carta está numerada del 1 al 10 (inclusive).

    params:
        Esta función no tiene parámetros de entrada.
    out:
        carta: int. El número de la carta sacada.
    '''
    carta = randint(1,10)
    return carta

######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################
usuario = sacar_carta()
crupier = sacar_carta()
banco = 500
comienzo = input('BIENVENIDO AL CASINO. QUERES ARRANCAR?: ')
while comienzo == 'si': 
    print(f'El Crupier sacó un {crupier} y tu carta es un {usuario}.')
    apuestapregunta = int(input)('Cuanto queres apostar?: ')
    if apuestapregunta  < banco:
        cartapregunta = input('Queres otra carta?: ')
        if cartapregunta == 'si':
            sacar_carta()
            lista = [usuario, ]
            print(f'Tus cartas son: {usuario} y {usuario2}, la suma total es:', sum(lista))
            if sum(lista) > 21:
                print('PERDISTE')
            elif sum(lista) <= 21 and sum(lista) > crupier:
                print('GANASTE')
        while cartapregunta == 'no':

 

    elif apuestapregunta == 'si':
        pregunta3 = int(input('Cuanto queres apostar?: '))
        if pregunta3 <= 500:
            apuesta = banco - pregunta3
            cartapregunta = input('Queres otra carta?: ')
            usuario2 = randint(1,10)
            lista = [usuario, usuario2]
            print(f'Tus cartas son: {usuario} y {usuario2}, la suma total es:', sum(lista))
            cartapregunta2 = input('Queres otra carta?: ')
        if cartapregunta2 == 'si':
            usuario3 = randint(1,10)
            lista.append(usuario3)
            print(f'Tus cartas son: {usuario}, {usuario2} y {usuario3}. La suma total es:', sum(lista))
            if sum(lista) > 21:
                print('Perdiste')
    else:
        print(f'Saldo insuficiente. Tu saldo actual es {banco}')
        








# while(): # Repetición del juego
#     #Tu código va acá
#     while(): # Turno del jugador
#         #Tu código va acá
#     while(): # Turno del crupier
    	#Tu código va acá
