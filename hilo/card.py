
class Card: 

    import random 

    # Attributes:
    # the number of the card that is currently displayed.  
    def __init__(self):
        self.current_card_number = 7
            
    # Methods: 

    def generate_next_card_number(self):
    # generates random number between 1 and 13 and returns that value  
        import random 
        next_card_number = random.randint(1, 13)
        return(next_card_number)
        
    def set_current_card_number(self, new_card_number): 
        self.current_card_number = new_card_number
    

