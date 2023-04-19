```python
reviews = [
    {"title": "Film X", "rating": 4.0, "review": "A captivating story with great character development."},
    {"title": "Film Y", "rating": 1.5, "review": "Disappointing plot and subpar acting."},
    {"title": "Film Z", "rating": 4.5, "review": "Incredible cinematography and a powerful performance by the lead actor."},
    {"title": "Film W", "rating": 3.5, "review": "A good movie with some memorable moments."},
    {"title": "Film V", "rating": 2.5, "review": "An interesting premise, but the execution falls short."},
]
```

Given a list of movie reviews, use higher-order functions to analyze and process the reviews, calculating the average rating, and filtering reviews based on sentiment.

**Task Breakdown**:

a. Calculate the average rating of all the movies using the reduce() function.
b. Create a function sentiment_analysis() that takes a review text and returns a sentiment score (positive, negative, or neutral) based on the presence of certain keywords.
c. Use the map() function to add a sentiment score to each review.
d. Use the filter() function to find reviews with positive sentiment.