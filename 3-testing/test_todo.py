from todo import app
import unittest
from pathlib import Path

class TestTodo(unittest.TestCase):
  def setUp(self) -> None:
    self.app = app.test_client()
    return super().setUp()

  def test_get_all_todos_works(self):
    response = self.app.get("/todos")
    self.assertEqual(response.status_code, 200)

  def test_create_new_todo_works_with_correct_header(self):
    response = self.app.post("/todos", 
                              json={"title": "This is a todo"},
                              headers={"x-api-key": "super-secret-key"}
                            )

    self.assertEqual(201, response.status_code)

    data = response.get_json()

    self.assertEqual(data['title'], "This is a todo")
    self.assertEqual(data['completed'], False)
    self.assertEqual(data['id'], 1)

  def test_create_new_todo_403_with_incorrect_header(self):
    response = self.app.post("/todos", 
                              json={"title": "This is a todo"},
                              headers={"x-api-key": "not-correct-key"}
                            )

    self.assertEqual(403, response.status_code)

  def test_create_new_todo_403_with_no_header(self):
    response = self.app.post("/todos", 
                              json={"title": "This is a todo"},
                            )

    self.assertEqual(403, response.status_code)


  def test_other_thing(self):
    with unittest.patch('Path.home', lambda x: Path("/abc")):
      target = Path.home()
      self.assertEqual(Path("/abc"), target)
    with unittest.patch('User.is_authed', True):

    print(Path.home())

if __name__ == "__main__":
  unittest.main()
