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
mazo = sacar_carta()
comienzo = input('BIENVENIDO AL CASINO. QUERES ARRANCAR?: ')
while comienzo == 'si': 
    print(f'Crupier: {crupier} | Usuario: {usuario}.')
    # apuesta:
    apuestapregunta = (input)('Cuanto queres apostar?: ')
    if int(apuestapregunta)  < banco:

        # pedido de cartas usuario:
        cartapregunta = input('Queres otra carta?: ')
        if cartapregunta == 'si':
            while (usuario <= 21) and (cartapregunta == 'si'):
                mazo = sacar_carta()
                usuario = usuario + mazo
                print(f'Nueva carta: {mazo}. Total Usuario: {usuario}')
                if usuario < 21:
                    cartapregunta = input('Queres pedir otra carta?: ')
            while (usuario == 21) and (usuario != crupier):
                print('Felicitaciones! Ganaste.')
            if usuario > 21:
                print('Perdiste! Te pasaste de 21')
            elif (cartapregunta == 'no'):
                print(f'Te plantaste en {usuario}')
        else:
            print(f'Te plantaste en {usuario}')
        
        # pedido de cartas crupier:
        mazo = sacar_carta()
        crupier = crupier + mazo
        while (crupier < 16) or (crupier < 21) and (usuario > crupier):
            mazo = sacar_carta()
            crupier = crupier + mazo
            cuantocrupier = print(f'Nueva carta: {mazo}. Total Crupier: {crupier}')
            if crupier > 21:
                cuantocrupier = print('El Crupier se pasó de 21. Felicitaciones, ganaste.')
            

        if (usuario <= 21) and (usuario > crupier) or (crupier > 21) and (usuario <= 21):
            banco = banco + int(apuestapregunta)
            print(f'Ganaste, ahora tu saldo es de ${banco}')
        elif (usuario > 21) or (crupier > usuario):
            banco = banco - int(apuestapregunta)
            print(f'Perdiste, ahora tu saldo es de ${banco}')


    else:
        print(f'SALDO INSUFICIENTE, TU SALDO ES {banco}')


    # while (usuario<= 21) and (usuario>crupier):
    #     print('GANASTE')

        #     if sum(lista) > 21:
        #         print('PERDISTE')
        #     elif sum(lista) <= 21 and sum(lista) > crupier:
        #         print('GANASTE')
        # while cartapregunta == 'no':

 

    # elif apuestapregunta == 'si':
    #     pregunta3 = int(input('Cuanto queres apostar?: '))
    #     if pregunta3 <= 500:
    #         apuesta = banco - pregunta3
    #         cartapregunta = input('Queres otra carta?: ')
    #         usuario2 = randint(1,10)
    #         lista = [usuario, usuario2]
    #         print(f'Tus cartas son: {usuario} y {usuario2}, la suma total es:', sum(lista))
    #         cartapregunta2 = input('Queres otra carta?: ')
    #     if cartapregunta2 == 'si':
    #         usuario3 = randint(1,10)
    #         lista.append(usuario3)
    #         print(f'Tus cartas son: {usuario}, {usuario2} y {usuario3}. La suma total es:', sum(lista))
    #         if sum(lista) > 21:
    #             print('Perdiste')
    # else:
    #     print(f'Saldo insuficiente. Tu saldo actual es {banco}')


