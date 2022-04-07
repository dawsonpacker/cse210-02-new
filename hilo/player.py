class Player: 

# Attributes: 
def __init__(self): 
	self.points = 300 

# Methods:
def guess_card_number(self):
    # prompts the user for an input of h or l to signify whether the player is guesing then next card will be higher or lower than the current card. 
    # then returns the value the player inputs. 
    guess = input('Higher or lower? [h/l]: ')
    return(guess)

