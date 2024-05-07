# Server functionalities description

## REST APIs

- GET       `/api/todos`
  - Description: get the list of todos
  - Query Params: none
  - Request body: empty
  - Response body: list of todos [{id, text, date, done, important}, ...]

- POST      `/api/todos`
  - Description: create a new todo record
  - Query Params: none
  - Request body: {todo: {id, text, date, done, important}}
  - Response body: todo object {id, text, date, done, important}

- PUT       `/api/todos/:todo_id`
  - Description: update a todo record
  - Query Params: none
  - Request body: {done, important}
  - Response body: todo object {id, text, date, done, important}

- DELETE    `/api/todos/:todo_id`
  - Description: delete a todo record
  - Query Params: none
  - Request body: empty
  - Response body: null

## Database

Server implemented with SQLite. DB file: "../app/instance/todos.sqlite3"

- Table **`todos`**: id, text, date, done, important
  - Primary keys: id
  - Foreign keys: none
  - Description: contains the todos with their informations
