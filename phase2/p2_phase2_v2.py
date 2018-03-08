""" P2.  Create an automated card dealer for a Texas Hold’em application. It
should be able to handle Deck objects,  consisting of Cards. Cards can be
added or removed from Decks, and Decks can be shuffled and sorted.  When
dealing cards, each Player receives a Hand consisting of 2 Cards. After all
cards are dealt,  the Dealer should draw the table Hand of 5 Cards" """

import random

class Card(object):
	def __init__(self, val, suit):
		self.value = val
		self.suit = suit
	
	def show(self):
		print( "{} of {}".format(self.value, self.suit))

class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()
	
	def build(self):
		cardType = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
		cardNames = ['Ace', 'Two', 'Three', 'For', 'Five', 'Six', 'Seven', 
    				'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
		
		for cn in cardNames:
			for ct in cardType:
				self.cards.append(Card(cn, ct))
				
	def show_deck(self):
		for card in self.cards:
			card.show()

class Player(object):
	def __init__(self, name):
		self.name = name
		self.cards = []
	
	def show_hand(self):
		for card in self.cards:
			card.show()

class Dealer(object):
	def __init__(self):
		self.deck = Deck()
	
	def shuffle_deck(self):
		for i in range(len(self.deck.cards)-1, 0, -1):
			r = random.randint(0, i)
			self.deck.cards[i], self.deck.cards[r] = self.deck.cards[r], self.deck.cards[i]
	
	def draw_card(self):
		return self.deck.cards.pop()
	
	def sort_deck(self):
		self.deck = Deck()

class Game(object):
	def __init__ (self, *players):
		self.dealer = Dealer()
		self.list_with_players = [*players]

	def play_game(self):
		self.dealer.shuffle_deck()

		for player in self.list_with_players:
			for _ in range(2):
				player.cards.append(self.dealer.draw_card())
		
		print("----------------------")
		print("Let's play!")
		print("----------------------")
		print("Dealer: All players has a hand full of two cards.\n")
		print("Dealer: Draw the first card!\n")
		self.dealer.draw_card().show()
		print("--------------------------")
		print("Dealer: Draw the second card!\n")
		self.dealer.draw_card().show()
		print("--------------------------")
		print("Dealer: Draw the third card!\n")
		self.dealer.draw_card().show()
		print("--------------------------\n")

if __name__ == '__main__':     
	player1 = Player("Bob")
	player2 = Player("Victor")
	player3 = Player("Clau")

	game = Game(player1, player2, player3)
	game.play_game()
	print(player1.name)
	player1.show_hand()
	print('\n')
	print(player2.name)
	player2.show_hand()
	print('\n')
	print(player3.name)
	player3.show_hand()
