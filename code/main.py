'''
main.py
(c) alexcarchiar
Code tailor made for lupus
'''
import cards

def show_rules():
	print("""Made by alexcarchiar

Intro
The game is simple: there is one narrator who needs to coordinate the game, give everyone their roles and make sure nobody cheats. At the same time, he will be the moderator during the day and will call out the roles during the night.

There are two phases: the day and the night. During the night, everyone "sleeps" (closes his/her eyes) and the narrator calls out the roles and asks them to do what they are supposed to. During the day, people need to cast their votes and decide who is a "lupus" (wolf in latin). The game ends when either the good ones or the bad ones win.

Roles
Good guys
The good guys win when there are no wolves left. These are the roles:

Villager: they have no powers. They have to guess the wolves and vote them out during the day.
Medium: he/she is called once every two turns. He/she can ask the narrator to reveal if one of the
dead players was good or bad.
Foreseer: he/she is called once every two turns (usually when you don't call the Medium). He/she does the same thing as the Medium but only for players who are not dead yet.
Guard: he/she can choose one person every night to protect from the wolves, including him/herself. He/she cannot choose the same person two nights in a row.
Hunter: he/she has a rifle with one bullet and can use it once in the game to kill a player.
Prostitute: he/she decides one person to sleep with the night; if this person is a wolf he/she dies, otherwise nothing happens.
Mason: a group of people who know each other's role. In order to be effective there needs to be at least two of them.
Owl: he/she decides one person each turn who starts with two votes on his head.
Onionboy: a villager who smells like onion. It is just a joke character that has no special powers other than making my friends happy.
Cupid: he/she decides two lovers that will be bound for the rest of the game: if one dies, the other one dies too. The two lovers can also be both good guys, one good guy and a bad guy and both bad guys.
Sorcerer: he/she has two potions, both for a one time use. One is to revive someone from the dead, the other one is to instantly kill someone else.
Bad guys
The bad guys win when the wolves outnumber the good guys.

Wolves: every night they are called and they decides who to devour (kill).
Wolf's son: he/she starts as a normal villager but if the wolves try and kill him/her, he/she does not die and becomes a wolf. He/she is then activated. From the Medium or Foreseer's perspective, the Wolf's son is always a bad guy. Note that, if the Wolf's son is not killed by the wolves during the night, he/she does not get activated.
White wolf: a single wolf who is called once every two/threee turns (it depends on how many players are there) and has to kill all of the wolves and all of the good guys in order to win.
Wolf seer: it's just the wolves version of the foreseer.
Additional comments
There very few rules:

Ghosts (dead people) can't talk, or at least not about the game. They may open their eyes during the night but this must be explicitly agreed upon the beginning of a game. (of course, if the sorcerer is playing, we recommend the ghosts don't open their eyes).
No talking during the night.
In case of a draw, there needs to be a runoff where you can vote only for the two (or three) people with most votes.""")

roles_numbers = {
	"villager" : 0,
	"medium" : 0,
	"foreseer" : 0,
	"guard" : 0,
	"hunter" : 0,
	"prostitute" : 0,
	"mason" : 0,
	"owl" : 0,
	"onionboy" : 0,
	"cupid" : 0,
	"sorcerer" : 0,
	"wolves" : 0,
	"wolf's son" : 0,
	"white wolf" : 0,
	"wolf seer" : 0

}

def main():
	global roles_numbers
	choice = None
	print("Welcome to werewolves by alexcarchiar.\nThis program is used to help the narrator do his job, especially when there are no cards laying around")
	choice = str(input("Do you need to see the rules? Y\\N?"))
	if(choice == "Y" or choice == "y"):
		show_rules()
	print("You now have to give the numbers of the cards")
	for key in roles_numbers:
		roles_numbers[key] = int(input(key + ": "))

	'''print("\n")
	for key in roles_numbers:
		print(roles_numbers[key])
	'''
	deck = cards.Deck(roles_numbers["villager"], roles_numbers["medium"], roles_numbers["foreseer"], roles_numbers["guard"], roles_numbers["hunter"], roles_numbers["prostitute"], roles_numbers["mason"], roles_numbers["owl"], roles_numbers["onionboy"], roles_numbers["cupid"], roles_numbers["sorcerer"], roles_numbers["wolves"], roles_numbers["wolf's son"], roles_numbers["white wolf"], roles_numbers["wolf seer"])

	players = []
	for i in range(0,deck.num_cards):
		print("Player num: " + str(i+1))
		name = str(input("Name: "))
		players.append(cards.Player(name, i))
		print("")

main()
