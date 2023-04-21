from todo import app
import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()



def test_get_all_todos_works(client):
  response = client.get("/todos")
  # self.assertEqual(response.status_code, 200)
  assert response.status_code == 200

#   def test_create_new_todo_works_with_correct_header(self):
#     response = self.app.post("/todos", 
#                               json={"title": "This is a todo"},
#                               headers={"x-api-key": "super-secret-key"}
#                             )

#     self.assertEqual(201, response.status_code)

#     data = response.get_json()

#     self.assertEqual(data['title'], "This is a todo")
#     self.assertEqual(data['completed'], False)
#     self.assertEqual(data['id'], 1)

#   def test_create_new_todo_403_with_incorrect_header(self):
#     response = self.app.post("/todos", 
#                               json={"title": "This is a todo"},
#                               headers={"x-api-key": "not-correct-key"}
#                             )

#     self.assertEqual(403, response.status_code)

#   def test_create_new_todo_403_with_no_header(self):
#     response = self.app.post("/todos", 
#                               json={"title": "This is a todo"},
#                             )

#     self.assertEqual(403, response.status_code)



# if __name__ == "__main__":
#   unittest.main()
