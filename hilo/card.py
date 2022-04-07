
Card: 

import random 

Attributes:
# the number of the card that is currently displayed.  
current_card_number = 7
		
Methods: 
generate_next_card_number:
# generates random number between 1 and 13 and returns that value  
    next_card_number = random.randint(1, 13)
    return(next_card_number)
    
 

