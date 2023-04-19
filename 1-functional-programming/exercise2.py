

from functools import reduce


reviews = [
    {"title": "Film X", "rating": 4.0, "review": "A captivating story with great character development."},
    {"title": "Film Y", "rating": 1.5, "review": "Disappointing plot and subpar acting."},
    {"title": "Film Z", "rating": 4.5, "review": "Incredible cinematography and a powerful performance by the lead actor."},
    {"title": "Film W", "rating": 3.5, "review": "A good movie with some memorable moments."},
    {"title": "Film V", "rating": 2.5, "review": "An interesting premise, but the execution falls short."},
]
# x = 0
# y = {"title": "Film X", "rating": 4.0, "review": "A captivating story with great character development."},

# x = 4.0
# y = {"title": "Film Y", "rating": 1.5, "review": "Disappointing plot and subpar acting."},

# Mean average
# accumulator/current total
def add(x, y):
  return x + y['rating']

total_rating = reduce(add, reviews, 0)
average_rating = total_rating / len(reviews)

print(f"Average rating: {average_rating:.2f}")


# b. Sentiment analysis function


def sentiment_analysis(review_text):
    positive_keywords = ["amazing", "recommend", "loved", "masterpiece"]
    negative_keywords = ["poor", "weak", "boring", "disappointing"]

    positive_count = sum(
        [1 for keyword in positive_keywords if keyword in review_text.lower()])
    negative_count = sum(
        [1 for keyword in negative_keywords if keyword in review_text.lower()])

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


reviews_with_sentiment = [add_sentiment(review) for review in reviews]

# d. Filter reviews with positive sentiment using filter()


def is_positive(review):
    return review["sentiment"] == "positive"


positive_reviews = [
    review for review in reviews_with_sentiment if is_positive(review)]

# Print results
print("Positive Reviews:")
for review in positive_reviews:
    print(f"{review['title']}: {review['review']}")
