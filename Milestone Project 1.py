# MILESTONE PROJECT 1
# TIC TAC TOE GAME

'''
What needs to be done:
- Ask user to choose a position for x and o
- Print the board with the position played
- Check if there is a winner
- Repeat if no winner
'''

import os

# Draws empty board
def empty_board():
	up  = [" ", " ", " "]
	mid = [" ", " ", " "]
	low = [" ", " ", " "]

	print(" | ".join(up))
	print('---------')
	print(" | ".join(mid))
	print('---------')
	print(" | ".join(low))
	print(" ")

# Drawing board with X and O
def draw_board(x=[],o=[]):
	up  = [" ", " ", " "]
	mid = [" ", " ", " "]
	low = [" ", " ", " "]

	for val in x:
		if val == 1 or val == 2 or val == 3:
			up = write_val("X", val, up)
		elif val == 4 or val == 5 or val == 6:
			mid = write_val("X", val-3, mid)
		else:
			low = write_val("X", val-6, low)

	for val in o:
		if val == 1 or val == 2 or val == 3:
			up = write_val("O", val, up)
		elif val == 4 or val == 5 or val == 6:
			mid = write_val("O", val-3, mid)
		else:
			low = write_val("O", val-6, low)

	print(" | ".join(up))
	print('---------')
	print(" | ".join(mid))
	print('---------')
	print(" | ".join(low))
	print(" ")

def write_val(val, pos, pos_lst):
	pos_lst[pos-1] = val
	return pos_lst

# Check if position is taken
def pos_check(num, all_vals):
	return num in set(all_vals)

# Asking for player's input
def ask_user(plyr, all_vals):
	val = input(f'Choose a position for {plyr}: ')

	while not val.isdigit() or int(val) not in range(1,10) or pos_check(int(val), all_vals):
		os.system("cls")
		print("Your input is incorrect or already used, please try again")
		val = input(f'Choose a position for {plyr}: ')

	return int(val)

# Check if someone won the game
def check_win(plyr, pos_lst):
	win_sets = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
	for s in win_sets:
		if set(pos_lst).issuperset(s):
			print("---------------------------")
			print(f"Player {plyr} has won! Good job!")
			print("---------------------------")
			return True
	return False

# Check if there is a tie
def check_tie(all_vals):
	if len(all_vals) == 9:
		print("----------------------")
		print("Good Game - it's a tie")
		print("----------------------")
		return True



# ------------- MAIN GAME ---------------
win = False
x = []
o = []
all_vals = []

draw_board()

while not win:
	# Player O
	o_val = ask_user("O", all_vals)
	o.append(o_val)
	all_vals.append(o_val)
	
	# Re-draw the board
	os.system('cls')
	draw_board(x, o)

	# Check if there is a winner or a tie
	if check_win("O",o) or check_tie(all_vals):
		win = True
		break

	# Player X 
	x_val = ask_user("X", all_vals)
	x.append(x_val)
	all_vals.append(x_val)
	
	# Re-draw the board
	os.system('cls')
	draw_board(x, o)

	# Check if there is a winner or a tie
	if check_win("X", x) or check_tie(all_vals):
		win = True
		break

print(" ")