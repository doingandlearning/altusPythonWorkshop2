import unittest


def is_palindrome(input_string):
    input_string = input_string.lower()
    cleaned_string = ''.join(c for c in input_string if c.isalnum())
    return cleaned_string == cleaned_string[::-1]


class TestPalindromeChecker(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama???"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
