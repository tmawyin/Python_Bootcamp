# Generators - Allows function to return a value and continue after
# Use "yield" keyword

def create_cube(n = 1):
	result = []
	for x in range(1,n+1):
		result.append(x**3)
	return result

print(create_cube(10))

# Another option is to return each element instead of 
# creating a large list
def create_cube_better(n = 1):
	for x in range(1,n+1):
		yield x**3

for x in create_cube_better(10):
	print(x)

print("-------")


def gen_fibonacci(n = 1):
	a = 1
	b = 1
	for i in range(n+1):
		yield a
		a, b = b, a+b

for num in gen_fibonacci(10):
	print(num)

print("-------")

# -- NEXT() FUNCTION
# Used to get the next value in the generator
def simple_gen():
	for x in range(3):
		yield x

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
print("-------")

# -- ITER() FUNCTION
# Converts an object to an iteratable
s_iter = iter("HELLO")

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))