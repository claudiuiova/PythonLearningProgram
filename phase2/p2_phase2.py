""" P2.  Create an automated card dealer for a Texas Hold’em application. It
should be able to handle Deck objects,  consisting of Cards. Cards can be
added or removed from Decks, and Decks can be shuffled and sorted.  When
dealing cards, each Player receives a Hand consisting of 2 Cards. After all
cards are dealt,  the Dealer should draw the table Hand of 5 Cards" """

import random

class Deck:     
	def __init__(self):         
		self.deck = self.createDeck()
		self.flag = True

	@staticmethod
	def createDeck():
		cardType = [' of Spades', ' of Hearts', ' of Clubs', ' of Diamonds']
		cardNames = ['Ace', 'Two', 'Three', 'For', 'Five', 'Six', 'Seven', 
    				'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
		return [cn + ct for cn in cardNames for ct in cardType]
	
	def removeCardFromDeck(self, cardToRemove):
		self.deck.remove(cardToRemove)
	
	def addCardToDeck(self, cardToAdd):
		self.deck.append(cardToAdd)
	
	def shuffleDeck(self):
		random.shuffle(self.deck)

	def getCards(self, numberOfCards):
		cards = []
		for i in range(numberOfCards):
			card = self.deck.pop(self.deck.index(self.deck[0]))
			cards.append(card)
		return cards

	def playGame(self):
		print('------------')
		print("Let's start!")
		print('------------')
		players = input("Insert players separated by ',': ").split(',')
		playersCards = []
		self.createDeck()
		self.shuffleDeck()
		
		for player in players:
			playerCards = self.getCards(2)
			playersCards.append({player: playerCards})
		
		restOfTheCards = self.getCards(3)

		for player in playersCards:
			player[list(player.keys())[0]] += restOfTheCards
			print(list(player.keys())[0])
			for card in player[list(player.keys())[0]]:
				print("************** " + card)

	def createMenu(self):
		while self.flag:
			print('================================')
			print('1. Play game!')
			print('2. Remove a card from the deck!')
			print('3. Add a card to the deck!')
			print('4. Shuffle the deck!')
			print('5. Sort deck!')
			print('Q/q. Exit!')

			userInput = input("Insert your choice: ")

			if userInput == '1':
				self.playGame()
				self.flag = False
			elif userInput == '2':
				cardToRemove = input("Insert the card: ")
				for card in self.deck:
					if cardToRemove.strip().lower() == card.lower():
						self.removeCardFromDeck(card)
						break
				print(self.deck)
			elif userInput == '3':
				cardToAdd = input("Insert a card: ")
				self.deck.append(cardToAdd.strip())
				print(self.deck)
			elif userInput.strip() == '4':
				self.shuffleDeck()
				print(self.deck)
			elif userInput.strip() == '5':
				self.deck = self.createDeck()
				print(self.deck)
			elif userInput == 'q' or userInput == 'Q':
				print('Good Bye!')
				self.flag = False
			else:
				print('================================')
				print("Nothing to do...!")

if __name__ == '__main__':     
	deck = Deck()
	deck.createMenu()