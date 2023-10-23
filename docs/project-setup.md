# Project setup guide

## Requirements

- Python 3.11+
- _(Optional)_ - Docker
- _(Optional)_ - Docker Compose

## Installation

#### Via Poetry (recommended)

The recommended way to install all the dependencies is via poetry. For that
first make sure [Poetry](https://pypi.org/project/poetry/) is installed.
```bash
pip install poetry
```

Then, simply run:
```bash
make install
```
This will create install all the dependencies using poetry, create a
virtual environment and activate it.

#### Via Pip
Make sure you are in a virtual environment and install all the required
dependencies in a virtual environment which are present in the
`requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Running the application

There are multiple ways to run the application which are listed below.

> NOTE: All the environment variables are available in the `.env` file.
>
> Additionally, a sample production env file `.env.prod` is kept for demo
> purposes.

1. ### Using make commands

   The `Makefile` takes care of everything and is the recommended way
   to spin things up. It will tear down, rebuild and start the
   docker containers using docker compose.

   Simply run:

   ```bash
   make server
   ```

2. ### Using Docker Compose

   Using docker compose to spin up the application.
   It'll setup a container with the app

   Simply run:

   ```bash
   docker compose up
   ```

   This spins up several things and ties everything together:
   - Database
   - Redis
   - 2 Worker clients
   - Celery beat
   - Flower

   _NOTE: The `WORKER_REPLICA_COUNT` environment variable controls the number
   of worker instances to be spawned._

3. ### Pythonic way

   Sometimes it takes time to spin up the containers. So you can use the more
   pythonic ways to get the application running. The following things have to
   be made available first:

   - [Install the dependencies](./project-setup.md#installation)
   - [Load environment variables](./project-setup.md#load-environment-variables)

   With that done, you can run the application independently.

   #### Start the local dev server
   This uses `uvicorn` to spin up the fastapi app.

   ```bash
   make dev
   ```
   OR
   ```bash
   uvicorn shortest.app:bootload --reload
   ```

   #### Spin up with Gunicorn
   The worker process will do the major task of executing each task

   ```bash
   make run
   ```
   OR
   ```bash
   gunicorn shortest.app:bootload --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```
   > NOTE: The number of gunicorn workers have been limited to `1`, since we
   > are strictly keeping things in-memory. Gunicorn workers have separate memory
   > space and we might have misses while decoding urls therefore to prevent it
   > we'll stick to 1 worker. However, shall you choose to introduce more
   > workers, switch to a sharey memory resource like Redis and implement
   > caching through it.


## Running Tests

Pytest is being used for testing making it easier to test.

Simply run:
```bash
make test
```
OR
```
python -m pytest
```

If you wish to execute tests from a specific test file, run:
```
python -m pytest tests/v1/test_api.py
```
and for running very specific tests, run:
```
python -m pytest tests/v1/test_api.py::test_encode
```

## Load environment variables

In order to run the application, you need some environment variables in place.
All the variables are stored in `.env` folder.

For development, use the ones in `.env` file.

> Note:
>
> To load environment variables if you're a terminal person, you might want
> to use [direnv](https://direnv.net/). Simply, make the variables present
> in `.env` file available by exporting them in a `.envrc` file
> at the root directory.

