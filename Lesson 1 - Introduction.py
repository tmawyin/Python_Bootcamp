# Introduction to Data Types

# FIRST CODE
print('hello World!')

# --- NUMBERS ---
# "Mod" Operator: %
print(7 % 4)

# Power
print(7**3)

# Variable type
a = 10
type(a)

# --- STRINGS --- 

x = "Hello World"
x.upper()
x.lower()
x.split()

# Using the .format() method for string
print('This is a string {}'.format('INSERTED'))

print('The {2} {1} {0}'.format('fox','brown','quick'))

print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

# Format for numbers - syntax: {value:width.precision f/e}
result = 100/777
print('The result was {r:1.3f}'.format(r=result))

# Using formated string literals - use the "f" before the string
name = "Jose"
print(f'Hello, his name is {name}')

# --- LISTS --- 
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

# pop($) removes item from the end of the list if no argument, or on the $ index
my_list.pop()
print(my_list)

# Other methods sort() and reverse()
my_list.sort()
my_list.reverse()


# --- DICTIONARIES ---
# Uses key value pairs {key1:value1, key2:value2, ...}
my_dict = {'name':'T', 'last_name':"M", 'age':35}
print(my_dict['last_name'])

# Adding key pairs to dictionary
my_dict['address'] = 'Michigan'

# All keys or values or pairings
my_dict.keys()
my_dict.values()
my_dict.items()


# --- TUPLES ---
# Similar to lists but they are immutable (can't change items inside them)
my_tuple = (1,2,3,4,5,6,7,8)

my_tuple.count(1) #counts how many times "1" is in the typle
my_tuple.index(1) #returns the index for the first time the item appears


# --- SETS ---
# Sets are unordered collections of unique elements
my_set = set()
my_set.add(1)
my_set.add(2) #if we try to add 1 again, we won't repeat the value if it's already there

print(my_set)
