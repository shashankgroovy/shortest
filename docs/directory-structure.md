# Directory Structure

```
.
├── docs
├── shortest
│   └── v1
└── tests
    └── v1
```

## Root level

At the root level, you'll find:

- `Makefile` with various commands to run servers, docker containers, perform
  lint checks and run tests.
- `Dockerfile`, `docker-compose.yml` file for containerzing and running things
  locally.
- `poetry.lock` file for installing python packages (recommended) and
  `requirements.txt` file as well.
- `pyproject.toml` for build tools configurations.
- `.env` and `.env.prod` file as samples for running things locally and in
  production mode using docker compose. For real scenarios, environment
  variables should be absorbed from compute servers.

## `docs`

The `docs` folder contains all the documentation.

## `shortest`

The `shortest` folder is where the entire application is packaged and can be
run as a python fastapi project. It has one sub folder:

- **v1** - It houses `v1` api routes including `/v1/encode` and `/v1/decode`,
  mutator and hash computing processor files.
- **config.py** - Holds settings to be fetched from environment variables.
- **utils** - Holds utility files like logger, cache and configuration loader.

## `tests`

The `tests` folder houses tests for `v1` api.
Read how to [run tests](./project-setup.md#running-tests)
