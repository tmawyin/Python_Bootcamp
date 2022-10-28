# I/O Basics
# Dealing with .txt files and directories
# Using test.txt file in the same directory

myfile = open('test_io_file.txt')

myfile.read() 	#reads the entire file as string
myfile.seek(0) 	#resets the cursor to the begining of the file

myfile.readlines()	#reads single line and appends them to a list

myfile.close()	#closes file - required when using "open" command

# -- Alternative method to open a file
with open('test_io_file.txt') as my_textfile:
	content = my_textfile.readlines()

print(content)


# -- Writing to files
# mode = 'w' to overwrite
# mode = 'a' to append to file
# mode = 'r+' to read and write
# mode = 'w+' to overwrite and read
with open('test.txt', mode='a') as my_textfile:
	my_textfile.write('\nThird Line')
