/*
cards.py
(c) alexcarchiar
Code tailor made for lupus
*/

class Card:
	def __init__(role, ide):
		self.role = role #determines the role of a card
		self.id = ide #determines the unique id of a card

	def role(self):
		return self.role

	def ide(self):
		return self.id

class Player:
	def __init__(name):
		self.name = name
		self.alive = 1
		self.card = None

	def give_card(self, card):
		self.card = card

	def show_card(self):
		print("The player is a" + self.card.role + " . The card's id is: " + self.card.id)

	def is_alive(self):
		if(self.alive == 1):
			#print("The player " + self.name + " is alive")
		else:
			#print("The player " + self.name + " is dead")
		return self.alive

	def kill(self):
		self.alive = 0

	def revive(self):
		self.alive = 1