# Other Modules
# os & shutil Modules
import os
import shutil

# -- Get current directory
print(os.getcwd())

# -- Get a list of files in the path given
print(os.listdir("C:\\Users"))

# -- Moving files around from source (src) to destination (dst)
# shutil.move(src, dst)

# -- Walking through the file directory
# os.walk(top directory)


# --------
# Datetime Module
import datetime

mytime = datetime.time(2,20)
print(mytime)
print(mytime.minute)

today = datetime.date.today()
print(today)

# datetime is more complete by showing hh:mm:ss
now = datetime.datetime(2020,8,6,15,22,50)
print(now)

print("----------\n")


# --------
# Math & Random Module
import math
import random

print(math.floor(4.32))
print(math.ceil(4.32))

# constant
print(math.pi)

mylist = list(range(0,21))
print(random.choice(mylist))


# Sampling with replacement
chosen_list = random.choices(mylist, k=10)
print(chosen_list)

# Sampling without replacement
random.sample(mylist, k=10)

# Distributions
random.uniform(a=0, b=100)
random.gauss(mu=0, sigma=1)

print("----------\n")


# --------
# Debugger Module
import pdb

x = [1,2,3]
y = 2
z = 3

# This is ok
result_one = y + z

# This is not ok - let's set a debug trace
pdb.set_trace()
result_two = y + x
