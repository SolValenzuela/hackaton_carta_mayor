from card import Card
import random 

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []



        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( Card( s , i , str_val ) )
        self.shuffle()

    
    def shuffle(self):
        random.shuffle(self.cards)
    

    def get_card(self): # quita una carta del mazo y la devuelve
        card=self.cards.pop() 
        return card
    

    def get_cards(self, x=5):
        varias_cartas=[]
        for cartas in range(0,x):
            varias_cartas.append(self.cards.pop().show_point_val()) 
        return max(varias_cartas)
        




    
deck=Deck()
# print(deck.show_cards())




