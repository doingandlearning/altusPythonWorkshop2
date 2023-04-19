# Introduction
- Brief overview of recursion 
- Importance of recursion in programming and algorithm design

# Recursion basics 
- Definition: A technique where a function calls itself as a subroutine
- Key components of a recursive function
- Base case: The condition when the recursion stops
- Recursive case: The part where the function calls itself
- Code example:
```python
def countdown(n):
	if n <= 0:
		print("Liftoff!")
	else:
		print(n)
		countdown(n - 1)

countdown(5)
```
- Points to talk about:
    - Recursive functions simplify code by expressing a problem in terms of a smaller instance of itself
    - Understanding how recursion works: call stack and execution context

# Recursive vs. iterative solutions 

- Comparison between recursive and iterative approaches to problem-solving
- Examples: Factorial, Fibonacci sequence
- Iterative factorial:
```python 
def factorial_iterative(n): 
  result = 1 
  for i in range(1, n + 1): 
    result *= i 
  return result 
```
- Recursive factorial:
```python
 def factorial_recursive(n): 
  if n == 0 or n == 1: 
    return 1 
  return n * factorial_recursive(n - 1) 
```

- Points to talk about:
	- Readability and conciseness: Recursive solutions are often more concise and easier to understand 
	- Performance: Iterative solutions can be more efficient in terms of time and space complexity 
	- Choosing the right approach: Trade-offs between readability and performance, as well as problem-specific considerations

# Tail recursion
- Definition: A specific form of recursion where the function call is the last operation in the function
- Importance: Some languages and compilers optimize tail recursion to prevent stack overflow issues
- Example: Tail-recursive factorial

```python 
def factorial_tail_recursive(n, accumulator=1): 
  if n == 0 or n == 1: 
    return accumulator 
  return factorial_tail_recursive(n - 1, accumulator * n) 
```

- Note: Python does not support tail call optimization, but understanding the concept is useful for other programming languages

# Common use cases
- Solving problems with repetitive tasks: Recursion simplifies code for problems that require repetitive operations
- Tree traversal: Recursion is a natural fit for traversing tree data structures (e.g., binary trees, file system directories)
- Backtracking: Recursion is often used in backtracking algorithms for solving puzzles, pathfinding, and combinatorial problems

#  Built-in examples: Factorial, Fibonacci sequence, and binary search
- Factorial: Covered earlier in the workshop
- Fibonacci sequence:

```python 
def fibonacci(n): 
  if n == 0: 
    return 0 
  elif n == 1: 
    return 1 
  return fibonacci(n - 1) + fibonacci(n - 2)
``` 

- Binary search:
```python 
def binary_search(arr, target, low, high): 
  if low > high: 
    return -1
  mid = (low + high)          
  if arr[mid] == target:             
    return mid         
  elif arr[mid] < target:             
    return binary_search(arr, target, mid + 1, high)         
  else:             
    return binary_search(arr, target, low, mid - 1)      
numbers = [1, 3, 5, 7, 9, 11, 13, 15]     
target_index = binary_search(numbers, 7, 0, len(numbers) - 1)     print(target_index)  # Output: 3     
```

# Exercise: Implement a recursive function to solve the Tower of Hanoi problem 
- Task: Write a recursive function to solve the Tower of Hanoi problem with a given number of disks
- Code example:
```python
def hanoi(n, source, target, auxiliary):
  if n > 0:
    # Move n-1 disks from source to auxiliary peg
    hanoi(n - 1, source, auxiliary, target)
	# Move the nth disk from source to target peg
	print(f"Move disk {n} from {source} to {target}")
	# Move n-1 disks from auxiliary to target peg
	hanoi(n - 1, auxiliary, target, source)

# Solve the Tower of Hanoi problem with 3 disks 
hanoi(3, "A", "C", "B")
```

# Gotchas!
Biggest gotchas for recursion in Python:

1. No tail call optimization: Python does not support tail call optimization, meaning that each recursive call adds a new frame to the call stack. This can lead to stack overflow errors when dealing with deep recursion or large inputs.

2. Performance concerns: Recursive solutions can be less efficient than their iterative counterparts in terms of time and space complexity, as they may involve higher function call overhead and increased memory usage.

3. Debugging difficulty: Debugging recursive functions can be more challenging due to the nature of the call stack and the need to understand the function's state at different recursion levels.

# Tips!

Tips for developers new to recursion:

1.  Understand the base case and recursive case: When designing a recursive function, always start by identifying the base case (when the recursion should stop) and the recursive case (how the function should call itself).
    
2.  Visualize the call stack: To understand how a recursive function works, visualize the call stack and the function's execution context at each recursion level. This will help with debugging and reasoning about the algorithm.
    
3.  Test with small inputs: Start testing your recursive function with small input values and build up from there. This will help ensure that the function works correctly and handles edge cases properly.
    
4.  Consider alternative solutions: Sometimes, an iterative solution might be more efficient or easier to understand. Compare the recursive and iterative approaches and choose the one that best suits the problem and your specific requirements.

5.  Convert to tail recursion when possible: If you are working on a problem that requires deep recursion, and you expect to port your code to another language that supports tail call optimization, consider converting your recursive function to use tail recursion.

# Using recursion in API creation or AWS  Lambdas:
1.  API creation: When designing APIs that involve processing hierarchical data structures, such as processing JSON or XML data, recursive functions can help simplify the code and make it more readable. For example, you can use recursion to traverse and manipulate nested dictionaries or lists in JSON data.
    
2.  AWS Lambdas: Although AWS Lambda functions are typically short-lived and event-driven, there are situations where recursion can be useful. For instance, if you need to implement a Lambda function that processes hierarchical data or traverses a tree-like structure (e.g., file system operations or processing hierarchical data in a database), recursion can be a helpful approach. However, keep in mind the execution time and memory limitations of Lambda functions, and consider using iterative solutions or other optimization techniques when appropriate to avoid exceeding these limits.

# Conclusion 
- Recap of key concepts: Recursion basics, recursive vs. iterative solutions, and tail recursion
- Importance of recursion in writing clean, concise, and elegant code
- Always balance the trade-offs between code readability, maintainability, and performance when deciding whether to use recursion or an alternative approach.

