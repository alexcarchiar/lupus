######
#cards.py
#(c) alexcarchiar
#Code tailor made for lupus
######

roles_description = {
	"villager" : "they have no powers. They have to guess the wolves and vote them out during the day",
	"medium" : "he/she is called once every two turns. He/she can ask the narrator to reveal if one of the dead players was good or bad.",
	"foreseer" : "he/she is called once every two turns (usually when you don't call the Medium). He/she does the same thing as the Medium but only for players who are not dead yet.",
	"guard" : "he/she can choose one person every night to protect from the wolves, including him/herself. He/she cannot choose the same person two nights in a row.",
	"hunter" : "he/she has a rifle with one bullet and can use it once in the game to kill a player.",
	"prostitute" : "he/she decides one person to sleep with the night; if this person is a wolf he/she dies, otherwise nothing happens.",
	"mason" : "a group of people who know each other's role. In order to be effective there needs to be at least two of them.",
	"owl" : "he/she decides one person each turn who starts with two votes on his head.",
	"onionboy" : "a villager who smells like onion. It is just a joke character that has no special powers other than making my friends happy.",
	"cupid" : "he/she decides two lovers that will be bound for the rest of the game: if one dies, the other one dies too. The two lovers can also be both good guys, one good guy and a bad guy and both bad guys.",
	"sorcerer" : "he/she has two potions, both for a one time use. One is to revive someone from the dead, the other one is to instantly kill someone else.",
	"wolves" : "every night they are called and they decides who to devour (kill).",
	"wolf's son" : "he/she starts as a normal villager but if the wolves try and kill him/her, he/she does not die and becomes a wolf. He/she is then activated. From the Medium or Foreseer's perspective, the Wolf's son is always a bad guy. Note that, if the Wolf's son is not killed by the wolves during the night, he/she does not get activated.",
	"white wolf" : "a single wolf who is called once every two/threee turns (it depends on how many players are there) and has to kill all of the wolves and all of the good guys in order to win.",
	"wolf seer" : "it's just the wolves version of the foreseer."
}

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
		#if(self.alive == 1):
			#print("The player " + self.name + " is alive")
		#else:
			#print("The player " + self.name + " is dead")
		return self.alive

	def kill(self):
		self.alive = 0

	def revive(self):
		self.alive = 1

class deck:
	#all of the variables in the __init__ arejust integers that refer to the number of cards for that role
	def __init__(self, villager, medium, foreseer, guard, hunter, prostitute, mason, owl, onionboy, cupid, sorcerer, wolves, wolf_son, white_wolf, wolf_seer):
		self.villager = villager
		self.medium = medium
		self.forseer = foreseer
		self.guard = guard
		self.hunter = hunter
		self.prostitute = prostitute
		self.mason = mason
		self.owl = owl
		self.onionboy = onionboy
		self.cupid = cupid
		self.sorcerer = sorcerer
		self.wolves = wolves
		self.wolf_son = wolf_son
		self.white_wolf = white_wolf
		self.wolf_seer = wolf_seer
