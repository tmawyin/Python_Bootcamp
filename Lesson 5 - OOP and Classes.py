# Object Oriented Programming
# Classes - Attributes & Methods

# Generating a class
class Dog():
	
	# Class object attribute - same for ANY instance
	species = "mammal"

	# Setting attributes for an instance of a class
	def __init__(self,breed,name):
		self.breed = breed
		self.name = name
		
	# Methods
	def bark(self, number):
		print("WoOf "*number + 'and my name is {}'.format(self.name))

# Creating an instance
mydog = Dog("Lab","Rocky")
print(mydog.breed)
print(mydog.name)
mydog.bark(3)

print('----------')

# Another example: Circle Class
class Circle():
	pi = 3.14

	def __init__(self,radius = 1):
		self.radius = radius

	def get_circumference(self):
		return self.radius * Circle.pi * 2

	def get_area(self):
		return self.pi * self.radius**2

mycircle = Circle(10)
print(mycircle.get_circumference())
print(mycircle.get_area())

print('----------')

# INHERITANCE & POLYMORPHISM
class Animal():
	def __init__(self):
		print("Animal Created!")

	def who_am_i(self):
		print("I am an animal")

	def eat(self):
		print("I'm eating")

# Dog class inherits from Animal
class Dog(Animal):
	
	# Class object attribute - same for ANY instance
	species = "mammal"

	# Setting attributes for an instance of a class
	def __init__(self,breed="",name=""):
		Animal.__init__(self)
		self.breed = breed
		self.name = name
		print("Dog Created!")

	def who_am_i(self):
		print("I am a Dog!")

	def bark(self, number):
		print("WoOf "*number + 'and my name is {}'.format(self.name))

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

print("-----------")


# POLYMORPHISM
# Sharing methods on different classes

class Dog():
	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says woof!"

class Cat():
	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says meow!"

niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())
print("----------")

# SPECIAL METHODS - MAGIC/DUNDER
class Book():
	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages

	# Special methods
	# __str__ substitutes print function
	def __str__(self):
		return f"{self.title} by {self.author}"

	def __len__(self):
		return self.pages

	def __del__(self):
		print("Your book is gone!")

b = Book('Python rocks','Me',200)
print(b)
print(len(b))

# to delete instance
del b
