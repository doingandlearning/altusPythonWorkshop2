To run test use `pytest <filename`.

1. Write a parameterized test for a subtraction function

Implement a my_subtract function that subtracts two numbers and returns the result. Write a parameterized test using pytest.mark.parametrize to test various cases.

2. Test a custom exception

```python
class MyGreatException(Exception):
	pass
```

Create a custom exception called NegativeResultError. Modify the my_add function to raise this exception when the result is negative. Write a test that checks if the custom exception is raised when adding two negative numbers.

3. Create a fixture to manage a temporary file

Write a fixture called temp_file that creates a temporary file, writes some data to it, and then deletes the file after the test is done. Write a test function that uses this fixture to read the contents of the temporary file and check if the data is correct.

4. Use pytest.mark.parametrize with a fixture

Create a new fixture called my_multiply that multiplies two numbers and returns the result. Write a parameterized test using pytest.mark.parametrize and the my_multiply fixture to test various cases.

5. Use monkeypatching to test a function that relies on the current date

Write a function called get_todays_date that returns the current date as a string in the format "YYYY-MM-DD". Use the monkeypatch to replace the standard library's datetime module with a custom implementation that returns a fixed date. Write a test that checks if the get_todays_date function returns the correct date when the datetime module is monkeypatched.