from card import Card
from deck import Deck


while True:
    respuesta=input('En éste juego se cada jugador recibe una carta.Desea jugar? s/n: ')
    if respuesta != 's':
        print ('gracias por participar')
        break

    deck = Deck()
    
    carta_cpu=deck.get_card().show_point_val()
    print(f'La computadora eligió : {carta_cpu}\n')
    carta_humano=deck.get_card().show_point_val()
    print(f'El humano eligió :{carta_humano} \n')

    if carta_humano > carta_cpu:
        print('El humano ha ganado')
    else:
        print ('La computadora ha ganado')
    

while True:
    respuesta=input('En éste juego se reparten 5 cartas.Desea jugar? s/n: ')
    if respuesta != 's':
        print ('gracias por participar')
        break

    deck = Deck()
    
    cartas_del_computador=deck.get_cards()
    print(f'La computadora eligió : {cartas_del_computador}\n')
    cartas_del_jugador=deck.get_cards()
    print(f'El humano eligió :{cartas_del_jugador} \n')

    if cartas_del_jugador > cartas_del_computador:
        print(f'El jugador ha ganado')
    else:
        print ('La computadora ha ganado')






