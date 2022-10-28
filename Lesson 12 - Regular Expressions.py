# Regular Expressions (regex)
# Used for pattern search

import re

text = "The agent phone number is 408-555-1234. Call soon!"

pattern = "phone"

find_pattern = re.search(pattern, text)
print(find_pattern)
print(find_pattern.span())
print(find_pattern.start())
print(find_pattern.end())

matches = re.findall(pattern, text)

pattern = "a"
for m in re.finditer(pattern, text):
	print(m) # returns the object it found
	print(m.group()) # returns the actual matched text

print("------\n")

# We can use special syntax or identifiers to be found
# for example: we can find items of the pattern (###)-###-####
# identifiers can be: \d (digit), \w (Alphanumeric), \s (white space)

exp = r"\d\d\d-\d\d\d-\d\d\d\d"
exp = r"\d{3}-\d{3}-\d{4}" #<- this is an alternate way to write the expression
phone = re.search(exp, text) #<- searching for the expression of digits followed by dash
print(phone.group())

# We can create "groups" of expressions using () and use compile() to join them
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
result = re.search(phone_pattern, text)
print(result)
print(result.group(3)) #picks up the 3rd group


# Additional Syntax ----

# pipe | operator is used like an "OR"
re.search(r"cat|dog","The dog is away of the house") # Searches for cat OR dog strings

# Using wildcard for placement
response = re.findall(r".at","The fat cat in the hat sat in the table") # the period (.) is used as wildcard
print(response)

# Other wildcards are: ^ for start with; $ for ends with; [^\d]+ for exclude digits
# Example:

pattern = r"[^\d]+"
result = re.findall(pattern,"There 3 are numbers 45 inside 6 this expression 50")

print(result)

# Another example to remove punctuation
test_phrase = "This is a string! A text! that has punctuation. How can we remove it?"
pattern = r"[^!.? ]+" # removes all punctuation and spaces

clean = re.findall(pattern, test_phrase)
print(" ".join(clean))