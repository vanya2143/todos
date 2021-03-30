# todos
This is a to-do list app. 
This application uses: django rest framework to create api and jwt to create token authentication system.


## Run
1. Clone project and create virtualenv
```shell
git clone https://github.com/vanya2143/todos.git
cd todos
pip3 install virtualenv
python3 -m venv .env
```

2. Activate virtualenv, install requirements and runserver
```shell
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage
Use [curl](https://en.wikipedia.org/wiki/CURL) utility in code examples

### Registration user
```shell
curl --request POST \
  --header "Content-Type: application/json" \
  --data '{"username":"user","password":"secret_password"}' \
  http://localhost:8000/api/auth/register/
```
Response:
```log
{"username":"user"}
```

### Get jwt token
```shell
curl --request POST \
  --header "Content-Type: application/json" \
  --data '{"username":"user","password":"secret_password"}' \
  http://localhost:8000/api/auth/token/
```
Response:
```json
{
    "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNTU3MTgwMiwianRpIjoiMzhjODE0Njc1MWEyNDI2OGE1NGI0ZDI1OTJlNTdiM2QiLCJ1c2VyX2lkIjo0fQ.YqHPS57ez1RZkADAqo3VZTWe3ubU9ooGVtUukqlePPI",
    "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE1NDg3MjAyLCJqdGkiOiI4Yzk0MDhhNzZjNDU0MzM5ODYyNWQyZjc2YTYxNzdiYiIsInVzZXJfaWQiOjR9.BtIimdMKnDWN7DkeBtCfXbLqJwoDnpO_VeGlLOaRFHA"
}
```
We store the access token in a variable for a shorter string length
```shell
TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE1NDg3MjAyLCJqdGkiOiI4Yzk0MDhhNzZjNDU0MzM5ODYyNWQyZjc2YTYxNzdiYiIsInVzZXJfaWQiOjR9.BtIimdMKnDWN7DkeBtCfXbLqJwoDnpO_VeGlLOaRFHA"
```

### Create todo
Writable fields:
```shell
{
    "title": "Todo title",
    "body": "Todo body!",
    "done": false  # true - If you have done this todo
}
```
Request:

We used an access token from [get-jwt-token](https://github.com/vanya2143/todos#get-jwt-token)
```shell
curl --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data '{"title":"My First Todo","body":"Todo body"}' \
  http://localhost:8000/api/todos/
```
Response:
```json
{
  "id":2,
  "title":"My First Todo",
  "body":"Todo body",
  "done":false,
  "owner":"user",
  "url":"http://localhost:8000/api/todos/2",
  "created":"2021-03-11T18:01:32.599423Z"
}
```

### Get all todos
```shell
curl --request GET \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  http://localhost:8000/api/todos/
```
Reaponse:
```json
[
  {
    "id":2,
    "title":"My First Todo",
    "body":"Todo body",
    "done":false,
    "owner":"user",
    "url":"http://localhost:8000/api/todos/2",
    "created":"2021-03-11T18:01:32.599423Z"
  }
]
```
### Update todo
Now we have completed the task and want change "done" field.

The url has a task id `http://localhost:8000/api/todos/` + `id` 
```shell
curl --request PUT \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  --data '{"title":"My First Todo","body":"Todo body", "done": "true"}' \
  http://localhost:8000/api/todos/2 # 2 it's task id
```
Response:
So, we see that the "done" field has changed.
```json
{
  "id":2,
  "title":"My First Todo",
  "body":"Todo body",
  "done":true,
  "owner":"user",
  "url":"http://localhost:8000/api/todos/2",
  "created":"2021-03-11T18:01:32.599423Z"
}
```
### Delete todo
```shell
curl --request DELETE \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  http://localhost:8000/api/todos/2
```
Response:
```log
HTTP/1.1 204 No Content
```
### List users
We can list all users with their tasks. We need administrator rights for this request.
```shell
curl --request GET \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${TOKEN}" \
  http://localhost:8000/api/users/
```
Response:
```json
{
  "count":3,
  "next":null,
  "previous":null,
  "results":
  [
    {
      "id":1,
      "username":"admin",
      "url":"http://localhost:8000/api/users/1",
      "todos": []
    }, 
    {
      "id":4,
      "username":"user",
      "url":"http://localhost:8000/api/users/4",
      "todos":
      [
        "http://localhost:8000/api/todos/4"
      ]
    }
  ]
}
```
