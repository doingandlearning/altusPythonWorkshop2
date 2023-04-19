def square(x):
  return x * x

numbers = [1,2,3,4,5,6,7,8,9]

# map
squared_numbers = [square(num) for num in numbers]
squared_with_map = list(map(square, numbers))

# filter
def is_even(x):
  return x % 2 == 0

even_numbers = list(filter(is_even, numbers))

even_numbers_comp = [num for num in numbers if is_even(num)]

print([x+1 if x>5 else x+2 for x in numbers])

# Tenary in list comp 
print(even_numbers)
print(even_numbers_comp)


# reduce
from functools import reduce

def multiply(a,b):
  return a * b

print(reduce(multiply, numbers))


# concurrency
import concurrent.futures

# Context
with concurrent.futures.ThreadPoolExecutor() as executor:
  # do some work in here
  results = list(executor.map(square, numbers))

print(results)
