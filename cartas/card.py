class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val
    

    def show_point_val(self):
        card_point=self.point_val
        return card_point
    

    # def show_cards(self):
    #     for card in self.cards:
    #         card.card_info()
        
        
    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

