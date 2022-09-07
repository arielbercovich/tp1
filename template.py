############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint
from re import A

# def sacar_carta():
#     '''
#     Esta función toma una carta de un mazo de forma aleatoria. La carta está numerada del 1 al 10 (inclusive).

#     params:
#         Esta función no tiene parámetros de entrada.
#     out:
#         carta: int. El número de la carta sacada.
#     '''
#     carta = randint(1,10)
#     return carta
    


######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################
usuario = randint(1, 10)
crupier = randint (1,10)
banco = 500
print('BIENVENIDO AL CASINO. EMPIEZA EL JUEGO')
print(f'El Crupier sacó un {crupier} y tu carta es un {usuario}.')
apuestapregunta = input('Queres apostar?: ')
if apuestapregunta == 'no':
    cartapregunta = input('Queres otra carta?: ')
    if cartapregunta == 'si':
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
