# todos
This is to do list app written in Django Rest Framework


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
In code examples usage curl utility

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
```shell
curl --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE1NDg3MjAyLCJqdGkiOiI4Yzk0MDhhNzZjNDU0MzM5ODYyNWQyZjc2YTYxNzdiYiIsInVzZXJfaWQiOjR9.BtIimdMKnDWN7DkeBtCfXbLqJwoDnpO_VeGlLOaRFHA" \
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

```
### Update todo
```shell

```
### Delete todo
```shell

```
### List users
```shell

```

## Project structure
