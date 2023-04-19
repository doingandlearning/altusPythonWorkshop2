# Introduction 
- Brief overview of higher-order functions in Python 
- Importance of higher-order functions in programming

# First-class functions 
- Definition: Functions that can be assigned to variables, passed as arguments to other functions, and returned as values from other functions 
- Code example: 
```python 
def square(x): 
  return x * x

f = square     
print(f(5))  # Output: 25     
``` 
- Points to talk about:    
	- First-class functions enable higher-order functions     
	- Python treats functions as first-class citizens

# Higher-order functions  
- Definition: Functions that take other functions as arguments or return them as results 
- Real-life example: Sorting a list of items by different criteria (price, name, etc.) by passing a different comparison function 
- Code example:
```python 
def apply(func, x, y): 
  return func(x, y)

def add(x, y):         
  return x + y      

def multiply(x, y):         
  return x * y      

print(apply(add, 5, 3))  # Output: 8     
print(apply(multiply, 5, 3))  # Output: 15     
```

# Function composition 
- Definition: Combining two or more functions to create a new function 
- Real-life example: Image processing pipeline (resizing, applying filters, and compressing) 
- Code example:
```python 
def compose(f, g): 
  def composed_function(x): 
    return f(g(x)) 
  return composed_function

def square(x): 
  return x * x 

def increment(x): 
  return x + 1 

square_after_increment = compose(square, increment) increment_after_square = compose(increment, square) print(square_after_increment(4)) # Output: 25
print(increment_after_square(4)) # Output: 17

```

# Common use cases 
- Creating reusable code: Higher-order functions allow for code modularity and reusability 
- Manipulating lists: Using higher-order functions to process and transform lists in a functional way 
- Simplifying complex tasks: Breaking down complex tasks into smaller, reusable functions and composing them as needed

# Built-in examples: `map()`, `filter()`, and `reduce()` functions 
- `map()`: Apply a given function to all items in an iterable 
- Code example:
```python 
def square(x): 
  return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

- `filter()`: Filter items from an iterable based on a given function (predicate) 
- Code example:
``` python 
def is_even(x): 
  return x % 2 == 0
      
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```
- `reduce()`: Apply a function with two arguments cumulatively to the items in an iterable, reducing the iterable to a single value
    - Note: `reduce()` is part of the `functools` module in Python 3
    - Code example:
```python
from functools import reduce

def add(x, y):
	return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15
```

# Exercise: Use `map()` and `filter()` to process a list of numbers 

- Task: Given a list of numbers, use `map()` and `filter()` to create a new list containing the squares of even numbers only 

- Code example:
```python
def is_even(x): 
  return x % 2 == 0

def square(x):         
  return x * x      
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]     
even_numbers = list(filter(is_even, numbers))     
squared_even_numbers = list(map(square, even_numbers))     print(squared_even_numbers)  # Output: [4, 16, 36, 64]`
```

# Exercise: Analyze and process a list of movie reviews

**Objective**: Given a list of movie reviews, use higher-order functions to analyze and process the reviews, calculating the average rating, and filtering reviews based on sentiment.

**Movie Review Data**:

```python

reviews = [
    {"title": "Movie A", "rating": 3.5, "review": "It was an average movie with decent acting."},
    {"title": "Movie B", "rating": 4.5, "review": "An amazing experience! Loved the visual effects."},
    {"title": "Movie C", "rating": 2.0, "review": "Poor acting and a weak storyline."},
    {"title": "Movie D", "rating": 3.0, "review": "An okay movie. Could have been better."},
    {"title": "Movie E", "rating": 5.0, "review": "A true masterpiece! I highly recommend it."},
]
```
**Task Breakdown**:

a. Calculate the average rating of all the movies using the reduce() function.
b. Create a function sentiment_analysis() that takes a review text and returns a sentiment score (positive, negative, or neutral) based on the presence of certain keywords.
c. Use the map() function to add a sentiment score to each review.
d. Use the filter() function to find reviews with positive sentiment.

**Sample Solution**
```python
from functools import reduce 

# a. Calculate the average rating
def add_ratings(x, y):
    return x + y["rating"]

total_rating = reduce(add_ratings, reviews, 0)
average_rating = total_rating / len(reviews)
print(f"Average rating: {average_rating:.2f}")

# b. Sentiment analysis function
def sentiment_analysis(review_text):
    positive_keywords = ["amazing", "recommend", "loved", "masterpiece"]
    negative_keywords = ["poor", "weak", "boring", "disappointing"]

    positive_count = sum([1 for keyword in positive_keywords if keyword in review_text.lower()])
    negative_count = sum([1 for keyword in negative_keywords if keyword in review_text.lower()])

    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

# c. Add sentiment scores to each review using map()
def add_sentiment(review):
    review["sentiment"] = sentiment_analysis(review["review"])
    return review

reviews_with_sentiment = list(map(add_sentiment, reviews))

reviews_with_sentiment = [add_sentiment(review) for review in reviews]

# d. Filter reviews with positive sentiment using filter()
def is_positive(review):
    return review["sentiment"] == "positive"

positive_reviews = list(filter(is_positive, reviews_with_sentiment))
positive_reviews = [review for review in reviews_with_sentiment if is_positive(review)]

# Print results
print("Positive Reviews:")
for review in positive_reviews:
    print(f"{review['title']}: {review['review']}")
```

# Conclusion 
- Recap of key concepts: First-class functions, higher-order functions, and function composition
- Importance of higher-order functions in writing clean, modular, and reusable code
- Encourage students to use higher-order functions in their projects and assignments to improve code quality and maintainability


