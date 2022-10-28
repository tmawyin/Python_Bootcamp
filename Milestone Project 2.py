# MILESTONE PROJECT 2
# BLACKJACK GAME

from random import shuffle
import os

suits = ("Hearts","Diamonds","Clubs","Spades")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}


# Class definitions

# Player class contains information about the player and initial amount to bet
class Player:
	def __init__(self,name="Player 1", amount=50):
		self.name = name
		self.amount = amount

	def bet_amount(self,chip):
		self.amount += chip


# Card class contains information about a single card
class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"

# Deck class contains a new deck of cards
class Deck:
	def __init__(self):
		self.all_cards = []
		for s in suits:
			for r in ranks:
				self.all_cards.append(Card(s,r))

	def shuffle(self):
		shuffle(self.all_cards)

	def remove_one(self):
		return self.all_cards.pop(0)

# Hand class contains actions at each hand
class Hand:
	def __init__(self):
		self.cards_on_hand = []
		self.bet = 0

	def add_card(self,card):
		self.cards_on_hand.append(card)

	def value_calc(self):
		value = 0
		aces = 0
		for card in self.cards_on_hand:
			value += card.value
			if card.rank == "Ace":
				aces += 1
		for i in range(aces):
			if value > 21:
				value -= 10
			else:
				continue
		return value

	def show_hand(self):
		for card in self.cards_on_hand:
			print(card)

	def ask_bet(self,ply_max):
		if ply_max == 0:
			print("Not enough funds to play \n")
		else:
			response = int(input("Place your bet (minimum $5): "))
			while (response > ply_max) or (response < 5):
				os.system("cls")
				print("Bet less, you don't have enough")
				response = int(input("Place your bet (minimum $5):: "))
			self.bet = response

	def ask_hit_stay(self):
		response = input("Hit(h) or Stay(s): ")
		while (response not in ["s","h"]):
			os.system("cls")
			print("Not valid response")
			response = input("Hit(h) or Stay(s): ")
		return response

	def __str__(self):
		val = self.value_calc()
		return f"-Hand value is {val}"

#-------------------------------------------------------------
os.system("cls")
# Game setup
ply_name = input("What is your name: ")
ply_cash = int(input("How much in chips: "))
print(f"\nWelcome {ply_name}, you have ${ply_cash} in chips")
print("\n")
player = Player(ply_name, ply_cash)


deck = Deck()
deck.shuffle()

# Game play
game_on = True
while game_on:
	# Initial Setup
	
	print("--GAME ON--")
	player_hand = Hand()
	dealer_hand = Hand()

	print("--Dealing--\n")
	player_hand.add_card(deck.remove_one())
	dealer_hand.add_card(deck.remove_one())
	player_hand.add_card(deck.remove_one())
	dealer_hand.add_card(deck.remove_one())

	print("Player Hand:")
	player_hand.show_hand()
	print(f"---Player at {player_hand.value_calc()}\n")
	print("\nDealer Hand:")
	print(dealer_hand.cards_on_hand[1])
	print("****** \n")

	player_hand.ask_bet(player.amount)
	if player_hand.bet == 0:
		break
	print(f"Player bets ${player_hand.bet} \n")
	
	
	busted = False
	while not busted:
		p_val = player_hand.value_calc()
		d_val = dealer_hand.value_calc()
		
		if p_val > 21:
			print("Busted! Dealer Wins!")
			player.bet_amount(-1*player_hand.bet)
			print(f"Player has ${player.amount}")
			busted = True
			break
		else:
			ply_choice = player_hand.ask_hit_stay()
			if ply_choice == "h":
				new_card = deck.remove_one()
				print(new_card)
				player_hand.add_card(new_card)
				print(f"Player at {player_hand.value_calc()}\n")
				continue
			else:
				os.system("cls")
				print(f"Player stays with {p_val}. Dearlers turn\n")
				player_hand.show_hand()
				print(f"---Player at {player_hand.value_calc()}\n")
				dealer_hand.show_hand()
				print(f"---Dealer at {dealer_hand.value_calc()}\n")
				
				# while dealer is less than player continue adding cards to dealer
				dealer_busted = False
				while not dealer_busted:
					if (dealer_hand.value_calc() >= player_hand.value_calc()) and dealer_hand.value_calc() <= 21:
						print(f"Dealer Wins! Dealer has {dealer_hand.value_calc()}")
						player.bet_amount(-1*player_hand.bet)
						print(f"Player has ${player.amount}")
						busted = True
						break
					elif (dealer_hand.value_calc() < player_hand.value_calc()) and dealer_hand.value_calc() <= 21: 
						dealer_hand.add_card(deck.remove_one())
						os.system("cls")
						print(f"Player stays with {p_val}. Dearlers turn\n")
						player_hand.show_hand()
						print(f"---Player at {player_hand.value_calc()}\n")
						dealer_hand.show_hand()
						print(f"---Dealer at {dealer_hand.value_calc()}\n")
					else:
						print("Dealer Busted! Player Wins!")
						player.bet_amount(+1*player_hand.bet)
						print(f"Player has ${player.amount}")
						dealer_busted = True
						busted = True
						break

	print("\n--GAME OVER--\n")

	if len(deck.all_cards) < 10:
		print("No more cards in deck!\n")
		reset_game = input("Would you like to reset the game (y or n)? ")
		if reset_game == "y":
			deck = Deck()
			deck.shuffle()
			continue
		else:
			game_on = False
			break
	play_again = input("Would you like to play again (y or n)? ")
	if play_again == "n":
		print(f"Player ends game with ${player.amount} \n")
		game_on = False
		break
	else:
		os.system("cls")
		continue
