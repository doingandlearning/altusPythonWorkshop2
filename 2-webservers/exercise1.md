# Basic Flask Application with Multiple Routes

## Objective:
In this exercise, you will create a simple Flask web application with multiple routes, each handling different functionalities. You will practice creating routes, writing functions for those routes, and testing the application using a web browser or a tool like Postman.

## Requirements:

- Python 3.6 or higher
- Flask library installed (use pip install Flask if not already installed)

## Instructions:
- Activate your virtual environment and install Flask

```bash
pip install flask
```

- Create a new Python file named app.py and import the required Flask module.
- Create a route for the main page (root URL) that returns a welcome message.
- Create a new route named /add that accepts two numbers (a and b) as query parameters and returns the sum of those numbers.
- Create a new route named /multiply that accepts two numbers (a and b) as query parameters and returns the product of those numbers.
- Add the main function to run the Flask application.
- Save the app.py file and run it using the command python app.py. This will start the Flask development server.
- Test the application using a web browser or a tool like Postman. Access the main page at http://localhost:5000/, the /add route by visiting http://localhost:5000/add?a=2&b=3 (replace 2 and 3 with any numbers), and the /multiply route by visiting http://localhost:5000/multiply?a=4&b=5 (replace 4 and 5 with any numbers).

## If time permits:
- Add a division route (make sure you handle divide by zero errors!)
- Add a route that a date as a parameter and tells how many days it is til then
- Add a route the calculates the factorial of a number
