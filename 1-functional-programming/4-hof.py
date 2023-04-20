
import operator


def apply(func, x, y):
  return func(x,y)

def add(x,y):
  return x + y

print(apply(add, 1, 2))


# Currying 
add5 = lambda x: add(5, x)

print(add5(10))

# const add = (x) => add(5,x)

# Composition
def compose(f,g):
  def composed_function(x):
    return f(g(x))
  return composed_function

def square(x):
  return x * x

def increment(x):
  return operator.add(x, 1)

square_then_increment = compose(increment, square)
incremenet_then_square = compose(square, increment)

print(square_then_increment(10))
print(incremenet_then_square(10))

id = 0
# User generator
def user_generator_function(role):
  id = 0
  def generate_new_user(name):
    nonlocal id
    id += 1
    return {'name': name, 'id': f"{role}-{id}", 'role': role}
  return generate_new_user

adminGenerator = user_generator_function("admin")
editorGenerator = user_generator_function("editor")


print(adminGenerator("Victor"))
print(adminGenerator("Rachel"))
print(adminGenerator("Jong"))
print(editorGenerator("Pranay"))
print(editorGenerator("Suman"))
print(editorGenerator("Frank"))