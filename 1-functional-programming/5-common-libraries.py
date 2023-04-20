import functools
import timeit

from typing import NewType

[1, "t", True]

# functools.reduce()

id = 0
def generate_user_object(name: str, company):
  global id
  id += 1
  return {'company': company, 'name': name, 'id': id}

# Currying
generate_altus_user = functools.partial(generate_user_object, "Altus")
generate_altus_user = lambda name: generate_user_object(name, "Altus")

user1 = generate_altus_user("Al")
user2 = generate_altus_user("Jong")
user3 = generate_altus_user("Anna")

# print(user1, user2, user3)

def add(*args, **kwargs):
  print(args)
  print(kwargs)

# add(1,2,3,4, name="Kevin", location="NI")

def test(a):
  pass

# test(1,2)

def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)

starttime = timeit.default_timer()
print(fib(33))
print("The time difference is :", timeit.default_timer() - starttime)

@functools.lru_cache(maxsize=None)
def cached_fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)

starttime = timeit.default_timer()
print(cached_fib(33))
print("The time difference is :", timeit.default_timer() - starttime)