# dockerized fastapi api demo

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

To reference docs or to view the interactive API documentation, powered by Swagger UI, use `http://localhost:8002/docs:`


To run tests

```
docker-compose exec web pytest .
```

## Reference:

https://testdriven.io/blog/fastapi-crud/

## Explanation Notes

Unlike Django and flask, FastAPI does not have a built-in development server. So, we'll use Uvicorn, an ASGI server, to serve up FastAPI.

Two environment variables:

`PYTHONDONTWRITEBYTECODE`: Prevents Python from writing pyc files to disc (equivalent to python -B option)

`PYTHONUNBUFFERED`: Prevents Python from buffering stdout and stderr (equivalent to python -u option)

### Uvicorn cmd in docker-compose file
When the container spins up, Uvicorn will run with the following settings:

- `--reload` enables auto-reload so the server will restart after changes are made to the code base.
- `--workers 1` provides a single worker process.
- `--host 0.0.0.0` defines the address to host the server on.
- `--port 8000` defines the port to host the server on.

`app.main:app` tells Uvicorn where it can find the FastAPI ASGI application -- e.g., "within the 'app' module, you'll find the ASGI app, `app = FastAPI()`, in the 'main.py' file.