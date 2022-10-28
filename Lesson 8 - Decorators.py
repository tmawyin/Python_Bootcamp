# Decorators
# On/Off switch to make functionality available on a function - uses @

def func(num=1):
	return num

# Passing a function to other function
def hello(name="You", fun = func):
	return f"Hello {name}, "*fun + \
	"\nThe hello() function is executed"


print(hello("Tomas", func(3)))
print("\n------\n")


# Decorator is like a wraper
def new_decorator(original_func):
	def wrap_func():
		print("Some extra code, before the original function")

		original_func()

		print("More code, after the original function")

	return wrap_func

def need_decoration():
	print("** I want to be decorated!! **")

decorated_func = new_decorator(need_decoration)
decorated_func()

# A better way is to add @ decorator:
# No need to create additional functions and pass functions around
@new_decorator
def need_decoration_method():
	print("** I want to be decorated, the better way!! **")

print("------")
need_decoration_method()
