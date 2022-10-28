# Modules & Packages
# Modules are just .py files that contain functions
# Package is a collection of modules

''' Packages require the following:
Folders: Package_Folder/Sub_Package_Folders
init file: __init__.py under the Package and Sub_Package folders
python file: all python files containign modules under each folder
'''

# Use module.py as an example
from module import my_func

my_func()


# ------- MAIN & NAME -----
if __name__ == '__main__':
	# some code here
	print("Code here is run directly")
else:
	print("Code here has been imported")