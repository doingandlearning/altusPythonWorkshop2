

## Functional programming concepts, principles, and benefits 
### What is functional programming? 
1. A programming paradigm that treats computation as the evaluation of mathematical functions 
2. Avoids changing state and mutable data 

### Key principles 
1. Pure functions 
	-  Definition: A function that always produces the same output for the same input and has no side effects 
	- Code example:
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5
```
2. Immutability 
	- Definition: An object whose state cannot be modified after it is created
	- Code example:
```python
def increment_items(items):
    return [item + 1 for item in items]

original_list = [1, 2, 3]
new_list = increment_items(original_list)

print(original_list)  # Output: [1, 2, 3]
print(new_list)       # Output: [2, 3, 4]
```

3. First-class functions 
	- Definition: Functions that can be assigned to variables, passed as arguments, and returned from other functions
	- Code example:
```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply(func, x):
    return func(x)

print(apply(square, 4))  # Output: 16
print(apply(cube, 3))    # Output: 27
```

### Benefits 
1. Easier to reason about 
2. More predictable 
3. Concurrency-friendly


## Refactoring
```python
from datetime import datetime


class Greeting:
    def __init__(self):
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good morning"
        elif 12 <= current_time.hour < 18:
            self.greeting_intro = "Good afternoon"
        else:
            self.greeting_intro = "Good evening"

    def greet(self, name):
        print(f"{self.greeting_intro}, {name}.")

    def greet_list(self, names):
        for name in names:
            self.greet(name)


def main():

    name = input("Enter your name: ")
    greeting = Greeting()
    greeting.greet(name)


if __name__ == "__main__":
    main()
```

## Common use cases: Data manipulation, parallel programming, and code readability 
###  Data manipulation 
1. Functional programming is useful for transforming and filtering data 
2. Example: map, filter, and reduce functions 
```python
# Example using map
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example using filter
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]

# Example using reduce
from functools import reduce

def multiply(a, b):
    return a * b

product = reduce(multiply, numbers)
print(product)  # Output: 120
```

B. Parallel programming 
1. Immutable data structures and pure functions make it easier to write parallel code 
2. Example: Parallelizing a map function 
```python
import concurrent.futures
import math

def calculate_square(x):
    return x * x

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Parallelize the map function using a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(calculate_square, data))

print(results)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

C. Code readability 
1. Functional code is often more concise and easier to understand 
2. Example: Comparing a functional solution to an imperative solution
```python
def sum_of_even_squares(numbers):
    even_squares_sum = 0
    for number in numbers:
        if number % 2 == 0:
            square = number * number
            even_squares_sum += square
    return even_squares_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_squares(numbers)
print(result)  # Output: 220
```

```python
def is_even(number):
    return number % 2 == 0

def square(number):
    return number * number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(is_even, numbers)
squared_even_numbers = map(square, even_numbers)
result = sum(squared_even_numbers)

print(result)  # Output: 220
```

Both approaches produce the same result, but the functional approach relies on higher-order functions like `filter` and `map` to achieve the same goal. The functional approach is often considered more readable and easier to reason about because it avoids mutable variables and focuses on data transformation.



## Exercise : Implement a function to find the top N words by frequency in a text 

### Task description 
1. Write a function that takes a string and an integer N as its arguments and returns the top N words by frequency in the given text 
2. The function should ignore case, remove punctuation, and consider words as sequences of characters separated by whitespace 
3. The function should use functional programming concepts like pure functions, immutability, and higher-order functions

### Requirements 
1. The function should take a string (text) and an integer (N) as its arguments 
2. The function should return a list of tuples, each containing a word and its frequency, sorted by frequency in descending order 
3. The function should be case-insensitive and remove punctuation from the text

### Tips 
1. You may use Python's built-in `collections` module to help with counting word frequencies 
2. Consider using higher-order functions like `map`, `filter`, and `sorted` to achieve a more functional programming style

### Example input and output


```python
text = "Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions or declarations instead of statements."
top_n = 5

print(top_n_words(text, top_n)) # # Expected output: [('programming', 4), ('and', 2), ('is', 2), ('a', 2), ('paradigm', 2)]
```
