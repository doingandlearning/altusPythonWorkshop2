Objective: Create a Python function `is_palindrome(input_string)` that checks if the given input string is a palindrome. 

A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

# Possible steps:
1. Write a failing test for the `is_palindrome` function
2. Write the `is_palindrome` function to make the test pass
3. Refactor the `is_palindrome` function for better code quality
4. Add edge cases and additional tests
	- Consider potential edge cases (e.g., empty strings, strings with special characters)
	- Add new tests to the test class to cover these edge cases
	- Handle non-string inputs 

# If time permits:
- you could implement a Palindrome Counter that takes a list of strings and returns the number of palindromes in the list.
- Implement a Custom Exception
	- Create a custom exception class, e.g., InvalidInputError
	- Modify the is_palindrome function to raise the custom exception for invalid inputs (e.g., non-string inputs)
	- Update the test cases to check if the custom exception is raised correctly