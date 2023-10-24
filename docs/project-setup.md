# Project setup guide

## Requirements

- Python 3.11+
- Redis
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
   It'll setup a container with the app and redis.

   Simply run:

   ```bash
   docker compose up
   ```

   This spins up several things and ties everything together:
   - API worker
   - Redis

3. ### Pythonic way

   Sometimes it takes time to spin up the containers. So you can use the more
   pythonic ways to get the application running. The following things have to
   be made available first:

   - [Install the dependencies](./project-setup.md#installation)
   - [Load environment variables](./project-setup.md#load-environment-variables)
   - [Provision redis](./project-setup.md#running-redis)

   With that done, you can run the application independently.

   You can also choose which config to follow by setting the `ENV_FILE`
   environment variable `export ENV_FILE=.env` but for running things locally
   use the `.env`

   #### Start the local dev server
   This uses `uvicorn` to spin up the fastapi app. Please make sure Redis is up
   and running.

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
   gunicorn shortest.app:bootload --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```


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


## Running Redis

1. If you have Redis locally
   [installed](https://redis.io/docs/getting-started/installation/) then it's
   fairly easy to run it. Simply run:
   ```
   redis-server
   ```
   This will make the server available at `localhost:6379`

2. _(Recommended)_  Run Redis via docker compose. Simply execute:
   ```
   docker compose up redis
   ```
   This will make the server available at `redis:6379` using default port forwarding.
   If you are running redis this way then please `export ENV_FILE=.env.prod`
   use the `.env.prod` file or set the `redis_host=redis` instead of
   `redis_host=localhost` since hostname should match the service name in
   `docker-compose.yml`.


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

