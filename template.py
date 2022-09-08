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
cartas = sacar_carta()
comienzo = input('BIENVENIDO AL CASINO. QUERES ARRANCAR?: ')
while comienzo == 'si': 
    print(f'Crupier: {crupier} | Usuario: {usuario}.')
    # apuesta:
    apuestapregunta = (input)('Cuanto queres apostar?: ')
    if int(apuestapregunta)  <= banco:

        # pedido de cartas usuario:
        cartapregunta = input('Queres otra carta?: ')
        if cartapregunta == 'si':
            while (usuario <= 21) and (cartapregunta == 'si'):
                cartas = sacar_carta()
                usuario = usuario + cartas
                print(f'Nueva carta: {cartas}. Total Usuario: {usuario}')
                if usuario < 21:
                    cartapregunta = input('Queres pedir otra carta?: ')
            while (usuario == 21) and (usuario != crupier):
                print('Felicitaciones! Ganaste.')
            if (usuario > 21) or (usuario <= crupier):
                print('Perdiste!')
            elif (cartapregunta == 'no'):
                print(f'Te plantaste en {usuario}')
        else:
            print(f'Te plantaste en {usuario}')
        
        # pedido de cartas crupier:
        cartas = sacar_carta()
        crupier = crupier + cartas
        while (crupier < 16) or (crupier < 21) and (usuario > crupier):
            cartas = sacar_carta()
            crupier = crupier + cartas
            cuantocrupier = print(f'Nueva carta: {cartas}. Total Crupier: {crupier}')
            if crupier > 21:
                cuantocrupier = print('El Crupier se pasó de 21. Felicitaciones, ganaste.')
            elif (crupier <= 21) and (usuario < crupier):
                cuantocrupier = print('Gana el Crupier')
            
        #actualizacion del saldo
        if (usuario <= 21) and (usuario > crupier) or (crupier > 21) and (usuario <= 21):
            banco = banco + int(apuestapregunta)
            print(f'Ahora tu saldo es de ${banco}')
        elif (usuario > 21) or (crupier > usuario):
            banco = banco - int(apuestapregunta)
            print(f'Ahora tu saldo es de ${banco}')



    else:
        print(f'SALDO INSUFICIENTE, TU SALDO ES {banco}')