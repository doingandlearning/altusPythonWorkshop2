# todo-grapqhl
Simple GraphQL server that allows managing todos:
* Create new todos
* Fetch all todos
* Fetch single todo
* Mark todo as done
* Update due date
* Delete todo


## Installation

Install required packages
```bash
pip install -r requirements.txt
```

Initialize the database:

```bash
flask shell
db.create_all()
```

If you want to, add a few todos:

```bash
python
from datetime import datetime
from api.models import Todo
today = datetime.today().date()
todo = Todo(description="Learn GraphQL", due_date=today, completed=False)
todo.to_dict()
{'id': None, 'completed': False, 'description': 'Run a marathon', 'due_date': '2022-04-20'}
db.session.add(todo)
db.session.commit()
```

## Running the app

```bash
export FLASK_APP=main
```

Start the server 
```bash
flask run 
```

and with debug we can use
```bash
flask run --debug
```

Open the GraphQL PlayGround by visiting http://127.0.0.1:5000/graphql 

Paste the query below in the editor and press the play button to get a list
 of available todos:
```graphql
query myQuery{
  todos {
    id
    description
    completed
  }
}
```

Fetch a single todo:

```graphql
query fetchTodo {
  todo(todoId: "1") {
    success
    errors
    todo { id completed description dueDate }
  }
}
```

To add a new todo, type a mutation in the editor, similar to the one below:
```graphql
mutation newTodo {
  createTodo(input:{description:"Go to the gym", dueDate:"25-10-2021"}) {
    description
    dueDate
    completed
  }
}
```

