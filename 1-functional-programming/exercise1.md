# Exercise: Implement a function to find the top X words by frequency in a text

# Task description
1. Write a function that takes a string and an integer X as its arguments and returns the top X words by frequency in the given text
2. The function should ignore case, remove punctuation, and consider words as sequences of characters separated by whitespace
3. The function should use functional programming concepts like pure functions, immutability, and higher-order functions

# Requirements
1. The function should take a string(text) and an integer(X) as its arguments
2. The function should return a list of tuples, each containing a word and its frequency, sorted by frequency in descending order `[("the", 10)]`
3. The function should be case-insensitive and remove punctuation from the text

# Tips
1. You may use Python's built-in `collections` module to help with counting word frequencies
2. Consider using higher-order functions like `map`, `filter`, and `sorted` to achieve a more functional programming style

# Example input and output


```python
text = "Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions or declarations instead of statements."
top_x = 5

print(top_x_words(text, top_x))
# Expected output: [('programming', 4), ('and', 2), ('is', 2), ('a', 2), ('paradigm', 2)]
```
