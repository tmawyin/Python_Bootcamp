# Timing Code
import time


def func_one(n):
	return [str(num) for num in range(n)]


# Time before
start_time = time.time()
# Run Code
func_one(100000)
# End time
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)


def func_two(n):
	return list(map(str,range(n)))

# Time before
start_time = time.time()
# Run Code
func_two(100000)
# End time
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)


# ------ TIMEIT MODULE ----
import timeit

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
	return [str(num) for num in range(n)]
'''

# This is running func_one(100) one million times. The setup string defines the function
time_result = timeit.timeit(stmt, setup, number = 1000000)
print(time_result)

