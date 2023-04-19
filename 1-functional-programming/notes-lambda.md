# Introduction 

- What are lambda functions?
- When to use lambda functions

## Basic Lambda Function Syntax

- Syntax and structure
- Code example: Basic lambda function
- Exercise: Create a simple lambda function to add two numbers
```python
# Example 
square = lambda x: x * x 
print(square(5)) # Output: 25 # Exercise: Create a lambda function to add two numbers
```

## Comparing Lambda Functions to Regular Functions 

- Key differences
- Code example: Converting a regular function to a lambda function
```python
# Regular function
def multiply(x, y):
    return x * y

# Lambda function equivalent
multiply = lambda x, y: x * y
```
- Exercise: Convert a given function to a lambda function
```python
# Exercise: Convert the following function to a lambda function
def is_even(number):
    return number % 2 == 0
```

## Common Use Cases

- Lambda functions with filter(), map(), and reduce()
- Code examples:
	a. Using lambda with filter()
	b. Using lambda with map()
	c. Using lambda with reduce()
```python
# Example: Using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# Example: Using lambda with map()
squares = list(map(lambda x: x * x, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example: Using lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 362880
```
- Exercise: Apply lambda functions in combination with filter(), map(), or reduce()
```python
# Exercise: Use a lambda function to filter out numbers divisible by 3 from a list
numbers = [3, 6, 10, 15, 20, 21, 25, 30]
```

## Gotchas and Best Practices 

1. Limitations of lambda functions:
   - Lambda functions can only contain a single expression.
   - They don't support statements, assignments, or multiple expressions.
   - They don't support type annotations or default arguments.

2. Best practices for using lambda functions:
   - Use lambda functions for small, simple operations.
   - Keep the lambda function short and readable.
   - When the function body gets too complex, use a regular function instead.
   - Don't use lambda functions if they make the code harder to understand.

3. Common pitfalls and how to avoid them:
   - Overusing lambda functions: Use lambda functions when they improve code readability or when using them with functions like filter(), map(), or reduce().
   - Using a lambda when a regular function is more appropriate: If the function body is complex, it's better to use a regular function.
   - Poorly named variables in lambda functions: Choose meaningful variable names that describe the data they represent, even in lambda functions.

lambda functions can be a powerful tool in Python when used appropriately. By understanding their use cases, syntax, and best practices, you can write cleaner, more efficient code. This workshop has provided you with practical examples and exercises to help you master lambda functions in Python.