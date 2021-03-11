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
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"user","password":"secret_password", "password2":"secret_password"}' \
  http://localhost:8000/api/auth/register/
```

### Create todo
```shell

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
