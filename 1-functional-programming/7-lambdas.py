square = lambda x: x * x 

def square(x):
  return x * x


def multiply(a,b):
  return a * b

multiply = lambda a, b: a * b 
multiply = lambda a, b: a * b 

print(multiply(1,2))

def is_even(number):
  return number % 2 == 0

is_even = lambda a: a % 2 == 0 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

squares = list(map(lambda x: x * x, numbers))
print(squares) 

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)



try:
  lambda_function = lambda: 1/0

except (ZeroDivisionError):
  print("This was a divide by zero error")

try:
  lambda_function()
except ZeroDivisionError as e:
    print("An error occurred: ", e)