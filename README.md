# Fastapi with Pytest dockerized demo

Disclaimer: This is not my original work. It is a clone from this [tutorial](https://testdriven.io/blog/fastapi-crud/)


## Objectives

Develop and test an asynchronous API with FastAPI, Postgres, Pytest, and Docker using Test-Driven Development (TDD)

- Develop a asynchronous RESTful API with Python and FastAPI
- Practice TDD with Pytest
- Interact with a Postgres database asynchronously
- Containerize FastAPI and Postgres inside a Docker container
- Parameterize test functions and mock functionality in tests with Pytest
- Document a RESTful API with Swagger/OpenAPI


## Dependencies:

```
FastAPI v0.46.0
Docker v19.03.5
Python v3.8.1
Pytest v5.3.2
Databases v0.2.6
```

## How to run

Build the image and spin up the container:

```
$ docker-compose up -d --build
```

Navigate to `http://localhost:8002/ping`. You should see:

```
{
  "ping": "pong!"
}
```

## SWAGGER API Documenation

To reference docs or to view the interactive API documentation, powered by Swagger UI, use `http://localhost:8002/docs:`

## Run tests

```
docker-compose exec web pytest .
```

## Reference:

https://testdriven.io/blog/fastapi-crud/

## Explanation Notes

### Dockerfile

Unlike Django and flask, FastAPI does not have a built-in development server. So, we'll use Uvicorn, an ASGI server, to serve up FastAPI.

#### environment variables:

`PYTHONDONTWRITEBYTECODE`: Prevents Python from writing pyc files to disc (equivalent to python -B option)

`PYTHONUNBUFFERED`: Prevents Python from buffering stdout and stderr (equivalent to python -u option)

#### Uvicorn cmd in docker-compose file
When the container spins up, Uvicorn will run with the following settings:

- `--reload` enables auto-reload so the server will restart after changes are made to the code base.
- `--workers 1` provides a single worker process.
- `--host 0.0.0.0` defines the address to host the server on.
- `--port 8000` defines the port to host the server on.

`app.main:app` tells Uvicorn where it can find the FastAPI ASGI application -- e.g., "within the 'app' module, you'll find the ASGI app, `app = FastAPI()`, in the 'main.py' file.


## CRUD Route api

| Endpoint | HTTP Method | Description 
-----------|-------------|------------
| /notes   | GET | Get all notes 
| /notes/:id/   | GET | Get a particular note
| /notes   | POST | add a note
| /notes   | PUT | Update a note 
| /notes   | DELETE | Delete a note 


## TDD

=> Write a test 
=> run (RED) 
=> Write enough code to pass the test (GREEN) 
=> Refactor 

## API Versioning with APIRouter

Use FastApi's APIRouter

## Postgresql setup

add a service to the docker-compose.yml file, add the appropriate environment variables, and install asyncpg.

SQLAlchemy `engine`: used for communicating with the database 
`Metadata` instance: used for creating the database schema.

`databases` is an async SQL query builder that works on top of the `SQLAlchemy Core` expression language.

command to ensure the `notes` table was created: 

```
docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev
```

## Pydantic

[docs](https://pydantic-docs.helpmanual.io/)
It enforces type hints at runtime, and provides user friendly errors when data is invalid.
Define how data should be in pure, canonical python; validate it with pydantic.

## Monkeypatch

[docs](https://docs.pytest.org/en/latest/monkeypatch.html)
Some tests use the Pytest monkeypatch fixture to mock out the crud.post function. 
Helps to invoke functionality which depends on global settings or which invokes code which cannot be easily tested such as network access.
The monkeypatch fixture helps you to safely set/delete an attribute, dictionary item or environment variable, or to modify sys.path for importing.

## Parameterize decorator

Pytest has a `parametrize` decorator to parametrize the arguments for the test_update_note_invalid function.