import unittest

# 5 USD x 2 = 10 USD
class Money:
  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency

  def times(self, multiplier):
    return Money(self.amount * multiplier, self.currency)

class TestMoney(unittest.TestCase):
  def test_multiplication(self):
    # Arrange::Given
    fiver = Money(5, "USD")
    
    # Act::When
    tenner = fiver.times(2)
    twenty = tenner.times(2)

    # Assert::Then
    self.assertEqual(10, tenner.amount)
    self.assertEqual(20, twenty.amount)
    self.assertEqual("USD", tenner.currency)
  
  def test_multiplication_in_euros(self):
    # Arrange
    tenEuros = Money(10, "EUR")

    # Act
    twentyEuros = tenEuros.times(2)

    # Assert
    self.assertEqual(20, twentyEuros.amount)
    self.assertEqual("EUR", twentyEuros.currency)

if __name__ == "__main__":
  unittest.main()