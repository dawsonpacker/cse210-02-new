 
import random
from player import Player
from card import Card


def main(): 

	player = Player()

	card = Card()
	
	want_to_play_game = 'y'

	

	want_to_play_game = 'y'

	while player.points > 0 and want_to_play_game == 'y': 
		print()
		print(f'The card is {card.current_card_number}')
		guess = player.guess_card_number()
		next_card_number = card.generate_next_card_number()
		print(f'Next card was: {next_card_number}')

		
		if guess == 'h' and next_card_number > card.current_card_number or guess == 'l' and next_card_number < card.current_card_number: 
			player.points += 100

		elif (guess == 'h' and next_card_number < card.current_card_number) or (guess == 'l' and next_card_number > card.current_card_number): 
			player.points -= 100
		print(f'Your score is: {player.points}')

		card.set_current_card_number(next_card_number)
		want_to_play_game = input('Play again? [y/n]: ')





		if want_to_play_game == 'n' or player.points < 0: 
			print('game over')
			
	



if __name__ == '__main__':
	main()
