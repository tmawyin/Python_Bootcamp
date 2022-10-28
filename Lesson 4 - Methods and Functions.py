# Methods & Functions

# --- METHODS ---
mylist = [1,2,3]

# Get help on a particular method of a list 
help(mylist.insert)

mylist.insert(0,0)
print(mylist)

print('----')

# --- FUNCTIONS ---
# use "def" and "return" to generate functions

def say_hello(name = 'You'):
	print('hello ' + name)

say_hello('Tom')
say_hello()

print('----')

# Function to check if number is even 
def is_even(num):
	return num % 2 == 0

print(is_even(2))
print(is_even(3))

print('----')

# Example --- Ball & Cup game using functions
from random import shuffle


# Create a function that shuffle items in a list
def shuffle_list(mylist=[]):
	shuffle(mylist)
	return mylist

# Game list
game_list =["","O",""]

# Asking the user to guess index
def player_guess():
	guess = ''
	while guess not in ['0','1','2']:
		guess = input("Pick a number: 0, 1, or 2 --")

	return int(guess)


def check_guess(my_list, guess):
	if my_list[guess] == 'O':
		print("You Win!")
		print(my_list)
	else:
		print("Try again")
		print(my_list)


# - Run code below to play:
# game_list = shuffle_list(game_list)
# guess = player_guess()
# check_guess(game_list, guess)

print('-----')

# --- *args & **kwargs ---
# *args allows to have multiple inputs to a function as parameters
# *args are passed as tupple of arguments
def myfunc(*args):
	return sum(args)

print(myfunc(10,20))
print(myfunc(10,20,4,50,10))
print(myfunc(10,20,30,40,50,60,70,80,90,100))

print('-----')

# **kwargs is similar to *args but passes as a dictionary
def fruit_func(**kwargs):
	if 'fruit' in kwargs:
		print('my fruit of choice is ' + kwargs['fruit'])
	else:
		print('no fruits were found')

fruit_func(fruit="mango", veggie="avocado")

print('----')

# Function to upper and lower case alternate letters in a string
def myfunc(string):
	new_str =''
	for index, letter in enumerate(string):
		print(index)
		if index % 2 == 0:
			new_str += string[index].lower()
		else:
			new_str += string[index].upper()
	return new_str

print(myfunc("hello"))
print('-----')

nums = [1,2,4,0,0,7,5]
nums = [1,7,2,0,4,5,0]
nums = [0,7,2,6,4,5,1]

def spy_game(nums):
	count = 0
	for i, v in enumerate(nums):
		if v == 7:
			found_seven = True
			pos_seven = i
		if v == 0:
			found_zero = True
			pos_zero = i
			count += 1

	if pos_seven > pos_zero and count >= 2:
		return True
	else:
		return False

print(spy_game(nums))
print('-----')

# --- LAMBDA EXPRESSIONS - MAP & FILTER ---
def square(num):
	return num**2

num_list = [1,2,3,4,5]

# Map: can help iterate all items through a function
# you can print through a for loop OR cast to a list
for item in map(square, num_list):
	print(item)

print(list(map(square, num_list)))

# Filter: helps with separating values based on a filter function
def check_even(num):
	return num%2 == 0

my_num = [1,2,3,4,5,6]

for n in filter(check_even,my_num):
	print(n)

print('----')

# LAMBDA aka anonymous function
square_new = lambda num: num**2
print(square_new(2))

print('----')

# Use it in conjunction with map or filter
sqrt_list = map(lambda num: num**2, my_num)
print(list(sqrt_list))

print('----')

# ---- NESTED STATEMENTS & SCOPE ---
# LEGB Rule for variables: Local, Enclosing function locals, Global, and Built-in
x = 50

def func():
	global x

	print(f'X is {x}')

	# reassign x globally
	x = 200

print(x)
func()
print(x) 

win_sets = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
o = [1,2]

print(win_sets[0])
print(set(o).issuperset(win_sets[0]))