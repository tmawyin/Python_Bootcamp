# Comparison Operators, Conditional Statements, & Control Flow
# if/elif/else
# for/while loops


# --- IF STATEMENTS ---
hungry = False
thirsty = True

if hungry == True:
	print('Feed me!')
elif hungry == True and thirsty == True:
	print('Feed me and give me a dring!')
else:
	print("Not hungry or thirsty")

print('-----')

# --- FOR LOOP ---
mylist = [1,2,3,4,5,6,7,8,9,10]
for item in mylist:
	# Check if the number is even
	if item % 2 == 0:
		print(f'{item} is even')
	else:
		print(f'{item} is odd')

print('-----')

list_sum = 0
for num in mylist:
	list_sum += num

print(list_sum)
print('-----')

# Tupple un-packing: Have access to the individual items of the tupple
tup_list = [(1,2),(2,3),(5,6)]
for a,b in tup_list:
	print(a)
	print(b)

print('-----')

# Dictionary iterations
d = {'k1':1,'k2':2,'k3':3,'k4':4}

for key,value in d.items():
	print(value)

print('-----')

# --- WHILE LOOP ---
# Can use while and else together
x = 0
while x < 5:
	print(f'the value of x is {x}')
	x += 1
else:
	print('The end!')
print('-----')

# --- BREAK, CONTINUE, PASS ---
# break: breaks out of the current closest enclosing loop
mystring = 'Sammy'
for letter in mystring:
	# avoing printing letters after 'a'
	if letter == 'a':
		break
	else:
		print(letter)
print('-----')

# continue: goes to the top of the closest enclosing loop
for letter in mystring:
	# avoing printing only letter 'a'
	if letter == 'a':
		continue
	else:
		print(letter)
print('-----')

# pass: do nothing
x = [1,2,3,4]
for item in x:
	pass

print('-----')

# --- USEFUL OPERATORS ---
# RANGE: generates a "list" of items used in loop
# range(start,stop,step)
for num in range(2,10,1):
	print(num)
print('-----')

# ENUMERATE: prints index and elemebt as a tupple
for letter in enumerate('abcde'):
	print(letter)
print('-----')

# ZIP: zips together 2 lists - joins lists in tupple
mylist_1 = [1,2,3, 4]
mylist_2 = ['a','b','c','d']

for item in zip(mylist_1,mylist_2):
	print(item)

print('-----')

# IN: check if item is in a list
print(2 in [1,3,4,5,2])
print('-----')

# INPUT : asks the user for input
# num = input('Enter a number:')

# LIST COMPREHENSION ---
my_list = [x*2 for x in [1,2,3,4,5,6,7,8] if x%2==0]
print(my_list)
