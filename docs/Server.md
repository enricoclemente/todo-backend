# Server functionalities description

This is a simple implementation of a backend made with Flask.  
REST APIs were chosen rather than GraphQL API because the data are simple and unstructured. It also avoids overhead making the application faster.

## REST APIs

- GET       `/api/todos`
  - Description: get the list of todos
  - Query Params: none
  - Request body: empty
  - Response body: list of todos [{id: string, text: string, date: Date, done: boolean, important: boolean}, ...]

- POST      `/api/todos`
  - Description: create a new todo record
  - Query Params: none
  - Request body: {todo: {id: string, text: string, date: Date, done: boolean, important: boolean}}
  - Response body: todo object {id: string, text: string, date: Date, done: boolean, important: boolean}

- PUT       `/api/todos/:todo_id`
  - Description: update a todo record
  - Query Params: none
  - Request body: one or more of the following fields: text: string, date: Date, done: boolean, important: boolean}
  - Response body: todo object {id: string, text: string, date: Date, done: boolean, important: boolean}

- DELETE    `/api/todos/:todo_id`
  - Description: delete a todo record
  - Query Params: none
  - Request body: empty
  - Response body: null

## Database

Server implemented with SQLite. DB file: "../app/instance/todos.sqlite3"

- Table **`todos`**: 
  - Fields: id: string, text: string, date: Date, done: boolean, important: boolean
  - Primary keys: id
  - Foreign keys: none
  - Description: contains the todos with their informations
