import pytest
from pathlib import Path

def my_add(a,b):
  return a + b


@pytest.mark.parametrize("a, b, expected", [
  (1, 2, 3),
  (4, 1, 5),
  (10, -5, 5),
  (10, 0, 10)
])
def test_adding_works(a, b, expected):
  assert my_add(a,b) == expected

@pytest.fixture(scope="function", autouse=True)
def sample_list():
  return [1,2,3,4,5,6]

def test_sample_list_append(sample_list):
  sample_list.append(6)
  assert len(sample_list) == 7

def test_sample_list(sample_list):
  assert len(sample_list) == 6

def home():
  return Path.home()

def test_home(monkeypatch):
  def mockreturn():
    return Path("/abc")
  
  monkeypatch.setattr(Path, "home", mockreturn)

  x = home()
  assert x == Path("/abc")

# def test_get_discount(monkeypatch):
#     # Mock the is_premium method
#     def mock_is_premium(self):
#         return True

#     monkeypatch.setattr(my_module.User, "is_premium", mock_is_premium)

#     user = my_module.User()
#     discount = my_module.get_discount(user)
#     assert discount == "Expected discount for premium users"


# def test_max_retries_reached(monkeypatch):
#     monkeypatch.setattr(my_module, "MAX_RETRIES", 0)

#     result = my_module.perform_operation()
#     assert result == "Expected result when max retries are reached"

# ## Test raising exceptions

def divide(a,b):
  # raise CustomException()
  return a /b

def test_can_divide():
  with pytest.raises(ZeroDivisionError):
    divide(2,0)  

class CustomException(Exception):
  pass

