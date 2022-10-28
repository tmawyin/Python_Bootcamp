# Errors & Exception Handling

# Keywords used -
# try: code to be attempted
# except: if error under "try" execute this
# finally: execute this code regardless of the error


def add(n1, n2):
	return (n1 + n2)

# no error
add(10, 20)

# type error: one value is a number, the other is a string
try:
	result = add(10, '20')
except TypeError:
	print("Both values must be numbers")
# use else if no error happens
else:
	print(f"Add went well. Final answer is {result}")
finally:
	print("Thank you for using the program")


# Can use try/except with a while loop
def ask():
	while True:
		try:
			result = int(input("Input a number: "))
		except:
			print("Error! Please try again!")
		else:
			print("Thank you, your number squared is {}".format(result**2))
		break

print('--------------\n\n\n')

# ---- UNIT TESTING ----
# pylint library
# Use pylint file_name.py -r y to get a report on the errors and coding format

a = 1
b = 2
print(a)
print(B) # <-- pylint will show an error for this


# unittest library - use unit_test.py file for this example
# see files: unit_test_cap and unit_test